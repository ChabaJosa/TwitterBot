import tweepy
import time
from configparser import ConfigParser

parser = ConfigParser()
parser.read('credentials.ini')
key_1 = parser.get('TwitterCredentials','key_1')
key_2 = parser.get('TwitterCredentials','key_2')
key_3 = parser.get('TwitterCredentials','key_3')
key_4 = parser.get('TwitterCredentials','key_4')

auth    = tweepy.OAuthHandler(key_1,key_2)
auth.set_access_token(key_3,key_4)


api     = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user    = api.me()
# me () is a tweepy thing: https://stackoverflow.com/questions/17386934/tweepy-api-me-not-returning-user-objects-of-friends

# print(user) #Brings back user data
# for follower in tweepy.Cursor(api.followers).items(): #Prints out all the users
#     print(follower.name).encode("utf-8")

# Do a big array of code keywords an randomize the output
search      = "JavaScript"
tweetQty    = 10

for tweet in tweepy.Cursor(api.search, search).items(tweetQty):
    try:
        print("Tweet Liked")
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break


