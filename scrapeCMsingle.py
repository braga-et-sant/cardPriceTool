from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Initialize the WebDriver (e.g., Chrome)


def main(urlbase):
    options = webdriver.ChromeOptions()
    options.headless = True  # Run without opening a browser window
    # Set a desktop-like viewport size to ensure price-container is visible
    options.add_argument("window-size=1280,720")
    options.add_argument('window-position=3500,0')
    driver = webdriver.Chrome(options=options)
    value = 0
    cardname = ""
    nameandcode = (0, "N/A)", 0)


    # Load the page
    url = urlbase + "?sellerType=1&language=1"
    driver.get(url)

    # Wait for the table-body to load
    table_body = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table-body"))
    )
    #print("Found table body")

    # Get the first div inside table-body
    first_div = table_body.find_elements(By.TAG_NAME, "div")[0]
    first_id = first_div.get_attribute("id")
    #print(f"First ID: {first_id}")

    # Wait for the price element within the articleRow div
    # Use a flexible XPath to target the price in either container

    cardname = driver.find_element(By.CLASS_NAME, "flex-grow-1")
    print(cardname.text)
    nameandcode = (cardname.text.splitlines()[0].split("(", 1))

    try:
        target_element = WebDriverWait(first_div, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, ".//div[contains(@class, 'price-container')]//span[contains(text(), '€')]")
            )
        )
        value = target_element.text
    except TimeoutException:
        print("Timed out waiting for an element to load. Possibly no professional seller / card in english found")
    except NoSuchElementException:
        print("Price element not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()
        return [nameandcode[0], "(" + nameandcode[1], value]

if __name__ == "__main__":
    print(main('https://www.cardmarket.com/en/OnePiece/Products/Singles/Anime-25th-Collection/Jewelry-Bonney-OP07-019'))