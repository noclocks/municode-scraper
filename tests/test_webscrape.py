import requests
from bs4 import BeautifulSoup

def scrape_municode(url):
    """
    Function to scrape content from a Municode website.

    Parameters:
    - url: str
        The URL of the Municode website to scrape.

    Returns:
    - str:
        The scraped content from the Municode website.

    Raises:
    - requests.exceptions.RequestException:
        If there is an error while making the HTTP request to the Municode website.
    - ValueError:
        If the provided URL is invalid or empty.
    """

    # Checking if the URL is empty or None
    if not url:
        raise ValueError("URL cannot be empty or None.")

    try:
        # Making an HTTP GET request to the Municode website
        response = requests.get(url)

        # Checking if the request was successful
        response.raise_for_status()

        # Parsing the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting the desired content from the HTML
        scraped_content = soup.get_text()

        return scraped_content

    except requests.exceptions.RequestException as e:
        raise requests.exceptions.RequestException(f"Error while making request to {url}: {e}")

# Example usage of the scrape_municode function:

# URL of the Municode website to scrape
municode_url = "https://library.municode.com/GA"

try:
    # Scraping content from the Municode website
    scraped_content = scrape_municode(municode_url)
    print(scraped_content)
except ValueError as e:
    print(f"Error: {e}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
