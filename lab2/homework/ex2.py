from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

raw_data = conn.read()
page_content = raw_data.decode("utf8")

with open("data_table.html", "wb") as f:
    f.write(raw_data)

soup = BeautifulSoup(page_content, "html.parser")
table = soup.find("table", id="tableContent")
tr_list = table.find_all("tr")

new_list = []
for tr in tr_list:
    td = tr.find_all("td", "b_r_c")
    if len(td) > 0:
        data = OrderedDict({
            "Name": td[0].string,
            "Quý 4-2016": td[1].string,
            "Quý 1-2017": td[2].string,
            "Quý 2-2017": td[3].string,
            "Quý 3-2017": td[4].string
        })
        new_list.append(data)
print(new_list)

pyexcel.save_as(records=new_list, dest_file_name="bao cao tai chinh.xlsx")
    

    
    
        
    

