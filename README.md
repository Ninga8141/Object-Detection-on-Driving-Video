📝 Project Write-Up: Object Detection on Driving Video

This project implements object detection on driving videos using the YOLOv8 deep learning model. The system processes video frames in real time and detects common road objects such as cars, buses, trucks, motorcycles, and pedestrians, drawing bounding boxes and class labels on each frame.

The objective of this project is to demonstrate the practical application of computer vision in autonomous driving and traffic analysis scenarios.

The solution is built using Python, OpenCV, and the Ultralytics YOLOv8 framework. A lightweight YOLOv8 Nano model was chosen to ensure fast inference and low computational overhead while maintaining good detection accuracy.

This project showcases skills in:

Computer vision fundamentals

Deep learning model integration

Video processing using OpenCV

Python-based project structuring

---

## 📌 Project Objectives
- Detect multiple road objects from driving videos
- Apply a pre-trained deep learning model for real-time inference
- Visualize detections with bounding boxes and labels
- Measure performance using FPS (Frames Per Second)
- Build a clean, modular, and reusable computer vision pipeline

---

## 🧠 Model Used
- **YOLOv8 Nano (`yolov8n.pt`)**
- Developed by **Ultralytics**
- Pre-trained on the **COCO dataset**
- Chosen for:
  - High inference speed
  - Low computational cost
  - Real-time performance on CPU

---

## 🛠️ Technologies & Tools
- **Python**
- **OpenCV** – video processing and visualization
- **Ultralytics YOLOv8** – object detection
- **NumPy**
- **Git & GitHub** – version control
- 
- Before: Take a screenshot of the original video frame
- ![image alt](https://github.com/Ninga8141/Object-Detection-on-Driving-Video/blob/18ce3e2f3c823df7d88267cb849dacc24bee98b7/Screenshots/Screenshot%20(25).png)
- ![image alt](https://github.com/Ninga8141/Object-Detection-on-Driving-Video/blob/e76e92a14dcad3d3847cfbea449d2805335e38b8/Screenshots/Screenshot%20(21).png)
- 
After: Take a screenshot from output_detected.mp4 (with bounding boxes)
- ![image alt](https://github.com/Ninga8141/Object-Detection-on-Driving-Video/blob/a56b65f566d9c6ed9f5b27649168d8ec8c6207f6/Screenshots/Screenshot%20(16).png)
- ![image alt](https://github.com/Ninga8141/Object-Detection-on-Driving-Video/blob/05d377ecc4d306cdd36b86b895d0cff514be45e2/Screenshots/Screenshot%20(12).png)

  ## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Ninga8141/Object-Detection-on-Driving-Video.git
cd Object-Detection-on-Driving-Video
2️⃣ Create a Virtual Environment (Recommended)
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
▶️ How to Run the Project
Place your driving video file inside the project folder

Update the video path in run_detection.py

Run the script:

bash
Copy code
python run_detection.py
The application will:

Read the video frame-by-frame

Detect objects using YOLOv8

Draw bounding boxes and class labels

Display the processed output in real time

🧩 Code Explanation
run_detection.py
Loads the YOLOv8 model using the Ultralytics library

Captures video frames using OpenCV

Performs object detection on each frame

Draws bounding boxes with class names and confidence scores

Displays the output until the video ends or the user exits

This modular flow makes the code easy to understand, extend, and optimize.

📊 Output
Detected objects are highlighted using colored bounding boxes

Each detection includes:

Object class name

Confidence score

Works on recorded driving videos and can be extended to live camera feeds

🚀 Future Enhancements
Real-time webcam detection

Object tracking (DeepSORT)

Vehicle speed estimation

Automatic output video saving

GPU acceleration support

🧠 Skills Demonstrated
Computer Vision fundamentals

Deep Learning model integration

Video processing using OpenCV

Python programming

Model inference optimization

Git & GitHub workflow


- 
