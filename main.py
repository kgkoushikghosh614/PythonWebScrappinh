import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
Url = "https://money.rediff.com/sectors/bse/teck"
page = requests.get(Url)
Bsoup = BeautifulSoup(page.content, 'html.parser')
ResultDiv = Bsoup.find(id="leftcontainer")
ResulTabe = ResultDiv.find_all("table")
FinalTable = ResulTabe[0]
NewTempTable = str(FinalTable)

def get_table_headers(table):
    """Given a table soup, returns all the headers"""
    headers = []
    for th in table.find("tr").find_all("th"):
        headers.append(th.text.strip())
    return headers

def get_table_rows(table):
    """Given a table, returns all its rows"""
    rows = []
    for tr in table.find_all("tr")[1:]:
        cells = []
        # grab all td tags in this table row
        tds = tr.find_all("td")
        if len(tds) == 0:
            # if no td tags, search for th tags
            # can be found especially in wikipedia tables below the table
            ths = tr.find_all("th")
            for th in ths:
                cells.append(th.text.strip())
        else:
            # use regular td tags
            for td in tds:
                cells.append(td.text.strip())
        rows.append(cells)
    return rows

def save_as_csv(table_name, headers, rows):
    pd.DataFrame(rows, columns=headers).to_csv(f"{table_name}.csv")


headers = get_table_headers(FinalTable)
Rows = get_table_rows(FinalTable)
save_as_csv(f"RediffFnance", headers, Rows)

Datatable = pd.read_csv('C:\\Users\\DELL\\PycharmProjects\\WebScrapping\\RediffFnance.csv')

print(Datatable)