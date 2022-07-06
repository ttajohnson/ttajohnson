# ....Lab 15 Version 1 ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

import requests
import time

def get_random_quote():
    response = requests.get("https://favqs.com/api/qotd", headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'})
    rand_quote = response.json()
    quote = rand_quote['quote']['body']
    author = rand_quote['quote']['author']
    print(f'{quote} \n-{author}')

# get_random_quote()

# ....Lab 15 Version 2 ~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-

def get_keyword_quote():

    while True:
        user_keyword = input("Enter a keyword to search for quotes: ")
        page_number = 1
        
        while True:
            response = requests.get(f'https://favqs.com/api/quotes', headers = {'Authorization': 'Token token="855df50978dc9afd6bf86579913c9f8b"'}, params = {'filter':user_keyword, 'page':page_number})
            list_quotes = response.json()
            number_of = len(list_quotes['quotes'])
            
            if list_quotes['quotes'][0]['body'] == 'No quotes found':
                time.sleep(1)
                print('No quotes found...')
                break
            
            print(f'Here are {number_of} quotes associated with {user_keyword} - page {page_number}')
            
            time.sleep(2)
            
            for i in range(len(list_quotes['quotes'])):
                quote = list_quotes['quotes'][i]['body']
                author = list_quotes['quotes'][i]['author']
                print(quote)
                print(f'-{author}\n')
                time.sleep(1)
            
            next_or_done = input("Enter 'next page' or 'done': ")
            
            if next_or_done == 'done':
                break
            
            elif next_or_done == 'next page':
                page_number += 1
                if list_quotes['last_page'] == True:
                    time.sleep(1)
                    print('No more quotes.')
                    break
                continue
        
        cont_or_break = input("Would you like to find more quotes? Y/N ").lower()
        
        if cont_or_break == 'n':
            print('Closing program...\nGoodbye!')
            break
        
        elif cont_or_break == 'y':
            continue
        

get_keyword_quote()
