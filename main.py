import re
from Service.TableFinder import TableFinder
from Service.TableWriter import TableWriter
from Service.ChampionshipFinder import ChampionshipFinder

seasons = ["2017_2018", "2016_2017", "2015_2016", "2014_2015"]
# seasons = ["2014_2015"]
table_types = ["Table", "Score"]

championship_finder = ChampionshipFinder()
table_finder = TableFinder()
table_writer = TableWriter()

j = 0
counter = 0
for season in seasons:
    campionati = championship_finder.find_championships(season)
    counter = 0
    for i in range(0, len(campionati)):
        links = campionati[i].findAll("a", {"href": re.compile("^(?!.*prom)^(?!.*piem).*(gen|mar).*")})
        for link in links:
            # print(link["href"])
            table_url = table_finder.find_table(link["href"], season)
            table_type = table_types[j % 2]
            # print(table_url)
            table_writer.write_table(table_url, season, table_type, counter)
            j += 1
            add = 1 if j % 2 == 0 else 0
            counter += add
