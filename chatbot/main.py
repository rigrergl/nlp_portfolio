import en_core_web_sm
import string


def extract_name(text):
    nlp = en_core_web_sm.load()
    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return string.capwords(ent.text)
    return "no_name"


def main():
    print("Assistant: Hello, what is your name?")
    user_response = input("User: ")

    user_name = extract_name(user_response)
    print(f"Assistant: Hello {user_name}")


if __name__ == "__main__":
    main()