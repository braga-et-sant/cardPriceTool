from time import sleep

from xlwt import Workbook

import scrapeCMGetPage
import scrapeCMsingle

def main(pageList, sheet, book, index):
    newindex = index
    namesetprice = []
    print(pageList)
    for i in pageList:
        print(i)
        value = (scrapeCMsingle.main(i))
        sleep(0.11)
        namesetprice.append(value)
        print("Writing to sheet:")
        print(value)
        sheet.write(newindex, 0, value[1])
        sheet.write(newindex, 1, value[0])
        sheet.write(newindex, 2, value[2])
        newindex = newindex + 1
        book.save('cardmarket.xls')

    book.save('cardmarket.xls')
    return newindex

if __name__=="__main__":
    pass
    # wb = Workbook()
    # ws = wb.add_sheet("Prices", cell_overwrite_ok=True)
    #
    #
    #
    # testpage = scrapeCMGetPage.main("https://www.cardmarket.com/en/OnePiece/Products/Singles/500-Years-into-the-Future?idRarity=0&sortBy=collectorsnumber_asc")
    # test = main(testpage, ws, wb, 1)
    #
    # wb.save('cardmarkettest.xls')
    # for i in test:
    #     print(i)
    #     print(i[0])
    #     print(i[1])
    #     print(i[2])