import pandas as pd
import json
import re
import csv
from tqdm import tqdm


def clean_summary(text):
    text = re.sub("\'", "", text)
    text = re.sub("[^a-zA-Z]", " ", text)
    text = ' '.join(text.split())
    text = text.lower()
    return text


def main():
    data = []

    with open("booksummaries.txt", 'r',  encoding='utf-8') as f:
        reader = csv.reader(f, dialect='excel-tab')
        for row in tqdm(reader):
            data.append(row)

    book_index = []
    book_id = []
    book_author = []
    book_name = []
    summary = []
    genre = []
    a = 1
    for i in tqdm(data):
        book_index.append(a)
        a = a + 1
        book_id.append(i[0])
        book_name.append(i[2])
        book_author.append(i[3])
        genre.append(i[5])
        summary.append(i[6])

    df = pd.DataFrame({'Index': book_index, 'ID': book_id, 'BookTitle': book_name, 'Author': book_author,
                       'Genre': genre, 'Summary': summary})

    # Cleaning up Genres
    df.isna().sum()

    df = df.drop(df[df['Genre'] == ''].index)
    df = df.drop(df[df['Summary'] == ''].index)

    genres_cleaned = []
    for i in df['Genre']:
        genres_cleaned.append(list(json.loads(i).values()))
    df['Genres'] = genres_cleaned

    # Cleaning up summaries
    df['clean_summary'] = df['Summary'].apply(lambda x: clean_summary(x))

    # saving to json
    save_kb(df)


def save_kb(df):
    cols_to_include = ['ID', 'BookTitle', 'Author', 'Genres', 'clean_summary']
    df_subset = df[cols_to_include]

    # save the DataFrame subset as a JSON file
    df_subset.to_json('book_summaries.json', orient='records')


if __name__ == "__main__":
    main()
