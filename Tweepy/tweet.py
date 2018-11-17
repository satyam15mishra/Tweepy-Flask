import tweepy
from flask import Flask, request

consumer_key = 'HSUdBnSRVroa1R2O3DM2bnAY7'
consumer_secret = '7piXeV9dYG9vdokLMqVgtgzXVHlA24U0pEiRn8BHLjRbTd2mel'
access_token = '780954917515124736-6ucBM7w84wWkoCVoEjG9D3OGDF88HE1'
access_token_secret = 'FqoGm7w3SnChaXz2BLrgyk3hneTGywnXGj4rZgZrvE99H'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text.encode('utf-8')

usr = api.get_user('goldy999')
print usr.screen_name
print usr.followers_count

for friend in usr.friends():
	print friend.screen_name