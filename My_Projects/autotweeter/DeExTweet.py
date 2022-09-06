import os
import tweepy
from config import api_key, api_secret, access_token, token_secret


auth = tweepy.OAuth1UserHandler(
    consumer_key= api_key,
    consumer_secret= api_secret,
    access_token= access_token,
    access_token_secret= token_secret 
)


api = tweepy.API(auth)

DATA_FILENAME = os.path.expanduser("days.txt")

with open(DATA_FILENAME, "r") as f:
    count = f.read()

with open(DATA_FILENAME, 'w') as nf:
    count = int(count) + 1
    new_count = str(count)
    nf.write(new_count)


tweet = f"Open to work! Day: {count}!"



api.update_status(tweet)



# api = tweepy.API(auth)

# Prints My Feed Tweets
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# Prints My Screen Name, Follwer Count (0, haha), and Followed Accounts
# user = api.get_user(screen_name='ttajohnson')
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#     print(friend.screen_name)

# Show Whether or Not Authenticated
# auth = tweepy.OAuthHandler(api_key, api_secret)
# auth.set_access_token(access_token, token_secret)
# api = tweepy.API(auth)
# try:
#     api.verify_credentials()
#     print("Authenticated")
# except:
#     print("Not Authenticated")

# auth = tweepy.OAuthHandler(api_key, api_secret)
# auth.set_access_token(access_token, token_secret)


