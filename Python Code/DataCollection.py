import os
import tweepy
import tweepy as tw
import pandas as pd

consumer_key= 'ACN50GxbhEO8ySEeD5bo1KEul'
consumer_secret= '0bU6eatF2gjcy4WPH10RrgLslGdBVQmWjOfLDltOncl8AjtRxU'
callback_uri = "oob"

auth = tw.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()
print(redirect_url)

user_pin_input = input("What is the pin value?")
auth.get_access_token(user_pin_input)

api = tweepy.API(auth)

pd.DataFrame()
for tweet in tweepy.Cursor(api.search, q='aart').items(10):
    print(tweet.text)