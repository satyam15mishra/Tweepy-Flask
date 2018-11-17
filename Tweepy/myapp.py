from flask import Flask, render_template, request, redirect, url_for, session, g, flash
import tweepy 

app = Flask(__name__) 
 
@app.route('/')
def page():
    return render_template('home.html')
 
@app.route('/send', methods=['GET', 'POST'])
def send():
	if request.method=='POST':
		user_interest = request.form['user_interest']
		
		consumer_key = 'HSUdBnSRVroa1R2O3DM2bnAY7'
		consumer_secret = '7piXeV9dYG9vdokLMqVgtgzXVHlA24U0pEiRn8BHLjRbTd2mel'
		access_token = '780954917515124736-6ucBM7w84wWkoCVoEjG9D3OGDF88HE1'
		access_token_secret = 'FqoGm7w3SnChaXz2BLrgyk3hneTGywnXGj4rZgZrvE99H'

		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

		auth.set_access_token(access_token, access_token_secret)

		api = tweepy.API(auth)

		usr = api.get_user(user_interest)
		a = usr.followers_count

		public_tweets = api.user_timeline(screen_name=user_interest, count=100, include_rts=True, exclude_replies=True)


		return render_template('send.html', user_interest = user_interest, a = a, public_tweets = public_tweets)

	return render_template('home.html')

if (__name__ == "__main__"):
	app.debug = True
	app.run()