from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream, API
import json

#Variables that contains the user credentials to access Twitter API
consumer_key = "**************"
consumer_secret = "***************"
access_token = "**************"
access_token_secret = "****************"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_status(self, status):
        print(status._json)

        #try:

            #print('full_text:', status.extended_tweet['full_text'])
            #twt_data.append(('full_text:', status.extended_tweet['full_text']))
            #twt_data.append(('location:', status.user.location))
            #twt_data.append(('time_zone:', status.user.time_zone))
            #twt_dict = dict(twt_data)
            #print(twt_dict)
            #with open('twtstreamtest.json', 'a') as f:
                #json.dump(twt_dict,f)
            #return True

        #except Exception as ex:
            #print(ex)
            #print('text:', status.text)
            #twt_data.append(('text:', status.text))
            #twt_data.append(('location:', status.user.location))
            #twt_data.append(('time_zone:', status.user.time_zone))

    def on_error(self, status_code):
        if status_code == 420:
            return False

#if __name__ == '__main__':

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

msl = StdOutListener()
ms = Stream(auth = api.auth, listener = msl)
ms.filter(track=['#gunviolence', '#schoolshooting', '#guncontrol', '#enough', '#NeverAgain', '#MarchForOurLives'], async=True)
