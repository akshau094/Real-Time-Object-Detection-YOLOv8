# 🎯 Real-Time Object Detection

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/YOLOv8-Ultralytics-green.svg" alt="YOLO Version">
  <img src="https://img.shields.io/badge/OpenCV-4.x-red.svg" alt="OpenCV Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</div>

## 📖 Overview

A sophisticated real-time object detection system built with **YOLOv8** and **OpenCV** that provides instant recognition and tracking of objects through webcam feed. The system delivers high-performance detection with smooth visual feedback and an intuitive user interface.

## ✨ Features

### 🔍 **Advanced Detection Capabilities**
- **Real-time Processing**: Instant object detection with minimal latency
- **Multi-class Recognition**: Detects 80+ object classes from COCO dataset
- **Confidence Scoring**: Adjustable confidence thresholds for precision control
- **Non-Maximum Suppression**: Eliminates duplicate detections for cleaner results

### 🎨 **Visual Experience**
- **Dynamic Bounding Boxes**: Smooth, responsive object highlighting
- **Confidence Display**: Real-time confidence scores for each detection
- **Optimized Performance**: Efficient frame processing with FPS monitoring
- **Clean Interface**: Minimalist design focusing on detection results

### ⚡ **Performance Features**
- **Adaptive Resizing**: Automatic frame optimization for best performance
- **FPS Counter**: Real-time performance monitoring
- **Memory Efficient**: Optimized for continuous operation
- **Graceful Cleanup**: Proper resource management on exit

## 🛠️ Installation

### Prerequisites
```bash
Python 3.8+
Webcam or camera device
```

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/real-time-object-detection.git
cd real-time-object-detection
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install ultralytics opencv-python numpy imutils
```

## 🚀 Usage

### Basic Usage
```bash
python yolo_object_detection.py
```

### Advanced Configuration
```bash
# Custom model
python yolo_object_detection.py -m yolov8s.pt

# Adjust confidence threshold
python yolo_object_detection.py -c 0.5

# Set NMS threshold
python yolo_object_detection.py -t 0.3

# Combined parameters
python yolo_object_detection.py -m yolov8m.pt -c 0.4 -t 0.5
```

## 🎮 Controls

| Key | Action |
|-----|--------|
| `Q` | Quit application |
| `ESC` | Exit gracefully |

## 📊 Technical Architecture

### 🔧 **Core Components**

#### **Model Loading & Initialization**
```python
model = YOLO(args["model"])  # Load YOLOv8 model
vs = VideoStream(src=0).start()  # Initialize video stream
```

#### **Real-time Processing Pipeline**
1. **Frame Capture**: Continuous video stream reading
2. **Preprocessing**: Frame resizing and optimization
3. **Inference**: YOLOv8 object detection
4. **Post-processing**: Bounding box extraction and filtering
5. **Visualization**: Dynamic overlay rendering

#### **Performance Optimization**
- **Efficient Frame Handling**: Using imutils for optimized processing
- **Adaptive Sizing**: 640px width for balanced performance
- **Memory Management**: Proper cleanup and resource handling

### 🎨 **Visual Elements**

#### **Bounding Box Design**
- **Color Scheme**: Professional green (#00FF00) for visibility
- **Line Weight**: 2px thickness for clear definition
- **Adaptive Positioning**: Smart label placement to avoid overlap

#### **Typography & Labels**
- **Font**: OpenCV Hershey Simplex for clarity
- **Size**: 0.5 scale for optimal readability
- **Information Display**: Class name + confidence percentage

#### **Animation & Transitions**
- **Smooth Detection**: Fluid bounding box updates
- **Real-time Feedback**: Instantaneous visual response
- **Performance Indicators**: Live FPS counter integration

## 📈 Performance Metrics

### **Speed Benchmarks**
- **YOLOv8n**: ~45-60 FPS (lightweight)
- **YOLOv8s**: ~35-45 FPS (balanced)
- **YOLOv8m**: ~25-35 FPS (accurate)

### **Accuracy Standards**
- **Confidence Threshold**: 0.25 (adjustable)
- **NMS Threshold**: 0.45 (eliminates duplicates)
- **Detection Classes**: 80 COCO categories

## 🔧 Configuration Options

### **Model Variants**
| Model | Speed | Accuracy | Use Case |
|-------|-------|----------|----------|
| `yolov8n.pt` | Fastest | Good | Real-time applications |
| `yolov8s.pt` | Fast | Better | Balanced performance |
| `yolov8m.pt` | Medium | High | High accuracy needs |
| `yolov8l.pt` | Slow | Higher | Maximum precision |

### **Parameter Tuning**
```bash
# High accuracy mode
python yolo_object_detection.py -m yolov8l.pt -c 0.5 -t 0.3

# Speed optimized mode
python yolo_object_detection.py -m yolov8n.pt -c 0.2 -t 0.5
```

## 🐛 Troubleshooting

### **Common Issues**

#### **Camera Not Found**
```bash
# Check available cameras
python -c "import cv2; print(cv2.VideoCapture(0).isOpened())"
```

#### **Low FPS Performance**
- Use smaller model (yolov8n.pt)
- Reduce frame size
- Close other applications

#### **Memory Issues**
- Ensure sufficient RAM (4GB+ recommended)
- Close unnecessary programs
- Use lighter model variants

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Ultralytics**: For the incredible YOLOv8 framework
- **OpenCV**: For computer vision capabilities
- **COCO Dataset**: For training data and class definitions
- **PyTorch**: For the underlying deep learning framework

## 📞 Support

For issues and questions:
- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/real-time-object-detection/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/real-time-object-detection/discussions)

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/yourusername">Your Name</a></p>
  <p>⭐ Star this repository if you found it helpful!</p>
</div>
