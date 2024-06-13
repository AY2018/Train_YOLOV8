import os
from PIL import Image

# Define the directories
image_dir = '/Users/ayoub/Desktop/YOLOV8_2/dataset/images/train/'
label_dir = '/Users/ayoub/Desktop/YOLOV8_2/dataset/labels/train/'

# Get list of images and labels
image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg') or f.endswith('.png')]
label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]

# Function to inverse image and save with new name
def inverse_image(image_path, new_image_path):
    image = Image.open(image_path)
    inverted_image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    inverted_image.save(new_image_path)

# Function to inverse YOLO coordinates and save with new name
def inverse_yolo_coordinates(label_path, new_label_path):
    with open(label_path, 'r') as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        data = line.strip().split()
        class_id = data[0]
        coords = list(map(float, data[1:]))

        inverted_coords = []
        for i in range(0, len(coords), 2):
            x = coords[i]
            inverted_x = 1 - x  # Inverse x-coordinate
            inverted_coords.append(inverted_x)
            inverted_coords.append(coords[i + 1])

        new_line = f"{class_id} {' '.join(map(str, inverted_coords))}\n"
        new_lines.append(new_line)

    with open(new_label_path, 'w') as file:
        file.writelines(new_lines)

# Process each image and its corresponding label
for image_file in image_files:
    image_path = os.path.join(image_dir, image_file)
    new_image_path = os.path.join(image_dir, image_file.replace('.jpg', '_inv.jpg').replace('.png', '_inv.png'))
    
    label_path = os.path.join(label_dir, image_file.replace('.jpg', '.txt').replace('.png', '.txt'))
    new_label_path = os.path.join(label_dir, image_file.replace('.jpg', '_inv.txt').replace('.png', '_inv.txt'))

    if os.path.exists(label_path):
        inverse_image(image_path, new_image_path)
        inverse_yolo_coordinates(label_path, new_label_path)
