# import library
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def url_to_page_source(category: str, url: str) -> str:
    """
    This function uses Selenium to navigate to a given URL, wait for the page to load,
    and extract specific data based on the provided category.

    Parameters:
    category (str): The category of data to extract. It should be either 'artist' or 'team'.
    url (str): The URL of the webpage to navigate to.

    Returns:
    str: The extracted data as a string.

    Raises:
    KeyError: If the provided category is not 'artist' or 'team'.
    """

    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()

    # Maximize the window
    driver.maximize_window()

    # Navigate to the specified URL
    driver.get(url=url)

    # Wait for 3 seconds to allow the page to load
    time.sleep(3)

    # Set an implicit wait of 10 seconds for elements to be available
    driver.implicitly_wait(10)

    # Define a dictionary to map categories to XPath selectors
    crawling_choice = {
        'artist': os.getenv('ARTIST_XPATH'),
        'team': os.getenv('TEAM_XPATH')
    }

    # Get the XPath selector based on the provided category
    xpath = crawling_choice[category]

    # Find the element using the XPath selector
    element = driver.find_element(By.XPATH, xpath)

    # Extract the text from the element
    raw_data = element.text

    # Return the extracted data
    return raw_data