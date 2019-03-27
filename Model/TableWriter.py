import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


class TableWriter:
    def __init__(self, season):
        self.root = "https://www.canecaccia.com/"
        self.season = season
        pass

    def write_table(self, url, name):

        html = urlopen(self.root + self.season + "/serieBA/class_gen.php")
        bsObj = BeautifulSoup(html, "html.parser")
        # The main comparison table is currently the first table on the page
        table = bsObj.findAll("table")[0]
        rows = table.findAll("tr")

        csvFile = open("url", 'wt', newline='', encoding='utf-8')
        writer = csv.writer(csvFile)
        try:
            for row in rows:
                csvRow = []
                for cell in row.findAll(['td', 'th']):
                    csvRow.append(cell.get_text())
                writer.writerow(csvRow)
        finally:
            csvFile.close()