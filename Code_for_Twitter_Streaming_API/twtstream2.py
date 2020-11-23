from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream, API

#Variables that contains the user credentials to access Twitter API
consumer_key = "*******************"
consumer_secret = "*******************"
access_token = "*******************"
access_token_secret = "*******************"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):

        try:
            for twt in data:
                with open('twtstreamtest.json', 'a') as f:
                    f.write(twt)
            return True
        except Exception as ex:
            print(ex)

    def on_error(self, status):
        print(status)
        return False

#if __name__ == '__main__':

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = API(auth)

msl = StdOutListener()
ms = Stream(auth = api.auth, listener = msl)
ms.filter(track=['#gunviolence','#schoolshooting'], async=True)

#Continue to gunanalysis2.py
