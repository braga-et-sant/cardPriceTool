import time

from xlwt import Workbook

import scrapeCMGetAllSets
import scrapeCMGetPricesOfPage
import scrapeCMGetAllPages
wb = Workbook()
ws = wb.add_sheet("Prices", cell_overwrite_ok=True)
PTCGSETS = [
    "Phantasmal Flames",
    "Mega Evolution",
    "White Flare",
    "Black Bolt",
    "Destined Rivals",
    "Journey Together",
    "Prismatic Evolutions",
    "Surging Sparks",
    "Stellar Crown",
    "Shrouded Fable",
    "Twilight Masquerade",
    "Temporal Forces",
    "Paldean Fates",
    "Paradox Rift",
    "151",
    "Obsidian Flames",
    "Paldea Evolved",
    "Scarlet & Violet"
]

OPTCGSETS = [
    # Main sets (release order)
    "Romance Dawn",
    "Romance Dawn (Pre-Errata)",
    "Paramount War",
    "Pillars of Strength",
    "Kingdoms of Intrigue",
    "Awakening of the New Era",
    "Memorial Collection",
    "500 Years into the Future",
    "Two Legends",
    "Emperors in the New World",
    "Royal Blood",
    "Legacy of the Master",
    "A Fist of Divine Speed",
    "Wings of the Captain",
    "Anime 25th Collection",
    "The Best",

    # Decks
    "Starter Deck: 3D2Y",
    "Starter Deck: Absolute Justice",
    "Starter Deck: Animal Kingdom Pirates",
    "Starter Deck: Big Mom Pirates",
    "Starter Deck: Black Marshall.D.Teach",
    "Starter Deck: Blue Buggy",
    "Starter Deck: Charlotte Katakuri",
    "Starter Deck: Donquixote Doflamingo",
    "Starter Deck: Edward.Newgate",
    "Starter Deck: EX Ace & Newgate",
    "Starter Deck: EX Gear 5",
    "Starter Deck: Green Jewelry Bonney",
    "Starter Deck: Green Uta",
    "Starter Deck: Green Yellow Yamato",
    "Starter Deck: Monkey.D.Luffy",
    "Starter Deck: ONE PIECE FILM edition",
    "Starter Deck: Purple Black Monkey.D.Luffy",
    "Starter Deck: Purple Monkey.D.Luffy",
    "Starter Deck: Red Shanks",
    "Starter Deck: Smoker",
    "Starter Deck: Straw Hat Crew",
    "Starter Deck: The Seven Warlords of the Sea",
    "Starter Deck: Uta",
    "Starter Deck: Worst Generation",
    "Starter Deck: Yamato",
    "Starter Deck: Zoro & Sanji",
    "Ultra Deck: The Three Brothers",
    "Ultra Deck: The Three Captains",

    # Promos / special products / reprints
    "Judge Promos",
    "One Piece Products",
    "Premium Bandai Products",
    "Promos",
    "Reprints",
    "Special Tournament Promos",
    "Unnumbered Promos"
]


def onePiece():
    index = 1
    ws.write(0, 0, 'Set Code')
    ws.write(0, 1, 'Card Name')
    ws.write(0, 2, 'Price')
    wb.save('cardmarketOP.xls')
    setlist = OPTCGSETS
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

        print("wrote a set")
        print("Printing cards:")
        print(cards)
        if set == setlist[len(setlist)-1]:
            break
        ws.write(index, 1, set)
        index = index + 1
        index = scrapeCMGetPricesOfPage.main(cards, ws, wb, index) + 1
    print("All done")

def pokemon():
    index = 1
    ws.write(0, 0, 'Set Code')
    ws.write(0, 1, 'Card Name')
    ws.write(0, 2, 'Price')
    wb.save('cardmarketPTCG.xls')
    setlist = PTCGSETS
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

        print("wrote a set")
        print("Printing cards:")
        print(cards)

        ws.write(index, 1, set)
        index = index + 1
        index = scrapeCMGetPricesOfPage.main(cards, ws, wb, index) + 1
    print("All done")

if __name__=="__main__":
    onePiece()