import os
import random
import shutil

source = "frames"
train_img = "dataset/images/train"
val_img = "dataset/images/val"

os.makedirs(train_img, exist_ok=True)
os.makedirs(val_img, exist_ok=True)

images = os.listdir(source)
random.shuffle(images)

split = int(len(images) * 0.8)

train_files = images[:split]
val_files = images[split:]

for f in train_files:
    shutil.copy(os.path.join(source, f), train_img)

for f in val_files:
    shutil.copy(os.path.join(source, f), val_img)

print("Dataset split completed!")