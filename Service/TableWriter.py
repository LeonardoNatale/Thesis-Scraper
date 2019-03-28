import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup


class TableWriter:

    def __init__(self):
        self.root = "https://www.canecaccia.com/"

    def write_table(self, url, season, table_type, counter):

        if url[0] == ".":
            url = self.root + season + url[1:]

        html = urlopen(url)
        bsObj = BeautifulSoup(html, "html.parser")
        # The main comparison table is currently the first table on the page
        table = bsObj.findAll("table")[0]
        rows = table.findAll("tr")

        title = "./" + season + "/" + season+table_type+str(counter)+".csv"
        csvFile = open(title, 'wt', newline='', encoding='utf-8')
        writer = csv.writer(csvFile)
        try:
            for row in rows:
                csvRow = []
                for cell in row.findAll(['td', 'th']):
                    csvRow.append(cell.get_text().replace("\n", "").replace("\r", "").replace("\t", ""))  # to avoid extra spaces
                writer.writerow(csvRow)
        finally:
            csvFile.close()
