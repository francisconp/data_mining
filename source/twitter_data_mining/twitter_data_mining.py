from pprint import pprint
from tweepy import Stream
from tweepy.streaming import StreamListener
from kafka import KafkaProducer, KafkaConsumer
import tweepy
import json
import os
 
producer = KafkaProducer(bootstrap_servers='localhost:9092')

class TagStream(StreamListener):
     def on_data(self, data):
        self.info = json.loads(data)
        print json.dumps(self.info, indent=4)
        
        producer.send('topic_hashtag', json.dumps(self.info))
        producer.flush()

        return True

     def on_error(self, status):
        print(status)
        return True
 
class TwitterStream():
    def __init__(self):
        try:
            self.consumer_key = os.environ['CONSUMER_KEY']
            self.consumer_secret = os.environ['CONSUMER_SERCRET']
            self.access_token = os.environ['ACCESS_TOKEN']
            self.access_secret = os.environ['ACCESS_SECRET']
            self.hashtag = os.environ['HASHTAG']
        except:
            print """Please, set all environment informations:
                CONSUMER_KEY
                CONSUMER_SERCRET
                ACCESS_TOKEN
                ACCESS_SECRET
                HASHTAG
            """
            return 0

        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_secret)
        self.twitter_stream = Stream(self.auth, TagStream())
        self.twitter_stream.filter(track=[self.hashtag])

if __name__ == '__main__':
    TwitterStream()