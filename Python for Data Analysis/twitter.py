import tweepy
import json
import nltk
from tweepy import OAuthHandler

consumer_key='yhin76TvCam58pLsfIomtPpNx'
consumer_secret='CPSkmak5pzgtE796vQdD7VrU5PAPQhnLRzjMSPf8XnwTkMwhOJ'
access_token='35008484-7aNmsudoCLXXb6n9T8OBB6HLjTiwZNHgiHpTQVV4Q'
access_secret='IvPpn460cGIvQQ6ENqxpuxn7IQi0PzCeVrAAyFcjUPYc5'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
    
def process_or_store(tweet):
    print(json.dumps(tweet))
        
for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)
    
#for friend in tweepy.Cursor(api.followers).items():
    #print friend

ldnlat = 51.5074
ldnlong= 0.1278


query="tech"
lang="en"
locale="London"
x=api.search_users(query,1,1)

for word in nltk.word_tokenize(str(x)):
    print word
    
re.findall("screen_name",nltk.word_tokenize(str(x)))
api.search(query,lang,locale)