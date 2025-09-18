from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\laterallyme\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Set up headless Chrome
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Load the page
    url = "https://www.ligaonepiece.com.br/?view=cards/card&card=Dracule%20Mihawk%20(OP12-030)"
    driver.get(url)

    # Step 2: Wait for the beginning-filters div to load
    beginning_filters = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "beginning-filters"))
    )
    print("Found beginning-filters div")

    # Step 3: Locate the filter div
    container = beginning_filters.find_element(By.XPATH, "..")
    filter_div = WebDriverWait(container, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "filter"))
    )
    print("Found filter div")

    # Step 4: Find the group-5 div inside the filter div
    group_5 = WebDriverWait(filter_div, 10).until(
        EC.presence_of_element_located((By.ID, "group-5"))
    )
    print("Found group-5 div")

    # Step 5: Find and check the field_5_1 checkbox
    checkbox = WebDriverWait(group_5, 10).until(
        EC.element_to_be_clickable((By.ID, "field_5_1"))
    )
    if not checkbox.is_selected():
        checkbox.click()
        print("Checked field_5_1 checkbox")
        time.sleep(2)  # wait for filter reload
    else:
        print("field_5_1 checkbox was already checked")

    # Step 6: Scrape the desired vendor price
    try:
        # Wait for the vendor list container to load
        marketplace_stores = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "marketplace-stores"))
        )
        print("Found marketplace-stores container")

        store_divs = marketplace_stores.find_elements(By.CLASS_NAME, "store")

        first_visible_store = None
        for store_div in store_divs:
            style = store_div.get_attribute("style")
            print(style)
            if style != "display: none;":
                print("style found style")
                first_visible_store = store_div
                break
        # Get the *first* vendor price element
        if first_visible_store:
            store_id = first_visible_store.get_attribute("id")
            print(f"First visible store ID: {store_id}")
        else:
            print("No visible store found.")

        pricedata = first_visible_store.find_element(By.CLASS_NAME, "price")

        # Take a screenshot of the price element
        png_data = pricedata.screenshot_as_png
        with open("vendor_price.png", "wb") as f:
            f.write(png_data)

        print("Saved first vendor price screenshot as vendor_price.png")

        # OCR the screenshot
        image = Image.open("vendor_price.png")
        price_text = pytesseract.image_to_string(image, config="--psm 7 digits")
        formatted = price_text[:-3] + "," + price_text[-3:]
        print(f"OCR detected vendor price: {formatted}")

    except Exception as e:
        print(f"Error while scraping vendor price: {e}")


except Exception as e:
    print("Error:", e)

finally:
    driver.quit()