from ultralytics import YOLO


model = YOLO("yolov8l-seg.yaml")  


results = model.train(data="dataset.yaml", epochs=200, imgsz=1280)


# yolo segment predict model=/Users/ayoub/Desktop/YOLOV8_2/runs/segment/train3/weights/best.pt source='/Users/ayoub/Desktop/YOLOV8_2/dataset/images/train/intext_10024-21.jpg' 


