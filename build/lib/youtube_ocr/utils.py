import pytesseract
from PIL import Image
from pytube import YouTube

# Set the path to the Tesseract executable (default path on macOS)
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

def download_youtube_video(youtube_link, output_path):
    # Download YouTube video using pytube
    yt = YouTube(youtube_link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(output_path)

def calculate_frame_difference(prev_frame, current_frame):
    # Calculate the absolute difference between two frames
    diff = cv2.absdiff(prev_frame, current_frame)
    
    # Calculate the percentage difference based on the mean color intensity
    percentage_diff = (np.mean(diff) / 255.0) * 100
    
    return percentage_diff

def ocr_on_image(image_path):
    # Open the image using PIL
    image = Image.open(image_path)
    
    # Perform OCR on the image
    text = pytesseract.image_to_string(image)
    
    return text
