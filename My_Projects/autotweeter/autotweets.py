import tweepy
from config import api_key, api_secret, access_token, token_secret


auth = tweepy.OAuth1UserHandler(
    consumer_key= api_key,
    consumer_secret= api_secret,
    access_token= access_token,
    access_token_secret= token_secret 
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

for tweet in public_tweets:
    print(tweet.text)
