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
    while True:
        user_term = input("Search jokes by term: ")
        page = 1

        jokes = get_jokes(user_term, page)

        if len(jokes[0]) < 1:
            print(f"No {user_term} jokes found...")
            pass
        else:
            print(f"{jokes[1]} page(s) of {user_term} jokes found.")

            for joke in jokes[0]:
                print("\n", joke["joke"], "\n")
                time.sleep(0.5)


main()
