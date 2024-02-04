import requests
from bs4 import BeautifulSoup

''' DONE
MAIN FUNCTION
Function to get all text from a website given a URL and return it as a string.

Params:
    url - the url of the website to get text from

Returns:
    A string of all text from the website
'''


def get_text_from_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract all text from the HTML
        text = soup.get_text(separator='\n', strip=True)

        return text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching content from {url}: {e}")
        return None


print(get_text_from_website("https://en.wikipedia.org/wiki/Introspection"))
