import sys
import tweepy
from textblob import TextBlob
from wordcloud import WordCloud
import pandas as pd
import numpy as np
import re
import nltk
from nltk.corpus import stopwords
import string

def treat(name):
	consumerKey = "8wcyNW5YZT5zNTl9uV05miZcy"
	consumerSecret = "QIuZ5bN0g8es7GPhgY9OCWFenfd3Zn2Ohs3UFmIsZpsi3wtvpT"
	accessToken = '1275478991844134912-s9PVmvpuMX6pfTnROTKq9aPHEi3SGp'
	accessTokenSecret = 'i28aoj25ZorFlgo8CPXm4bypzBFk9hyZER48fEp4bHSbx'
	auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
	auth.set_access_token(accessToken, accessTokenSecret)
	api = tweepy.API(auth, wait_on_rate_limit = True)

	searchTerm = name
	NoOfTerms = 200


	posts = api.user_timeline(screen_name=searchTerm, count=NoOfTerms, lang ="en", tweet_mode="extended")
	df = pd.DataFrame([tweet.full_text for tweet in posts], columns=['Tweets'])
	nltk.download('stopwords')


	




	

	# Create a function to get the subjectivity
	def getSubjectivity(text):
	   return TextBlob(text).sentiment.subjectivity

	# Create a function to get the polarity
	def getPolarity(text):
	   return  TextBlob(text).sentiment.polarity


	# Create two new columns 'Subjectivity' & 'Polarity'
	df['Subjectivity'] = df['Tweets'].apply(getSubjectivity)
	df['Polarity'] = df['Tweets'].apply(getPolarity)
	df.head(5)



	df['Analysis'] = df['Polarity'].apply(getAnalysis)

	emotions={
		  "neutral":0,
		  "positive":0,
		  "wpositive":0,
		  "spositive":0,
		  "negative":0,
		  "wnegative":0,
		  "snegative":0
	}

	return max(emotions,key=lambda k:emotions[k])

def getAnalysis(score):
	  if (score== 0):  # adding reaction of how people are reacting to find average later
		    return "neutral"
	  elif (score > 0 and score<= 0.3):
		    return "wpositive"
	  elif (score> 0.3 and score <= 0.6):
		    return "positive"
	  elif (score > 0.6 and score <= 1):
		    return "spositive"
	  elif (score > -0.3 and score <= 0):
		    return "wnegative"
	  elif (score > -0.6 and score <= -0.3):
		    return "negative"
	  elif (score > -1 and score <= -0.6):
		    return "snegative"


def clean(dataFrame):
	    dataFrame=dataFrame.lower()
	    nopunc = [char for char in dataFrame if char not in string.punctuation]
	    nopunc = ''.join(nopunc)
	    
	    #2 Remove Stop Words
	    clean_words = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]
	    
	    #3 Return a list of clean words

	    return clean_words


