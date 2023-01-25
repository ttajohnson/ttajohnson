# LAB 11: DAD JOKE API
# Use the Dad Joke API to get a dad joke and display it to the user.

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 1

# >>>
# import requests

# response = requests.get(
#     "https://icanhazdadjoke.com/", headers={"Accept": "application/json"}
# )
# response_data = response.json()

# print(response_data["joke"])
# >>>

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 2

# >>>
# import time

# choice = input("What kind of jokes do you want to hear?")
# page = 1

# search_response = requests.get(
#     "https://icanhazdadjoke.com/search",
#     headers={"Accept": "application/json"},
#     params={"page": page, "term": choice},
# )

# search_data = search_response.json()
# search_results = search_data["results"]

# for joke in search_results:
#     print(joke["joke"], "\n---\n")
#     time.sleep(1)
# >>>

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 3

# >>>
import requests
import time


def random_joke():
    response = requests.get(
        "https://icanhazdadjoke.com/", headers={"Accept": "application/json"}
    )
    response_data = response.json()

    print(response_data["joke"])


def get_jokes(term, page):
    response = requests.get(
        "https://icanhazdadjoke.com/search",
        headers={"Accept": "application/json"},
        params={"page": page, "term": term},
    )
    data = response.json()
    results = data["results"]
    total_pages = data["total_pages"]
    return results, total_pages


def main():
    print("Welcome to the Joke Zone!")

    while True:

        user_choice = input(
            "\n1. Random Joke\n2. Jokes by Term\n3. Exit the Joke Zone\n"
        )

        if user_choice == "1":
            random_joke()
        elif user_choice == "2":
            term = input("Joke Term: ")
            page = 1
            while True:
                jokes = get_jokes(term, page)
                print(f"{jokes[1]} pages of {term} jokes found!\nPage {page}:\n")

                for joke in jokes[0]:
                    print(joke["joke"])
                    time.sleep(1)
                next_or_back = input(f"\n1. Next Page of {term} jokes.\n2. Fresh Jokes")
                if next_or_back == "1":
                    page += 1
                    pass
                elif next_or_back == "2":
                    break
                else:
                    print("Invalid input!")
                    continue
        elif user_choice == "3":
            break
        else:
            print("Invalid option!")
            pass


main()
