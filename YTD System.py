from pytube import YouTube
url = 'https://www.youtube.com/watch?v=yU-gJFjH700'
my_video = YouTube(url)
print(my_video.title)
print(my_video.thumbnail_url)
# masic Line
my_video = my_video.streams.get_highest_resolution()
my_video.download()
