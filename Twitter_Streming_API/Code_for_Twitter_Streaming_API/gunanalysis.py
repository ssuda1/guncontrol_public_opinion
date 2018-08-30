import json
import pandas as pd
import matplotlib.pyplot as plt

path = '/Users/satokosuda/twtgun3.24.json'

with open(path,'r') as fhand:
    

with open('result.json','w') as fp:
    json.dump(path, fp)

#print(tweet_data[:2])
#print(count)
#print(tweet_data)

#tweets = pd.DataFrame()
#tweets['text'] = list(map(lambda tweet: tweet['text'], tweet_data))
#tweets['location']= list(map(lambda tweet: tweet['user']['location'], tweet_data))
#tweets['time_zone']= list(map(lambda tweet: tweet['user']['time_zone'], tweet_data))
#tweets['time']= list(map(lambda tweet: tweet['created_at'], tweet_data))
#tweets['extended_text'] = list(map(lambda tweet: tweet['extended_tweet'], tweet_data))

#tweets.to_csv('schoolshooting3.csv')
