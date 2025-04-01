from pytube import YouTube

# Replace with the actual YouTube video URL
video_url = 'https://www.youtube.com/watch?v=2vAdx6-aofc&list=RD2vAdx6-aofc&start_radio=1'

yt = YouTube(video_url)

# Get the highest resolution stream
stream = yt.streams

# Download the video
stream.download()