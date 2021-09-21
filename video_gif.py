#%% Import libraries
import cv2

#%% read info about video
video = cv2.VideoCapture('../datasets/videos/file.mp4')
frames_per_second = video.get(cv2.CAP_PROP_FPS)
num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
duration = num_frames/frames_per_second

print(f'Video FPS: {frames_per_second}')
print(f'Total Frames {num_frames}')
print(f'Duration (sec): {duration}')