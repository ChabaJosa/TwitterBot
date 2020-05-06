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

# print(user) #Brings back user data

for follower in tweepy.Cursor(api.followers).items(): #Prints out all the users
    print(follower.name).encode("utf-8")

