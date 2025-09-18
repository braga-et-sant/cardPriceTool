import sys
import re
import xlwt
from xlwt import Workbook

import scrapeLigaGetAll
import scrapeLigaTable
URLONEPIECETABLES = "https://www.ligaonepiece.com.br/?view=cards/edicoes"


def transformIntoExcel():
    wb = Workbook()
    ws = wb.add_sheet("Prices")
    ws.write(0, 0, 'Set Code')
    ws.write(0, 1, 'Card Name')
    ws.write(0, 2, 'Price')
    wb.save('test.xls')

def scrapeLigaAllPrices():
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
        wb.save('test.xls')

if __name__=="__main__":
    scrapeLigaAllPrices()