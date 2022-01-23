from pytube import YouTube
import subprocess
import re
import os

# open the file with the links
link = open('yt_downloader_links.txt','r')

for i in link:
  try:
    # create a youtube object
    yt = YouTube(i)
  except:
    print("Connection Error")

  try:
    # filter audio streams by bitrate and select the best one
    audio = yt.streams.filter(only_audio=True, mime_type='audio/webm').order_by('bitrate').desc().first()
  except:
    print("No audio available")

  try:
    # filter video streams by resolution, select the best one
    video = yt.streams.filter(only_video=True, resolution='1440p', mime_type='video/webm').desc().first()
  except:
    try:
      video = yt.streams.filter(only_video=True, resolution='1080p', mime_type='video/webm').desc().first()
    except:
      try:
        video = yt.streams.filter(only_video=True, resolution='720p', mime_type='video/webm').desc().first()
      except:
        print("No high-quality video available")

  try:
    # download streams to temporary folders
    video_path= video.download("yt_downloads\\video")
    audio_path = audio.download("yt_downloads\\audio")
  except:
    print("An error occured while downloading the files")

  # get the video name
  video_name = repr(video_path).split('\\')
  video_name = re.split("\.", video_name[-1])
  file_name = "yt_downloads\\" + video_name[0] + ".mp4"
  print(video_name[0])

  try:
    # ffmpeg -i input_0.mp4 -i input_1.mp4 -c copy -map 0:v:0 -map 1:a:0 -shortest out.mp4
    subprocess.check_call(["ffmpeg", "-n", "-loglevel", "panic", "-i", video_path, "-i", audio_path, "-c", "copy", "-c:a", "aac", "-map", "0:0", "-map", "1:0", file_name])
    print("--> Download successful")
  except:
    print("--> Video already downloaded (or an error occured)")

  # remove the .webm files
  os.remove(audio_path)
  os.remove(video_path)

# remove temporary folders
os.rmdir("yt_downloads\\audio")
os.rmdir("yt_downloads\\video")

print('Task Completed!') 