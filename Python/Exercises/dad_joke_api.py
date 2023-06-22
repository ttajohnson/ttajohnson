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
        search_term = input("What genre of joke do you want to hear?: ")
        page = 1
        while True:
            headers = {"Accept": "application/json"}
            params = {"page":page, "term":search_term}
            response = requests.get("https://icanhazdadjoke.com/search", headers=headers, params=params)
            json_data = response.json()
            if json_data['results'] == []:
                print(f"I don't have any {search_term} jokes...")
                break
            else:
                # print(json_data)
                print(f"\nI found {json_data['total_jokes']} {search_term} jokes.")
                print(f"Page: {json_data['current_page']} of {json_data['total_pages']}\n")
                for index, joke in enumerate(json_data['results'], start=1):
                    print(f"{index}. {joke['joke']}")
            if json_data['total_pages'] > 1:
                next_page = input(f"\nNext page of {search_term} jokes? Y/N: ").upper()
                if next_page == "Y":
                    page += 1
                    continue
                else:
                    break
            else:
                break

if __name__ == "__main__":
    main()