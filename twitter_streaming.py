#Import the necessary methods from tweepy library
import tweepy
from tweepy.streaming import Stream
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(Stream):

#    def on_data(self, data):  # Work with raw data, if you'd like
#        print(data)           # This will override on_status if you un-comment it

    def on_status(self, status): # Print Tweets as they stream in
        if not status.truncated: # Handle both 140- and 280-character Tweets
            print(status.text)
        else:
            print(status.extended_tweet['full_text'])
	#print(status._json) # Make sure to use the ._json attribute when you save to file
        
        
    def on_error(self, status): # Print Errors if you encounter them
        if status == 401:
            print("401: Authentication Error") # 401 is an authentication error
        else:
            print(status)       # Other error codes get printed 


#This handles Twitter authetication and the connection to Twitter Streaming API
# Authenticate to Twitter
#auth = OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_token, access_token_secret)

#l = StdOutListener(consumer_key, consumer_secret, access_token, access_token_secret)
stream = StdOutListener(consumer_key, consumer_secret, access_token, access_token_secret)

#This line filters Twitter Streams using the specified search terms
#Do not change these search terms
stream.filter(track=['vaccine', 'adverse event', 'safety', 'injury', 'mandatory', 'side effect', 'monograph', 'death'], languages=['en'])
