from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


class TableFinder:

    def find_table(self, url):

        html = urlopen(url)
        try:
            bsObj = BeautifulSoup(html, "html.parser")
            frame = bsObj.find("iframe")
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(url + "could not be found")

        return frame["src"]
