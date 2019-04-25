from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


class ResultsFinder:

    def __init__(self):
        self.root = "https://www.canecaccia.com/2017_2018/"

    def find_results(self, url):

        try:
            html = urlopen(self.root + url)
            bsObj = BeautifulSoup(html, "html.parser")
            squadre = bsObj.findAll("b")

        except HTTPError as e:
            print(e)
        except URLError as e:
            print(self.root + "could not be found")

        return squadre

