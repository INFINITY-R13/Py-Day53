# Py-Day53

# Zillow Scraper & Google Form Auto-Filler

This Python script automates the process of finding rental property data and populating it into a Google Form. It first scrapes a Zillow clone website to gather property addresses, prices, and listing links. Then, it uses Selenium to launch a web browser and automatically fill in a Google Form with the collected data for each listing.

## Features ✨

  * **Web Scraping**: Uses `Requests` and `BeautifulSoup` to parse HTML and extract relevant property data.
  * **Data Cleaning**: Cleans the scraped text to get formatted addresses and prices.
  * **Browser Automation**: Leverages `Selenium` to automatically navigate to a Google Form, input the data, and submit it.
  * **Robust Automation**: Implements `WebDriverWait` instead of fixed pauses, making the script more reliable and efficient.

-----

## Tech Stack & Requirements 💻

  * Python 3.x
  * [Beautiful Soup 4](https://pypi.org/project/beautifulsoup4/) (`beautifulsoup4`)
  * [Requests](https://www.google.com/search?q=https://pypi.org/project/Requests/) (`requests`)
  * [Selenium](https://pypi.org/project/selenium/) (`selenium`)
  * A web browser (e.g., Google Chrome)
  * The corresponding WebDriver (e.g., [ChromeDriver](https://chromedriver.chromium.org/downloads))

-----

## Setup & Installation 🚀

Follow these steps to get the project running on your local machine.

### 1\. Download the Script

Clone this repository or simply download the `main.py` file.

### 2\. Install Dependencies

You'll need to install the required Python packages. Open your terminal or command prompt and run the following command:

```bash
pip install beautifulsoup4 requests selenium
```

### 3\. Install WebDriver

Download the WebDriver that corresponds to your web browser and its version. For example, if you use Google Chrome, download ChromeDriver.

**Important:** Make sure the downloaded WebDriver executable is either placed in the same directory as the `main.py` script or is added to your system's PATH.

-----

## How to Use 📋

### Step 1: Create a Google Form

First, create a Google Form that will receive the data. The form should have **three "Short answer" questions** for:

1.  Property Address
2.  Property Price
3.  Property Link

### Step 2: Get Your Form's Link

Click the "Send" button on your Google Form, go to the "link" tab, and copy the shareable URL.

### Step 3: Update the Script with Your Link

Open the `main.py` file and find the following line:

```python
YOUR_GOOGLE_FORM_LINK = "YOUR_GOOGLE_FORM_LINK_HERE"
```

Replace `"YOUR_GOOGLE_FORM_LINK_HERE"` with the link you copied in the previous step.

### Step 4: Update the XPaths (If Necessary)

The script uses XPaths to find the input fields on the Google Form. These can sometimes change. If the script fails to find an element, you may need to update them.

1.  Open your Google Form in Chrome.
2.  Right-click on an input field (e.g., the address field) and select **"Inspect"**.
3.  In the developer console, right-click on the highlighted HTML element.
4.  Go to **Copy \> Copy XPath**.
5.  Paste the new XPath into the corresponding `find_element` line in the script.

### Step 5: Run the Script

You're all set\! Open your terminal, navigate to the project directory, and run the script:

```bash
python main.py
```

The script will open a Chrome window, visit the Zillow clone site, scrape the data, and then fill out and submit your Google Form for each property listing.
