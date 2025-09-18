from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main(url):
    # Set up headless Chrome
    options = Options()
    options.headless = True  # Run without opening a browser window
    driver = webdriver.Chrome(options=options)
    linklist = []

    try:
        # Step 1: Load the page
        driver.get(url)

        # Step 2: get switchview
        try:
            edictable = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "container-timeline"))
            )
            #print("Found edictable ")
        except Exception as e:
            print("Could not find edictable.")
            print(f"Error: {e}")
            driver.quit()
            exit()

        for contenttables in edictable.find_elements(By.CLASS_NAME, "edition-content"):
            setlist = WebDriverWait(contenttables, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "editions"))
            )
            for content in setlist.find_elements(By.CLASS_NAME, "edition"):
                link = content.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                linklist.append(link)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()
    return linklist