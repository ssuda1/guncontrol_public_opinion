from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream, API
import json

#Variables that contains the user credentials to access Twitter API
consumer_key = "**********************"
consumer_secret = "************************"
access_token = "***********************"
access_token_secret = "*************************"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

result = api.search(q = '#gunviolence, #schoolshooting', count = 100000, tweet_mode = 'extended')
print(result)
with open('twt4.csv','a') as file:
    for twt in result:
       file.write(twt.full_text)

file.close()

#Still not extract full text
