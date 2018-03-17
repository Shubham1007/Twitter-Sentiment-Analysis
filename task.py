from tweepy import OAuthHandler
import re
import tweepy
from textblob import TextBlob
 
class myapp(object):  
    def __init__(self):
        con_key = 'XXXXXXXXXXXXXXX'               # consumer key 
        con_secret = 'XXXXXXXXXXXXXXX'            # consumer secret 
        ac_token = 'XXXXXXXXXXXXXXX '             # access token
        ac_token_secret = 'XXXXXXXXXXXXXXXXXXX'   # acess token secret 
		
        try:
            self.auth = OAuthHandler(con_key, con_secret)
            self.auth.set_access_token(ac_token, ac_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
 
    def clean_tweet(self, tweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
 
    def getsenti(self, tweet):
        ans = TextBlob(self.clean_tweet(tweet))
        if ans.sentiment.polarity > 0:
            return 'positive'
        else:
            return 'negative'
 
    def tweets(self, query, count = 10):
        tweets = []
 
        try:
            ft = self.api.search(q = query, count = count)
 
            
            for tweet in ft:
        
                par_t = {}
                par_t['text'] = tweet.text
                par_t['sentiment'] = self.getsenti(tweet.text)

                if tweet.retweet_count > 0:
                    if par_t not in tweets:
                        tweets.append(par_t)
                else:
                    tweets.append(par_t)
 
            return tweets
 
        except tweepy.TweepError as e:
            print("Error : " + str(e))
try:

    print("Enter the String to get Positive and Negative tweets of that:  ")
    sj=input();
    api = myapp()
    tweets = api.tweets(query = sj, count = 200)
    pts = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    nts = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    print("\n\nPositive tweets:")
    print("\n");

    for twt in pts[:10]:
        print(twt['text'])
                    
    print("\n\nNegative tweets:")
    print("\n");
    for twt in nts[:6]:
        print(twt['text'])
except:
    print(" ")



