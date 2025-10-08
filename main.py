# This script automates the process of finding rental property listings and
# recording them in a Google Form. It is divided into two main parts:
# Part 1: Scrapes a Zillow-clone website for property links, addresses, and prices.
# Part 2: Uses Selenium to automatically fill out and submit a Google Form with the scraped data.

# Tested with the following package versions:
# beautifulsoup4==4.12.2
# Requests==2.31.0
# selenium==4.15.1


# --- Import necessary libraries ---
from bs4 import BeautifulSoup  # For parsing HTML and XML documents.
import requests                # For making HTTP requests to get the webpage content.
from selenium import webdriver # The main library for browser automation.
from selenium.webdriver.common.by import By # To specify how to locate elements (e.g., by XPATH, ID, etc.).
from selenium.webdriver.support.ui import WebDriverWait # For waiting for elements to appear before interacting with them.
from selenium.webdriver.support import expected_conditions as EC # A set of predefined conditions to use with WebDriverWait.
import time                    # Used for pausing the script (though replaced with a better method).

# ================= PART 1: SCRAPE RENTAL PROPERTY DATA =================

# --- Define headers to mimic a real browser visit ---
# Some websites block requests from scripts. A User-Agent header helps to avoid this.
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# --- Fetch the website content ---
# The URL points to a static Zillow clone page, which is good for testing scraping scripts.
ZILLOW_CLONE_URL = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(ZILLOW_CLONE_URL, headers=header)
response.raise_for_status()  # This will raise an error if the request failed.
data = response.text

# --- Create a BeautifulSoup object to parse the HTML ---
soup = BeautifulSoup(data, "html.parser")

# --- Extract property links using a CSS Selector ---
# The selector targets all <a> (anchor/link) tags within elements with the class 'StyledPropertyCardDataWrapper'.
# A list comprehension is used to efficiently extract the 'href' attribute from each found link.
all_links = [link["href"] for link in soup.select(".StyledPropertyCardDataWrapper a")]
print(f"There are {len(all_links)} links to individual listings in total: \n")
print(all_links)

# --- Extract property addresses using a CSS Selector ---
# The selector targets all <address> tags.
# The text from each tag is cleaned by removing the "|" separator and any leading/trailing whitespace.
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in soup.select(".StyledPropertyCardDataWrapper address")]
print(f"\nAfter having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")
print(all_addresses)

# --- Extract property prices using a CSS Selector ---
# FIX: The selector is now more specific, targeting <span> tags inside '.StyledPropertyCardDataWrapper'.
# The list comprehension filters for spans containing a '$' symbol, then cleans the text
# by removing "/mo" and any extra text after a "+", which is common for "starting at" prices.
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in soup.select(".StyledPropertyCardDataWrapper span") if "$" in price.text]
print(f"\nAfter having been cleaned up, the {len(all_prices)} prices now look like this: \n")
print(all_prices)


# ================= PART 2: AUTOMATE GOOGLE FORM ENTRY =================

# --- Configure Selenium WebDriver ---
# Keep the Chrome browser open after the script finishes. This is useful for debugging.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

# --- Loop through each scraped listing and fill the form ---
for n in range(len(all_links)):
    # CRITICAL: You must replace the placeholder link below with the link to your own Google Form.
    # To get the link, create a Google Form and click the "Send" button, then get the shareable link.
    YOUR_GOOGLE_FORM_LINK = "YOUR_GOOGLE_FORM_LINK_HERE"
    driver.get(YOUR_GOOGLE_FORM_LINK)

    # FIX: Replaced time.sleep() with WebDriverWait for robustness.
    # This creates a wait object that will wait a maximum of 10 seconds for an element to become available.
    wait = WebDriverWait(driver, 10)

    # NOTE: The XPaths below are very specific to the structure of the form they were created for.
    # If your form is different, or if Google updates its form structure, these will likely break.
    # To get a new XPath:
    # 1. Open your form in Chrome.
    # 2. Right-click the input field -> "Inspect".
    # 3. In the developer console, right-click the highlighted HTML -> Copy -> Copy XPath.

    # Find the "Address" input field, wait for it to be present, and then type in the address.
    address_field = wait.until(EC.presence_of_element_located((By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    address_field.send_keys(all_addresses[n])

    # Find the "Price" input field, wait for it to be present, and then type in the price.
    price_field = wait.until(EC.presence_of_element_located((By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_field.send_keys(all_prices[n])

    # Find the "Link" input field, wait for it to be present, and then type in the link.
    link_field = wait.until(EC.presence_of_element_located((By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link_field.send_keys(all_links[n])

    # Find the "Submit" button, wait for it to be clickable, and then click it.
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')))
    submit_button.click()

    print(f"Form submission {n+1}/{len(all_links)} complete.")
    # A small pause to allow the next form to load properly after submission.
    time.sleep(1)

# The browser will remain open due to the 'detach' option. You can close it manually.
print("All listings have been submitted.")