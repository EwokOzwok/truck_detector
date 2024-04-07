import os
import cv2

# Function to extract frames from video and resize them
def extract_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    frame_count = 0

    # Read and process each frame
    while True:
        success, frame = video_capture.read()
        if not success:
            break

        # Resize frame to 360x360 pixels
        resized_frame = cv2.resize(frame, (360, 360))

        # Save resized frame
        frame_filename = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_filename, resized_frame)

        frame_count += 1

    # Release the video capture object
    video_capture.release()

# Define the directory containing video files
video_directory = r"C:/Users/intra/OneDrive/Desktop/AI Projects/TL/All Timpse Lapses"

# Define the output folder for resized frames
output_folder = r"C:/Users/intra/OneDrive/Desktop/AI Projects/TL/AllFrames"

# List all video files in the directory
video_files = [file for file in os.listdir(video_directory) if file.endswith('.mp4')]

# Process each video file
for video_file in video_files:
    video_path = os.path.join(video_directory, video_file)
    extract_frames(video_path, output_folder)

print("Frames extraction complete!")
