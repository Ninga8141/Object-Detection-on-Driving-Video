import cv2
import time
from ultralytics import YOLO
import os

# Load YOLOv8 model (lightweight)
model = YOLO("yolov8n.pt")

# Video folder
VIDEO_FOLDER = "video"
videos = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(('.mp4', '.avi', '.mov'))]

if len(videos) == 0:
    raise Exception("No video found in the 'video' folder!")

VIDEO_PATH = os.path.join(VIDEO_FOLDER, videos[0])
OUTPUT_PATH = os.path.join(VIDEO_FOLDER, "output_detected.mp4")

print(f"Processing video: {VIDEO_PATH}")

def run_pipeline(width, height):
    cap = cv2.VideoCapture(VIDEO_PATH)
    fps_list = []

    # Get video properties
    fps_input = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(OUTPUT_PATH, fourcc, fps_input, (width, height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Resize frame
        frame = cv2.resize(frame, (width, height))

        start = time.time()
        results = model(frame, verbose=False)
        end = time.time()

        fps = 1 / (end - start)
        fps_list.append(fps)

        # Draw detections
        annotated_frame = results[0].plot()
        out.write(annotated_frame)  # Save frame to output video

        # Optional: display live detection
        cv2.imshow(f"Detection {width}x{height}", annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    if len(fps_list) > 0:
        avg_fps = sum(fps_list) / len(fps_list)
        print(f"Average FPS at {width}x{height}: {avg_fps:.2f}")
    else:
        print("No frames processed.")

# Run at one resolution (you can run multiple if needed)
print("Running at 640x360")
run_pipeline(640, 360)

print(f"Detected video saved as: {OUTPUT_PATH}")
