from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

import scrapeCMGetPage

# Initialize the WebDriver (e.g., Chrome)
options = webdriver.ChromeOptions()
#options.headless = True  # Run without opening a browser window
# Set a desktop-like viewport size to ensure price-container is visible
#options.add_argument("window-size=1920,1080")
options.add_argument('window-position=3500,0')
options.add_argument("window-size=1280,720")
driver = webdriver.Chrome(options=options)



def main(set):
    listofsets = []
    finalist = []
    try:
        # Load the page
        treatset = set.replace("& ", "").replace(" ", "-").replace(":", "").replace("& ", "")
        driver.get("https://www.google.com/search?q=" + treatset)
        url = "https://www.cardmarket.com/en/OnePiece/Products/Singles/" + treatset + "?idRarity=0&perSite=20&site="
        itemamount = scrapeCMGetPage.getItemAmount(url)


        # Wait for the table-body to load
        for i in range(1, int(itemamount / 20) + 2):
            #print(i)
            urltreated = url + str(i)
            print("Treated URL:")
            print(urltreated)
            listofsets.append(scrapeCMGetPage.main(urltreated))




    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        for i in listofsets:
            finalist += list(i)
        #print(finalist)
        driver.quit()
        return finalist

if __name__ == "__main__":
    print(main("Anime-25th-Collection"))