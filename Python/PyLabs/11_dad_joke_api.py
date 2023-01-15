# LAB 11: DAD JOKE API
# Use the Dad Joke API to get a dad joke and display it to the user.

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 1

# >>>
import requests

response = requests.get(
    "https://icanhazdadjoke.com/", headers={"Accept": "application/json"}
)
response_data = response.json()

# print(response_data["joke"])
# >>>

# -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

# VERSION 2

# >>>
import time

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


while True:
    user_term = input("What kind of jokes do you want to hear? Or 'Exit'").title()
    page = 1

    if user_term == "Exit":
        break

    else:

        search_response = requests.get(
            "https://icanhazdadjoke.com/search",
            headers={"Accept": "application/json"},
            params={"page": page, "term": user_term},
        )

        search_data = search_response.json()
        search_results = search_data["results"]

        if len(search_results) < 1:
            print(f"No {user_term} jokes found.")
            break

        else:

            print(f"{search_data['total_pages']} page(s) of {user_term} jokes found.")
            print(f"Current page: {search_data['current_page']}")

            for joke in search_results:
                print(joke["joke"], "\n---\n")
                time.sleep(1)

            next_page = input("Want to go to the next page?").title()
            if next_page == "Yes":
                page += 1
                continue
            else:
                continue
