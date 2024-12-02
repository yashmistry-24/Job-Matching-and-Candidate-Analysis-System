import cv2
import numpy as np
import tempfile
import os

def process_video(video_file):
    """Extract frames and audio from the video."""
    # Save the video to a temporary file
    temp_dir = tempfile.mkdtemp()
    temp_video_path = os.path.join(temp_dir, "video.mp4")
    with open(temp_video_path, "wb") as f:
        f.write(video_file.read())

    # Load the video
    cap = cv2.VideoCapture(temp_video_path)
    frames = []
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()

    # Assuming the audio is extracted here
    audio_file_path = extract_audio(temp_video_path)  # This should be a function to extract audio
    return audio_file_path

def extract_audio(video_path):
    """Extract audio from video."""
    # Assuming ffmpeg or a similar tool is installed for audio extraction
    audio_path = video_path.replace(".mp4", ".wav")
    os.system(f"ffmpeg -i {video_path} {audio_path}")
    return audio_path
