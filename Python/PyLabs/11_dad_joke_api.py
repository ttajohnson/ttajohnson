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

choice = input("What kind of jokes do you want to hear?")
page = 1

search_response = requests.get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"},
    params={"page": page, "term": choice},
)

search_data = search_response.json()
search_results = search_data["results"]

for joke in search_results:
    print(joke["joke"], "\n---\n")
    time.sleep(1)
