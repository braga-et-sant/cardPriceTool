import time

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
        try:
            cards = scrapeCMGetAllPages.main(set) #.replace(" ", "-").replace(":", ""))
        except Exception as e:
            print(e)
            print("Error printing set. Possibly 503. Waiting three minutes then trying again")
            time.sleep(200)
            try:
                cards = scrapeCMGetAllPages.main(set)
            except Exception as e:
                print("Definitive error. Skipping set")


        print("Printing cards:")
        print(cards)
        index = scrapeCMGetPricesOfPage.main(cards, ws, wb, index) + 1
    print("wrote a set")


if __name__=="__main__":
    main()