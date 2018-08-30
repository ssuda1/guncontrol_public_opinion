from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream, API
import json

#Variables that contains the user credentials to access Twitter API
consumer_key = "EDtTKZasT63Crc3wDcTSyoiPh"
consumer_secret = "0PVIrkTgFSRma4fWjjwznAgpNR7yl3dKZ8a9N77vZMu6bpPiIF"
access_token = "1094940992-pxSc1pjyoflJx0fo9bjb0P3QBdqvwQzyUYRRtTe"
access_token_secret = "Ri7UXZ5Ox8d7g5Wu7QZurohWqz6XGNYEafLeN1nWoZVJ0"

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
