import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup, element


class ResultsWriter:

    def __init__(self):
        self.root = "https://www.canecaccia.com/"

    def write_results(self, squadre, title):

        title = f"../{title}.csv"
        csvFile = open(title, 'wt', newline='', encoding='utf-8')
        writer = csv.writer(csvFile)

        try:
            for i in range(0, len(squadre)):
                csvRow = clean_team_name(squadre[i].get_text()).split("-")  # inizio riga
                riga = squadre[i].next_sibling
                csvRow += riga[3:13].replace("\xa0", "").split("-")  # aggiungo punteggio finale
                parziali = clean_string(riga[14:])  # trovo punteggi parziali
                risultati_parziali = parziali.split("-")
                if len(risultati_parziali) >= 3:
                    csvRow += risultati_parziali
                else:
                    riga = riga.next_sibling
                    parziali = clean_string(riga.get_text())
                    risultati_parziali = parziali.split("-")
                    if len(risultati_parziali) >= 3:
                        csvRow += risultati_parziali
                    else:
                        riga = riga.next_sibling
                        if isinstance(riga, element.NavigableString) and len(riga) < 50:
                            parziali = clean_string(riga)
                            risultati_parziali = parziali.split("-")
                            csvRow += risultati_parziali

                writer.writerow(csvRow)
        finally:
            csvFile.close()


def clean_string(s):
    s = s.replace("Parziali", "").replace("Patziali", "").replace("\xa0", "").replace(",", "-")\
                                .replace("/", "-").replace("d1ts", "").replace("1ts", "").replace("i", "")
    return s


def clean_team_name(t):
    return t.replace(" ", "").replace("\xa0", "").replace(".", "")
