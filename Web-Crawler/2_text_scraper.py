"""
    Scrapes text off pages in relevant urls
    Stores each page's text in it own file
"""

import pathlib
from bs4 import BeautifulSoup
import urllib.request
import re
import os

successful_scrape_counter = 1


def is_visible(element):
    """
    Determines if an element is visible on the page
    :return: True if an element is visible on the page, False otherwise
    """
    if element.parent.name in ['script', 'style', '[document]', 'head', 'title']:
        return False
    elif re.match('<!--.*-->', str(element.encode('utf-8'))):
        return False
    elif element.name == 'code':
        return False
    return True


def get_text(url):
    global successful_scrape_counter
    try:
        html = urllib.request.urlopen(url)
    except Exception as e:
        print(f"Error occurred while opening URL: {url}", e)
        return

    soup = BeautifulSoup(html, features="html.parser")
    data = soup.findAll(string=True)
    result = filter(is_visible, data)
    tmp_lst = list(result)
    tmp_str = ' '.join(tmp_lst)

    if len(tmp_str) < 800:
        return

    with open(pathlib.Path.cwd().joinpath('data', 'text', f'text_{successful_scrape_counter}.txt'),
              'w', encoding='utf-8') as out:
        out.write(tmp_str)

    successful_scrape_counter = successful_scrape_counter + 1


def main():
    global successful_scrape_counter

    text_directory = pathlib.Path.cwd().joinpath('data', 'text')
    if not os.path.exists(text_directory):
        os.makedirs(text_directory)

    with open(pathlib.Path.cwd().joinpath('data', 'urls.txt'), 'r') as f:
        urls = f.read().splitlines()

    for url in urls:
        if successful_scrape_counter <= 15:
            get_text(url)
        else:
            break


if __name__ == "__main__":
    main()
