from flask import Flask, render_template, request, redirect, url_for, session, g, flash
import tweepy 
import requests
from textblob import TextBlob


#############################################################################################
################################  TWEEPY SETUP  #################################################

consumer_key = 'xxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
##############################################################################################

app = Flask(__name__) 
 
@app.route('/')
def page():
    return render_template('home.html')
 

#---------------T W I T T E R  A P I---------------
#---------------GETTING TWEET SPECIFIC TO USERNAME---------------
@app.route('/send', methods=['GET', 'POST'])
def send():
	if request.method=='POST':
		user_interest = request.form['user_interest']

		usr = api.get_user(user_interest)
		a = usr.followers_count

		public_tweets = api.user_timeline(screen_name=user_interest, count=100, include_rts=True, exclude_replies=True)


		return render_template('send.html', user_interest = user_interest, a = a, public_tweets = public_tweets)

	return render_template('home.html')

#---------------GETTING TWEETS SPECIFIC TO HASHTAG---------------
@app.route('/hash', methods=['GET', 'POST'])
def hash():
	if request.method=='POST':
		hashtag = request.form['hashtag']
		h = tweepy.Cursor(api.search, q = hashtag, count = "10", lang = "en", since = "2018-11-11").items()
		return render_template('hash.html', h = h, hashtag = hashtag)

	return render_template('map.html')

#---------------GETTING TWEETS FOR SENTIMENT ANALYSIS---------------
@app.route('/senti', methods=['GET', 'POST'])
def senti():
	if request.method=='POST':
		word = request.form['senti_word']
		#pt = api.search(word)
		analysis = TextBlob(word)
		sentiment = analysis.sentiment.polarity
		if sentiment > 0:
			ans = 'Positive Statement'
		elif sentiment < 0:
			ans = 'Negative Statement'
		else:
			ans = 'Neutral Statement'
		return render_template('senti.html', word = word, ans = ans, sentiment = sentiment)
	return render_template('senti_form.html')


if (__name__ == "__main__"):
	app.debug = True
	app.run(threaded = True)
