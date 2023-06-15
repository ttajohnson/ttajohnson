""" Python Exercise - Dad Joke API

    Instructions: Utilize the requests library and the Dad-Joke API to get a random Dad-Joke and display it to the user.
        1. Utilize the 'accept' header as 'application/json' to return the data in JSON format, use this to display.
        2. Create a REPL that adds the ability to search for jokes via a search term.
        3. Add support for multiple pages.
"""

import requests
"""
Initial Request for testing of Random Dad Joke Fetch.

headers = {"Accept": "application/json"}
response = requests.get("https://icanhazdadjoke.com/", headers=headers)
print(response.json())
"""

def main():
    
    # Initiation of REPL
    while True:
        print("Welcome to the Dad Joke API!")
        search_term = input("What genre of joke do you want to hear?\n")

        headers = {"Accept": "application/json"}

        response = requests.get("https://icanhazdadjoke.com/search", headers=headers)
        json_data = response.json()

        print(json_data)
        
        

        break

    return

if __name__ == "__main__":
    main()