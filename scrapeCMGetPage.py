from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import traceback
# Initialize the WebDriver (e.g., Chrome)

#options.headless = True  # Run without opening a browser window
# Set a desktop-like viewport size to ensure price-container is visible
#options.add_argument("window-size=1920,1080")



def getItemAmount(url):
    options = webdriver.ChromeOptions()
    options.add_argument('window-position=3500,0')
    options.add_argument("window-size=1280,720")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    itemamount = (driver.find_element(By.CLASS_NAME, 'col-auto.d-none.d-md-block')).text.split(" ")[0]
    print(itemamount)
    return int(itemamount)

def main(url):
    items = set()
    options = webdriver.ChromeOptions()
    options.add_argument('window-position=3500,0')
    options.add_argument("window-size=1280,720")
    driver = webdriver.Chrome(options=options)
    try:
        # Load the page
        #url = "https://www.cardmarket.com/en/OnePiece/Products/Singles/500-Years-into-the-Future?idRarity=0&sortBy=collectorsnumber_asc"
        driver.get(url)


        itemlist = driver.find_element(By.CLASS_NAME, "table.table-striped.mb-3")
        itemlistsub = itemlist.find_element(By.CLASS_NAME, "table-body")
        itemlistvalues = itemlistsub.find_elements(By.CLASS_NAME, "row.g-0")

        for content in itemlistvalues:
            price = 0
            try:
                price_element = WebDriverWait(content, 0.1).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.col-price.pe-sm-2"))
                )
                price_text = price_element.text.strip()  # "0,02 €"

                if (price_text != "N/A"):

                    price = float(
                        price_text.replace("€", "").replace(".00", "").replace(",", ".").strip()
                    )
                    #print(price)
            except TimeoutException:
                pass
            if(not price <= 0.02):
                inner = content.find_element(By.CLASS_NAME, "col-10.col-md-8.px-2.flex-column.align-items-start.justify-content-center")
                href = inner.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                items.add(href)
        #print(items)

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

    finally:
        print(items)
        driver.quit()
        return items


if __name__ == "__main__":
    #main("https://www.cardmarket.com/en/OnePiece/Products/Singles/500-Years-into-the-Future?idRarity=0&sortBy=collectorsnumber_asc")
    pass