import tweepy
import time
import random
from configparser import ConfigParser

parser = ConfigParser()
parser.read('credentials.ini')
key_1 = parser.get('TwitterCredentials','key_1')
key_2 = parser.get('TwitterCredentials','key_2')
key_3 = parser.get('TwitterCredentials','key_3')
key_4 = parser.get('TwitterCredentials','key_4')

# http://docs.tweepy.org/en/latest/api.html?highlight=retweet#API.retweet
auth    = tweepy.OAuthHandler(key_1,key_2)
auth.set_access_token(key_3,key_4)


api     = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user    = api.me()
# .me() is to use the authenticated user's profile

# print(user) #Brings back user data
# for follower in tweepy.Cursor(api.followers).items(): #Prints out all the users
#     print(follower.name).encode("utf-8")

topics   = ["JavaScript", "JS", "Python", "Py", "Pandas", "SciPy", "React", "NodeJS", "ExpressJS", "MongoDB", "MERN", "MERNSTACK", "Code", "Programming", "Bot", "ImAbot", "Developers", "Tech", "Django", "UdemyCode", "StackOverflow", "ReactNative", "SQL", "AI", "MachineLearning"]
thyTimes = [10, 15, 8, 18, 9, 13, 25, 30, 20]
# search   = random.choice(topics)
tweetQty = len(topics)*random.choice(thyTimes)

# Try using RegEx here
def Retweet():
    search   = random.choice(topics)
    for tweet in tweepy.Cursor(api.search, search).items(tweetQty):
        try:
            print("Tweet Retweeted with the keyword: ", search)
            tweet.retweet()
            time.sleep(random.choice(thyTimes))
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def Favorite():
    search   = random.choice(topics)
    for tweet in tweepy.Cursor(api.search, search).items(tweetQty):
        try:
            print("Tweet Liked with the keyword: ", search)
            tweet.favorite()
            time.sleep(random.choice(thyTimes))
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

# def followTechie():
#     for follower in tweepy.Cursor(api.followers).items():
#     follower.follow()

randomFunks = [Retweet(), Favorite() ]

def Randomness():
    random.choice(randomFunks)


