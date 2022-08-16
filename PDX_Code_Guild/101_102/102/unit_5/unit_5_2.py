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

while True:
    username_attempt = input('Enter your username: ')
    password_attempt = input('Enter your password: ')
    if login(username_attempt, password_attempt, profile):
        print(f'Welcome, {profile["username"]}')
        break
    else:
        input('Incorrect username or password, would you like to try again?: ')



login(username_attempt, password_attempt, profile)