import pytube

url = 'LINK DO VIDEO DO YOUTUBE'
youtube = pytube.YouTube(url)
video = youtube.streams.get_highest_resolution()

video.download('/home/william/Downloads')
