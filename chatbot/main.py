import string
import requests

API_URL = "http://localhost:3000"


def extract_name(text):
    data = {
        "userInput": text
    }
    response = requests.post(API_URL + "/openai/extract-name", data=data)

    return response.json()["name"]


def get_user_profile(user_name):
    response = requests.get(API_URL + f"/users/get-profile?name={user_name}")
    return response.json()


def clean_preferences(raw_user_input):
    data = {
        "userInput": raw_user_input
    }
    response = requests.post(API_URL + f"/openai/extract-preference-list", data=data)

    return response.json()["preferences"]


def clean_search(raw_user_input):
    data = {
        "userInput": raw_user_input
    }
    response = requests.post(API_URL + f"/openai/clean-search", data=data)

    return response.json()["cleanSearch"]


def update_preferences(user_name, user_profile):
    print(f"Assistant: What are some books, authors, or genres you like?")
    new_user_likes = input("User: ")
    new_user_likes = clean_preferences(new_user_likes)

    print(f"Assistant: What are some books, authors, or genres you dislike?")
    new_user_dislikes = input("User: ")
    new_user_dislikes = clean_preferences(new_user_dislikes)

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


def make_recommendation(user_profile):
    print(f"Assistant: What kind of book are you interested in reading today?")
    user_search = input("User: ")
    user_search = clean_search(user_search)

    nearest_books = fetch_nearest_books(user_profile, user_search)
    print("Assistant: Here are some book recommendations:")
    for i in range(0, len(nearest_books)):
        current_book = nearest_books[i]
        print(i + 1, ":", current_book['title'], "by", current_book["author"], current_book["link"])


def parse_user_yes_no_response(raw_user_input):
    """Returns True if user response evaluates to yes"""
    data = {
        "userInput": raw_user_input
    }
    response = requests.post(API_URL + f"/openai/get-yes-no", data=data)

    return response.json()["isYes"]


def main():
    print("Assistant: Hello, what is your name?")
    user_response = input("User: ")

    user_name = extract_name(user_response)
    print(f"Assistant: Hello {string.capwords(user_name)}")

    user_profile = get_user_profile(user_name)

    if user_profile["likes"] != "" and user_profile["dislikes"] != "":
        likes = user_profile["likes"]
        dislikes = user_profile["dislikes"]
        print(f"\tAccording to my records, you like {likes}.\n\tAs far as I know, you dislike {dislikes}.")
        print("\t Would you like to add any preferences?")
        user_response = input("User: ")
        should_add_preferences = parse_user_yes_no_response(user_response)

        if should_add_preferences:
            update_preferences(user_name, user_profile)
    else:
        update_preferences(user_name, user_profile)

    make_recommendation(user_profile)


if __name__ == "__main__":
    main()
