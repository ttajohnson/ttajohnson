# profile = {                                   Close but no cigar!
#     'username': 'Aa', 
#     'password': 'bB'

# }

# user = profile['username']
# passw = profile['password']

# def login(username_attempt, password_attempt, profile):
#     if username_attempt != user or password_attempt != passw:
#         print('\nError! your username or password was incorrect! ')
#     elif username_attempt == user and password_attempt == passw:
#         print(f'\nWelcome, {user}! ')

# username_attempt = input('Enter your username: ')
# password_attempt = input('Enter your password: ')

# login(username_attempt, password_attempt, profile)

profile = {
    'username': 'Aa', 
    'password': 'bB'
}


def login(username, passw, prof):
    if username != prof['username'] or passw != prof['password']:
        return False
    elif username == prof['username'] and passw == prof['password']:
        return True


username_attempt = input('Enter your username: ')
password_attempt = input('Enter your password: ')


if login(username_attempt, password_attempt, profile):
    print(f'Welcome, {profile["username"]}')
else:
    print('Error! Your username or password was incorrect!')

login(username_attempt, password_attempt, profile)
