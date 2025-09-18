from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Initialize the WebDriver (e.g., Chrome)
options = webdriver.ChromeOptions()
#options.headless = True  # Run without opening a browser window
# Set a desktop-like viewport size to ensure price-container is visible
#options.add_argument("window-size=1920,1080")
options.add_argument('window-position=3500,0')
options.add_argument("window-size=1280,720")
driver = webdriver.Chrome(options=options)
setlist = []
def main(cardgame):
    try:
        # Load the page
        url = "https://www.cardmarket.com/en/"+cardgame+"/Products/Singles"
        driver.get(url)

        # Wait for the table-body to load
        select_element = driver.find_element(By.NAME, 'idExpansion')
        select = Select(select_element)
        option_list = select.options

        for content in option_list[1:]:
            if not "(Non-English)" in content.text and not "(Japanese)" in content.text:
                setlist.append(content.text)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        #print(setlist)
        driver.quit()
        return setlist

if __name__ == "__main__":
    main("OnePiece")