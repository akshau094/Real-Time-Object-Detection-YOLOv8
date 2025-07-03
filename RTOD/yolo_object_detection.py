# Import required packages
from ultralytics import YOLO
import cv2
import numpy as np
import time
from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils

# Parse command line arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", default="yolov8n.pt",
    help="path to YOLO model")
ap.add_argument("-c", "--confidence", type=float, default=0.25,
    help="minimum probability to filter weak detections")
ap.add_argument("-t", "--threshold", type=float, default=0.45,
    help="threshold for non-maxima suppression")
args = vars(ap.parse_args())

# Load the YOLO model
print("[INFO] loading YOLO model...")
model = YOLO(args["model"])

# Initialize the video stream and FPS counter
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)  # Warm up the camera
fps = FPS().start()

# Process frames from the video stream
while True:
    # Grab and resize the frame
    frame = vs.read()
    frame = imutils.resize(frame, width=640)
    
    # Run YOLOv8 inference on the frame
    results = model(frame, conf=args["confidence"])
    
    # Process the results
    for r in results:
        boxes = r.boxes
        
        for box in boxes:
            # Get box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            # Get confidence and class
            confidence = float(box.conf[0])
            cls = int(box.cls[0])
            class_name = model.names[cls]
            
            # Draw bounding box and label
            color = (0, 255, 0)  # Green color for bounding box
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            
            # Create label with class name and confidence
            label = f"{class_name}: {confidence:.2f}"
            
            # Calculate label position
            y = y1 - 15 if y1 - 15 > 15 else y1 + 15
            
            # Put text on the frame
            cv2.putText(frame, label, (x1, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
    # Show the output frame
    cv2.imshow("Frame", frame)
    
    # Check for 'q' key to break the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    
    # Update the FPS counter
    fps.update()

# Stop the timer and display FPS information
fps.stop()
print(f"[INFO] Elapsed time: {fps.elapsed():.2f}")
print(f"[INFO] Approximate FPS: {fps.fps():.2f}")

# Clean up
cv2.destroyAllWindows()
vs.stop()