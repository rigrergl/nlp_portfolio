## How to run Locally

The files must be run in the following order
1. [1_link_scraper.py](1_link_scraper.py)
2. [2_text_scraper.py](2_text_scraper.py)
3. [3_clean_text.py](3_clean_text.py)
4. [4_extract_important_terms.py](4_extract_important_terms.py)
5. [5_create_knowledge_base.py](5_create_knowledge_base.py)

**IMPORTANT NOTE**: between steps 4 and 5, you must look at the output of step 4 and manually select the top 10 terms from the outputted top 40 terms and save them to [this](data/manually_determined_top_10_terms.txt) text file.

Alternatively, you can leave the file unchanged, it already contains the top 10 terms that I picked when I ran it.

## Requirements
1. 'requests' module installed (`pip install requests`)
2. 'beautifulsoup4' module installed (`pip install beautifulsoup4`)

## Notes
- Saved 40 urls because often some urls fail (requires login or resource is protected). This ensures that I get at least 15 urls that work
- Since I am extracting from website that sometimes contain japanese text, I am filtering the top terms to only contain English alphabet characters
- I am only extracting material inside <p> tags for better results