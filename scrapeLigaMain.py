import sys
import re
import xlwt
from xlwt import Workbook

import scrapeLigaGetAll
import scrapeLigaTable
URLONEPIECETABLES = "https://www.ligaonepiece.com.br/?view=cards/edicoes"

PTCGSETCODES = [
    "730%20ed=MEG",
    "722%20ed=WHT",
    "721%20ed=BLK",
    "706%20ed=DRI",
    "654%20ed=JTG",
    "649%20ed=PRE",
    "639%20ed=SSP",
    "730%20ed=MEG",
    "557%20ed=SFA",
    "538%20ed=TWM",
    "529%20ed=TEF",
    "505%20ed=PAF",
    "439%20ed=PAR",
    "411%20ed=MEW",
    "406%20ed=OBF",
    "391%20ed=PAL",
    "343%20ed=SV1"
]

def scrapeAllOPTCG():
    wb = Workbook()
    ws = wb.add_sheet("Prices")
    ws.write(0, 0, 'Set Code')
    ws.write(0, 1, 'Card Name')
    ws.write(0, 2, 'Price Liga (R$)')
    columnc = 1
    rowc = 0

    setlist = scrapeLigaGetAll.main(URLONEPIECETABLES)
    for set in setlist:
        prices = scrapeLigaTable.main(set)
        for p in prices:
            for item in p:
                ws.write(columnc, rowc, item)
                rowc +=1
            print(' '.join(p))
            rowc = 0
            columnc +=1
        wb.save('ligaop.xls')

def scrapeAllPTCG():
    wb = Workbook()
    ws = wb.add_sheet("Prices")
    ws.write(0, 0, 'Set Code')
    ws.write(0, 1, 'Card Name')
    ws.write(0, 2, 'Price Liga (R$)')
    columnc = 1
    rowc = 0
    setlist = PTCGSETCODES
    for set in setlist:
        url = "https://www.ligapokemon.com.br/?view=cards/search&card=edid=" + set
        prices = scrapeLigaTable.main(set)
        for p in prices:
            for item in p:
                ws.write(columnc, rowc, item)
                rowc += 1
            print(' '.join(p))
            rowc = 0
            columnc += 1
        wb.save('ligaptcg.xls')



if __name__=="__main__":
    pass