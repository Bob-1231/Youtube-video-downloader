from pytube import YouTube

# Get the video URL
video_url = input("Input the video url you want to download: ")

# Create a YouTube object
yt = YouTube(video_url)

# Get the video with the highest resolution
video = yt.streams.get_highest_resolution()

# Set the download location
video.download(r"/path/to/the/location/you/want")