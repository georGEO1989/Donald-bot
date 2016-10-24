import tweepy
import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
from secrets import *

auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
api = tweepy.API(auth)
response = 'Have you grabbed anyone\'s pussy today?'
user_to_troll = '#####'
handle = '@' + user_to_troll
# timeline = api.user_timeline(user_to_troll)[0]
# last_tweet = timeline.id

# print last_tweet

# api.update_status(response + handle, last_tweet) # replys to tweet ID with the response

class MyStreamListener(tweepy.StreamListener): # stream class

	def on_status(self, status):
		# print(status.id) # prints latest tweet ID
		print(status.text)
		# api.update_status(response + handle, status.id) # need to get this to see latest tweet and reply to it.


streamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=streamListener)


myStream.userstream(user_to_troll)
# myStream.filter(track=[handle]) # used just to filter words, doesn't work to filter users