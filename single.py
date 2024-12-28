import yt_dlp

# YouTube video link
link = "https://youtu.be/_J9KTao172U?si=9CtmvkfgYfe0nWmu"

# Save location
SAVE_PATH = r"C:\Users\cemkgenc\Downloads"

# Use custom naming? Set to True for custom name, False for default name
use_custom_name = True
custom_name = "My_Custom_Video_Name" # Custom name for the video (if needed)

# Configure yt-dlp
ydl_opts = {
    'outtmpl': f"{SAVE_PATH}/{'%(title)s' if not use_custom_name else custom_name}.%(ext)s",  # Use default title or custom name
    'format': 'bestvideo[height<=720]+bestaudio/best',  # Download 720p video + best audio
    'merge_output_format': 'mp4',  # Ensure the output file is MP4
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print(f"Video downloaded successfully as {'%(title)s' if not use_custom_name else custom_name}.mp4!")
