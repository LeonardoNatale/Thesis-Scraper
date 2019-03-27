from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.canecaccia.com/2017_2018/")
bsObj = BeautifulSoup(html, "html.parser")
# The main comparison table is currently the first table on the page
links = bsObj.findAll("a")
print(links)
