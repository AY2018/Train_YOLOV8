import cv2
import numpy as np
import matplotlib.pyplot as plt
from ultralytics import YOLO

model = YOLO("/Users/ayoub/Desktop/YOLOV8_2/runs/segment/train3/weights/best.pt")

# Perform inference on an image
image_path = "/Users/ayoub/Desktop/YOLOV8_2/dataset/images/train/intext_10024-21.jpg"
results = model.predict(source=image_path)

# Load the original image
image = cv2.imread(image_path)
orig_height, orig_width = image.shape[:2]

# Extract the predictions
predictions = results[0]

# Check if there are masks in the predictions
if hasattr(predictions, 'masks') and predictions.masks is not None:
    # Convert the Masks object to a numpy array
    masks = predictions.masks.data.cpu().numpy()
    
    for mask in masks:
        # Resize the mask to the original image size
        mask_resized = cv2.resize(mask, (orig_width, orig_height))
        
        # Convert mask to uint8 format
        mask_resized = (mask_resized * 255).astype(np.uint8)
        
        # Find contours
        contours, _ = cv2.findContours(mask_resized, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Draw contours on the image
        for contour in contours:
            cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)

# Display the image with masks
plt.figure(figsize=(10, 10))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
