import yt_dlp

# Save location
SAVE_PATH = r"C:\Users\cemkgenc\Downloads"

# List of YouTube video links and optional custom names
video_list = [
    {"link": "https://youtu.be/r_QZl1gfxVQ?si=FFs9ZYipWHz7PDGY", "custom_name": "Custom_Video_1"},
    {"link": "https://youtu.be/xyz12345", "custom_name": None},  # Use None for default naming
    {"link": "https://youtu.be/abc67890", "custom_name": "My_Second_Video"}
]

# Function to download videos
def download_videos(videos):
    for video in videos:
        link = video["link"]
        custom_name = video["custom_name"]
        
        # Configure yt-dlp
        ydl_opts = {
            'outtmpl': f"{SAVE_PATH}/{'%(title)s' if not custom_name else custom_name}.%(ext)s",
            'format': 'bestvideo[height<=720]+bestaudio/best',  # Download 720p video + best audio
            'merge_output_format': 'mp4',  # Ensure output is MP4
        }
        
        # Download video
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([link])
            print(f"Downloaded: {custom_name if custom_name else 'Default Title'}")
        except Exception as e:
            print(f"Failed to download {link}: {e}")

# Start downloading
download_videos(video_list)
