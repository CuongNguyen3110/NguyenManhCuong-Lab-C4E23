from youtube_dl import YoutubeDL

#1. Download a single youtube video
# dl = YoutubeDL()
# dl.download(["https://www.youtube.com/watch?v=HXkh7EOqcQ4"])

#2. Download multiple video
# dl = YoutubeDL()
# dl.download(["https://www.youtube.com/watch?v=HXkh7EOqcQ4",\
#  "https://www.youtube.com/watch?v=D164TFHeOcI"])

#3. Download audio
# options = {
#     "format": "bestaudio/audio"
# }
# dl = YoutubeDL(options)
# dl.download(["https://www.youtube.com/watch?v=HXkh7EOqcQ4"])

#4. Search then download the first video
# options = {
#     "default_search": "ytsearch",
#     "max_downloads": 1
# }
# dl = YoutubeDL(options)
# dl.download(["con dien TAMKA PKL"])

#5. Search then download the first audio
options = {
    "format": "bestaudio",
    "default_search": "ytsearch",
    "max_download": 1
}
dl = YoutubeDL(options)
dl.download(["bích phương"])