from ultralytics import YOLO
import os

ROOT_DIR = "C:\\Users\\tthla\\OneDrive\\Documents\\research\YOLO8"
model = YOLO("yolov8n.yaml")
results = model.train(data= os.path.join(ROOT_DIR , "config.yaml"), epochs = 100)