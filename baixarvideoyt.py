import pytube

url = 'https://www.youtube.com/watch?v=KuVAeTHqijk'
youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()

video.download('/home/william/Downloads')
