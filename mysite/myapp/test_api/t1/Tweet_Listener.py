import tweepy
from tweepy import OAuthHandler # to authenticate Twitter API
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json


# Twitter developer Credentials to connect to twitter_spark account

consumer_key = '7SPrh2xcgpxuOLLy13JJfpaMH'
consumer_secret = 'bz1JdRd9BLveGxuWwqAiuo2xwZsoNbByu5vAyl0mvWbJJh6HDS'

access_token = '1360418282755379200-lQ8PIPMT2hh0Z2L9bqjJPZmHwXCwYy'
access_secret = 'zcFW0psud0ZWYKe3JG0cwugEZY33rN7bXUsvzNEr5fAOB'

class TweetsListener(StreamListener):
    # initialized the constructor
    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            # read the Twitter data which comes as a JSON format
            msg = json.loads(data)

            # the 'text' in the JSON file contains the actual tweet.
            print(msg['text'].encode('utf-8'))

            # the actual tweet data is sent to the client socket
            self.client_socket.send(msg['text'].encode('utf-8'))
            return True

        except BaseException as e:
            # Error handling
            print("Ahh! Look what is wrong : %s" % str(e))
            return True

    def on_error(self, status):
        print(status)
        return True


def sendData(c_socket):
    # authentication
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    # twitter_stream will get the actual live tweet data
    twitter_stream = Stream(auth, TweetsListener(c_socket))
    # filter the tweet feeds related to "corona"
    twitter_stream.filter(track=['BTC','ETH','BNB','ADA','USDT'])
    # in case you want to pass multiple criteria
    # twitter_stream.filter(track=['DataScience','python','Iot'])


# create a socket object
s = socket.socket()

# Get local machine name : host and port
host = "127.0.0.1"
port = 3333

# Bind to the port
s.bind((host, port))
print("Listening on port: %s" % str(port))

# Wait and Establish the connection with client.
s.listen(5)
c, addr = s.accept()

print("Received request from: " + str(addr))

# Keep the stream data available
sendData(c)