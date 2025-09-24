Card Price Tool

A program to quickly lookup all prices from a certain TCG's dataset. 

Files:

scrapeCMGetAllSets - Get all sets from a given TCG

scrapeCMGetAllPages -  Outputs all prices from a given set. 

scrapeCMGetPage - Outputs all prices from a one single page of a set (generally just a helper for the function above)

scrapeCMMain - Given a TCG, performs a full price check of all relevant sets inputed in memory

scrapeCmGetPricesOfPage - Outputs the contents of a price check to a .xls file. Used as a helper for the function above

scrapeCMSingle - Gets the price of the cheapest English NM listing of a card done by a professional seller

scrapeLigaMain - Similar to scrapeCMMain

scrapeLigaGetAll - Returns all card prices from any given sets of a TCG from Liga

scrapeLigaOCR - Gets the price of the cheapest English NM listing of a card, needs to use OCR due to obsfuscation

scrapeLigaPagEdicoes - Gets all sets through the Editions page

ScrapeLigaTable - In construction, intended to handle the difference in structure the PTCG page in Liga has. Currently gets all card prices from a given editions page in Liga




Example usage: 

>----Get all one piece card prices from both sites
>run onePiece() scrape scrapeCMMain.py then onePieceLiga() from scrapeLigaMain.py
>
>
>----Get all prices of cards of EB02 from One piece in Cardmarket
>run print(main("Anime-25th-Collection")) in scrapeCMGetAllPages. You can find most available sets in the OPTCGSETS lists inside scrapeCMMain.py. Just change the string in quotes to another one to try other sets
>
>
>----Get all prices of cards of EB02 from One Piece in LigaYGO
>run  print(main(https://www.ligaonepiece.com.br/?view=cards%2Fsearch&card=+ed%3DEB02&tipo=1)) in scrapeLigaTable.py. You need the actual URL from liga for now since they handle the editions page a bit weirdly, but you can nab any URL after clicking in any given set [here](https://www.ligaonepiece.com.br/?view=cards/edicoes):
