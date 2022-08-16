# ....Lab 14 Version 1 ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

import requests
import pprint
import time

def random_dad_joke(): # Displays one random dad joke.
    response = requests.get("https://icanhazdadjoke.com", headers={'Accept':'application/json'})
    response_dict = response.json()
    joke = response_dict['joke']
    print("Here's a random Dad Joke")
    time.sleep(3)
    print(joke)

# random_dad_joke()

def rolling_term_jokes(): # Asks user for a keyword to filter jokes, and rolls through each with 5sec gaps.
    search_term = input('Enter a keyword and I will tell you some Dad Jokes: ')
    response = requests.get('https://icanhazdadjoke.com/search', headers ={'Accept':'application/json'}, params={'term':search_term})
    response_dict = response.json()
    jokes = response_dict['results']
    for joke in jokes:
        print(joke['joke'])
        time.sleep(5)
    print(f'End of {search_term} jokes.')

# rolling_term_jokes()

# ....Lab 14 Version 2 ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-


def main():
    
    print('Welcome to the Dad Joke Simulator!')

    time.sleep(3)

    while True:
        search_term = input('Enter a keyword and I will tell you some Dad Jokes: ')
        response = requests.get('https://icanhazdadjoke.com/search', headers ={'Accept':'application/json'}, params={'term':search_term})
        response_dict = response.json()
        jokes = response_dict['results']
        pages = response_dict['total_pages']
        if jokes == []: # Case for search term returning no jokes.
            print(f"I don't have any {search_term} jokes...")
            break
        else: 
            print(f'I found {pages} page(s) of {search_term} jokes.')
            pass
        for joke in jokes:
            print(joke['joke'])
            time.sleep(3)
            another = input('Want to hear another? ').lower()
            if another in ['no', 'n', 'please god no']:
                break
            time.sleep(3)
        print(f"End of {search_term} jokes.")
        break

main()