from flask import Flask, render_template, request, redirect, url_for, session, g, flash
import tweepy 
import requests


#############################################################################################
################################  TWEEPY SETUP  #################################################

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

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

if (__name__ == "__main__"):
	app.debug = True
	app.run(threaded = True)
