from bs4 import BeautifulSoup
import urllib.request
import json


def get_text(url):
    try:
        html = urllib.request.urlopen(url)
    except Exception as e:
        print(f"Error occurred while opening URL: {url}", e)
        return

    soup = BeautifulSoup(html, features="html.parser")

    # Find the header tag with the text "Short Summary"
    short_summary_header = soup.find('h2', string='Short Summary')

    # Find the paragraph tag that comes right after the header tag
    short_summary_paragraph = short_summary_header.find_next_sibling('p')

    # Extract the text of the paragraph
    short_summary_text = short_summary_paragraph.get_text()

    # Find the header tag with the text "Long Summary"
    long_summary_header = soup.find('h2', string='Long Summary')

    # Find the paragraph tag that comes right after the header tag
    long_summary_paragraph = long_summary_header.find_next_sibling('p')

    # Extract the text of the paragraph
    long_summary_text = long_summary_paragraph.get_text()

    return short_summary_text, long_summary_text


def main():
    data_list = []

    for i in range(1, 1081):
        short_summary, long_summary = get_text(f"https://onepiece.fandom.com/wiki/Chapter_{i}")
        entry = {'id': i, 'short_summary': short_summary, 'long_summary': long_summary}
        data_list.append(entry)

    with open('kb.json', 'w') as f:
        json.dump(data_list, f)


if __name__ == "__main__":
    main()
