import en_core_web_sm
import string
import requests

API_URL = "http://localhost:3000"
nlp = en_core_web_sm.load()


def extract_name(text):
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text.lower()
    return "no_name"


def get_user_profile(user_name):
    response = requests.get(API_URL + f"/users/get-profile?name={user_name}")
    return response.json()


def update_preferences(user_name, user_profile):
    print(f"Assistant: What are some books, authors, or genres you like?")
    new_user_likes = input("User: ")

    print(f"Assistant: What are some books, authors, or genres you dislike?")
    new_user_dislikes = input("User: ")

    user_profile["likes"] += " " + new_user_likes
    user_profile["dislikes"] += " " + new_user_dislikes

    data = {
        "name": user_name,
        "likes": user_profile["likes"],
        "dislikes": user_profile["dislikes"]
    }

    requests.post(API_URL + "/users/set-profile", data=data)


def fetch_nearest_books(user_profile, search):
    data = {
        "search": search,
        "likes": user_profile["likes"],
        "dislikes": user_profile["dislikes"]
    }

    response = requests.post(API_URL + "/vector-db/query-book", data=data)
    return response.json()['nearestBooks']


def main():
    print("Assistant: Hello, what is your name?")
    user_response = input("User: ")

    user_name = extract_name(user_response)
    print(f"Assistant: Hello {string.capwords(user_name)}")

    user_profile = get_user_profile(user_name)

    update_preferences(user_name, user_profile)

    print(f"Assistant: What kind of book are you interested in reading today?")
    user_search = input("User: ")

    nearest_books = fetch_nearest_books(user_profile, user_search)
    print("Assistant: Here are some book recommendations:\n")
    for i in range(0, len(nearest_books)):
        current_book = nearest_books[i]
        print(i + 1, ":", current_book['title'], current_book["link"])


if __name__ == "__main__":
    main()
