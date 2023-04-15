import en_core_web_sm
import string
import requests

API_URL = "http://localhost:3000"


def extract_name(text):
    nlp = en_core_web_sm.load()
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text.lower()
    return "no_name"


def get_user_profile(user_name):
    response = requests.get(API_URL + f"/users/get-profile?name={user_name}")
    return response.json()


def main():
    print("Assistant: Hello, what is your name?")
    user_response = input("User: ")

    user_name = extract_name(user_response)
    print(f"Assistant: Hello {string.capwords(user_name)}")

    user_profile = get_user_profile(user_name)
    print(user_profile)


if __name__ == "__main__":
    main()
