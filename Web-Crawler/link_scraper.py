# from bs4 import BeautifulSoup
import requests
import pathlib
from bs4 import BeautifulSoup
from collections import deque


def clean_url(url):
    """
    Returns a clean version of the URL, or None if the URL is not interesting
    A clean and interesting URL is one that can be used to put back in the queue to continue scraping

    :param: (str) url to be cleaned
    :return: (str) clean version of url | None if url is not interesting
    """

    if not url:
        return None

    # Clean up the URL
    if url.startswith("/url?q="):
        url = url[7:]
    if "?" in url:
        i = url.find("?")
        url = url[:i]

    # Make sure that the URL is valid
    unacceptable_extensions = [".pdf", ".png", ".jpeg"]
    unacceptable_keywords = ["wikipedia", "wikidata", "wikimedia", "youtube", "google"]

    if url.startswith("http") \
            and not any(url.endswith(ext) for ext in unacceptable_extensions) \
            and not any(keyword in url for keyword in unacceptable_keywords):
        return url

    return None


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

    # Initialize a deque to store the URLs to be visited
    url_queue = deque([start_url])

    selected_links = []

    while url_queue and len(selected_links) < max_links:
        # pop the URL from the left end of the queue
        current_url = url_queue.popleft()

        # Make a request to the current URL and parse the HTML response
        response = requests.get(current_url)
        soup = BeautifulSoup(response.text, features="html.parser")

        # Loop through links in the current URL
        for link_element in soup.find_all('a'):
            if len(selected_links) >= max_links:
                break
            new_url = link_element.get('href')
            new_url = clean_url(new_url)
            if new_url:
                url_queue.append(new_url)
                selected_links.append(new_url)

    return selected_links


def main():
    # Scrape for links
    links = scrape_links("https://en.wikipedia.org/wiki/Vince_Gilligan")

    # Write the selected links to a text file
    with open(pathlib.Path.cwd().joinpath('data', 'urls.txt'), 'w') as f:
        for link in links:
            f.write(link + "\n")


if __name__ == "__main__":
    main()
