import cv2
import os

def extract_frames(video_path, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    
    frame_count = 0
    while True:
        success, frame = video_capture.read()
        if not success:
            break  # Break the loop if no more frames are available
        
        # Save the current frame as an image file
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)
        print(f"Saved: {frame_filename}")
        frame_count += 1
    
    # Release the video capture object
    video_capture.release()
    print(f"Extracted {frame_count} frames to {output_folder}")

# Example usage
video_path = "C:\\Users\\tim\\Projects\\src\\video_input\\GX010211.MP4"  # Replace with your video file path
output_folder = "C:\\Users\\tim\\Projects\\src\\video_output\\GX010211.MP4"  # Replace with your desired output folder
extract_frames(video_path, output_folder)

video_path = "C:\\Users\\YourUsername\\Videos\\input_video.mp4"
output_folder = "C:\\Users\\YourUsername\\Documents\\output_frames"
