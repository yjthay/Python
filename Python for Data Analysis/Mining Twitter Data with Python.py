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
    
for status in tweepy.Cursor(api.home_timeline).items(30):
    print(status.text)
    
for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    process_or_store(status._json) 

for friend in tweepy.Cursor(api.friends).items():
    process_or_store(friend._json)
    
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
    
from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('C:\Users\YJ\OneDrive\Documents\mysearch1.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#TamirRice'])

#fpath="C:\Users\YJ\OneDrive\Documents\mysearch1.json"
#fhand=open(fpath)
#jsonstring=""
#for line in fhand:
#    jsonstring+=line

import json

with open('C:\Users\YJ\OneDrive\Documents\mysearch1.json', 'r') as f:
    line = f.readline() # read only the first tweet/line
    tweet = json.loads(line) # load it as Python dict
    print json.dumps(tweet, indent=4) # pretty-print
    
from nltk.tokenize import word_tokenize

 
tweet = 'RT @marcobonzanini: just an example! :D http://example.com #NLP'
print(word_tokenize(tweet))
# ['RT', '@', 'marcobonzanini', ':', 'just', 'an', 'example', '!', ':', 'D', 'http', ':', '//example.com', '#', 'NLP']
import re
 
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 
tweet = "RT @marcobonzanini: just an example! :D http://example.com #NLP"
print(preprocess(tweet))
# ['RT', '@marcobonzanini', ':', 'just', 'an', 'example', '!', ':D', 'http://example.com', '#NLP']
