from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


class TableFinder:

    def __init__(self):
        self.root = "https://www.canecaccia.com/"

    def find_table(self, url, season):
        if url[0] == ".":
            url = self.root + season + url[1:]

        try:
            html = urlopen(url)
            bsObj = BeautifulSoup(html, "html.parser")
            frame = bsObj.find("iframe")
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(url + "could not be found")

        link = frame["src"]
        if len(link) < 40: # check if part of link hidden
            lista = url.split("/")
            link = "/".join(lista[:-1]) + link[1:]
        return link
