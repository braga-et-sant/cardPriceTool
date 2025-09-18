from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Set up headless Chrome
options = Options()
options.headless = True  # Run without opening a browser window
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Load the page
    url = "https://www.ligaonepiece.com.br/?view=cards/card&card=Dracule%20Mihawk%20(OP12-030)"
    driver.get(url)

    # Step 2: Wait for the beginning-filters div to load
    try:
        beginning_filters = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "beginning-filters"))
        )
        print("Found beginning-filters div")
    except Exception as e:
        print("Could not find beginning-filters div.")
        print(f"Error: {e}")
        driver.quit()
        exit()

    # Step 3: Find the parent container to locate the filter div
    container = beginning_filters.find_element(By.XPATH, "..")
    try:
        filter_div = WebDriverWait(container, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "filter"))
        )
        print("Found filter div")
    except Exception as e:
        print("Could not find filter div.")
        print(f"Error: {e}")
        driver.quit()
        exit()

    # Step 4: Find the group-5 div inside the filter div
    try:
        group_5 = WebDriverWait(filter_div, 10).until(
            EC.presence_of_element_located((By.ID, "group-5"))
        )
        print("Found group-5 div")
    except Exception as e:
        print("Could not find group-5 div.")
        print(f"Error: {e}")
        driver.quit()
        exit()

    # Step 5: Find and check the field_5_1 checkbox
    try:
        checkbox = WebDriverWait(group_5, 10).until(
            EC.element_to_be_clickable((By.ID, "field_5_1"))
        )
        if not checkbox.is_selected():
            checkbox.click()
            print("Checked field_5_1 checkbox")
            # Wait for the JavaScript function (screenfilter.search) to complete
            time.sleep(2)  # Adjust based on observed update time
        else:
            print("field_5_1 checkbox was already checked")
    except Exception as e:
        print("Could not find or interact with field_5_1 checkbox.")
        print(f"Error details: {e}")
        # Print the full HTML of group-5 and its inputs for debugging
        print("HTML of group-5 div:", group_5.get_attribute("outerHTML"))
        inputs = group_5.find_elements(By.TAG_NAME, "input")
        print(f"Found {len(inputs)} input elements in group-5:")
        for i, input_elem in enumerate(inputs):
            attrs = input_elem.get_attribute("outerHTML")
            print(f"Input {i}: {attrs}")
        driver.quit()
        exit()

    # Step 6: Scrape the desired data
    try:
        # Wait for the price container to load
        price_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "container-price-mkp-card"))
        )
        print("Found price container")
        # Find all price elements within the container
        price_elements = price_container.find_elements(By.CLASS_NAME, "price-mkp")
        print(f"Found {len(price_elements)} price elements in group-5:")
        if price_elements:
            print("Found price elements")
            # Extract prices for Normal and Foil
            prices = {}
            for i, price_elem in enumerate(price_elements):
                price_text = price_elem.text.strip().replace('R$', '').replace('.', '').replace(',', '.')
                if i == 0:  # First price is for Normal
                    prices["Normal"] = price_text
                elif i == 1:  # Second price is for Foil
                    prices["Foil"] = price_text

            print(f"Price for Normal: R${prices['Normal']}")
            print(f"Price for Foil: R${prices['Foil']}")
        else:
            print("No price elements found.")

    except Exception as e:
        print(f"Error while scraping data: {e}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()