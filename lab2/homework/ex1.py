from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs"
conn = urlopen(url)

raw_data = conn.read()
page_content = raw_data.decode("utf8")

with open("itunes.html", "wb") as f:
    f.write(raw_data)

soup = BeautifulSoup(page_content, "html.parser")
section = soup.find("section", "section chart-grid")

li_list = section.find_all("li")
options = {
    "default_search": "ytsearch",
    "max_download": 1,
}
dl = YoutubeDL(options)

new_list = []
for li in li_list:
    a = li.a
    link = url + a["href"]
    top = li.strong.string
    song = li.h3.a.string
    artist = li.h4.a.string
    top_100 = OrderedDict({
        "Top": top,
        "Song": song,
        "Artist": artist,
        "Link": link
    })
    new_list.append(top_100)
    dl.download([song])
print(new_list)

pyexcel.save_as(records=new_list, dest_file_name="TOP_100_Song.xlsx")




