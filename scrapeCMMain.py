
from xlwt import Workbook

import scrapeCMGetAllSets
import scrapeCMGetPricesOfPage
import scrapeCMGetAllPages
URLONEPIECETABLES = "https://www.ligaonepiece.com.br/?view=cards/edicoes"
wb = Workbook()
ws = wb.add_sheet("Prices", cell_overwrite_ok=True)

def main():
    index = 1
    ws.write(0, 0, 'Set Code')
    ws.write(0, 1, 'Card Name')
    ws.write(0, 2, 'Price')
    wb.save('cardmarket.xls')
    setlist = scrapeCMGetAllSets.main("OnePiece")
    print("Printing Setlist:")
    print(setlist)
    for set in setlist:
        print("Printings Set:")
        print(set)
        cards = scrapeCMGetAllPages.main(set) #.replace(" ", "-").replace(":", ""))

        print("Printing cards:")
        print(cards)
        index = scrapeCMGetPricesOfPage.main(cards, ws, wb, index) + 1
    print("wrote a set")


if __name__=="__main__":
    main()