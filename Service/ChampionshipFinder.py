from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


class ChampionshipFinder:

    def __init__(self):
        self.root = "https://www.canecaccia.com/"

    def find_championships(self, season):

        try:
            html = urlopen(self.root + season)
            bsObj = BeautifulSoup(html, "html.parser")

            children = bsObj.find("a", string='Home')
            navigation_bar = children.parent.parent
            campionati = navigation_bar.findAll("li", recursive=False)[1:5]  # Ho lista campionati
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(self.root + "could not be found")

        return campionati
