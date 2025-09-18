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
    cardinfo = []

    try:
        # Step 1: Load the page
        driver.get(url)

        # Step 2: get switchview
        try:
            switchview = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "tb-view-02"))
            )
            #print("Found switchview ")
        except Exception as e:
            print("Could not find switchview.")
            print(f"Error: {e}")
            driver.quit()
            exit()
        switchview.click()
        #print("View Switched")
        #sleep(10)
        #table_element = driver.find_element("css selector", ".card-table.table-tcgs")
        #print(table_element.text)
        # Step 3: Find the parent container
        try:
            fulltable = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "card-estoque"))
            )
            #print("Found fulltable")
        except Exception as e:
            print("Could not find fulltable.")
            print(f"Error: {e}")
            driver.quit()
            exit()

        #sleep(10)

        # Step 4: Find the group-5 div inside the filter div
        try:
            cardgrid = WebDriverWait(fulltable, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "grid-cardsinput"))
            )
            #print("Found card table tcgs div")
        except Exception as e:
            print("Could card table tcgs div.")
            print(f"Error: {e}")
            driver.quit()
            exit()

        try:
            cardlist = WebDriverWait(cardgrid, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "card-table.table-tcgs"))
            )
            #print("Found card list div")
        except Exception as e:
            print("Could not find card list div.")
            print(f"Error: {e}")
            driver.quit()
            exit()
        #print(cardlist.text)

        #Now to treat the output

        cardlistsplit = cardlist.text.splitlines()
        for i in cardlistsplit[1:]:
            tokens = i.split(" ")

            namecounter = 0
            for i in tokens:
                if i.__contains__("("):
                    break;
                else:
                    namecounter+=1
            templist = []
            templist.append(tokens[0])
            templist.append(' '.join(tokens[1:namecounter]))
            templist.append(tokens[len(tokens) - 3])
            cardinfo.append(templist)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()
    return cardinfo