import os
import cv2

video_folder = "videos"
output_folder = "frames"

os.makedirs(output_folder, exist_ok=True)

for video in os.listdir(video_folder):
    video_path = os.path.join(video_folder, video)

    cap = cv2.VideoCapture(video_path)
    count = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

        if count % 5 == 0:  # every 5th frame
            frame_name = f"{video}_{count}.jpg"
            cv2.imwrite(os.path.join(output_folder, frame_name), frame)

        count += 1

    cap.release()

print("Frames extracted successfully!")