# from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup
from collections import deque

def is_good_url(url):
    return True # TODO

def scrape_links(start_url, max_links=15):
    """
    Scrape links from web pages starting from a given seed URL.

    Parameters:
        start_url (str): The starting URL to scrape links from.
        max_links (int): The maximum number of links to scrape. Defaults to 10.

    Returns:
        A list of unique links scraped from web pages starting from the
        given seed URL.
    """

    # Start with a list of seed URLs
    seed_urls = ["https://en.wikipedia.org/wiki/Vince_Gilligan"]

    # Initialize a deque to store the URLs to be visited
    url_queue = deque(seed_urls)

    selected_links = []

    while url_queue and len(selected_links) < 15:
        # pop the URL from the left end of the queue
        current_url = url_queue.popleft()

        # Make a request to the current URL and parse the HTML response
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, features="html.parser")

        # Loop through links in the current URL
        for link_element in soup.find_all('a'):
            new_url = link_element.get('href')
            if is_good_url(new_url):
                selected_links.append(new_url)

    return selected_links


def main():
    links = scrape_links("https://en.wikipedia.org/wiki/Vince_Gilligan")
    print(links)


if __name__ == "__main__":
    main()

