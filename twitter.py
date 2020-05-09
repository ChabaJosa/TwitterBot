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

topics          = ["JavaScript", "JS", "Python", "Py", "Pandas", "SciPy", "React", "NodeJS", "ExpressJS", "MongoDB", "MERN", "MERNSTACK", "Code", "Programming", "Bot", "ImAbot", "Developers", "Tech", "Django", "UdemyCode", "StackOverflow", "ReactNative", "SQL", "AI", "MachineLearning"]
thyTimes        = [10, 15, 8, 18, 9, 13, 25, 30, 20]
searchGlobal    = random.choice(topics)
tweetQty        = len(topics)*random.choice(thyTimes)

#With Variating Keywords
def RetweetRandom(NumberOfRetweets):
    
    for i in range(0,NumberOfRetweets):
        search   = random.choice(topics)
        for tweet in tweepy.Cursor(api.search, search).items(1):
            try:
                print("Tweet Retweeted with the keyword: ", search)
                tweet.retweet()
                time.sleep(random.choice(thyTimes))
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

def FavoriteRandom(NumberOfRetweets):

    for i in range(0,NumberOfRetweets):
        try:
            print("Tweet Liked with the keyword: ", search)
            tweet.favorite()
            time.sleep(random.choice(thyTimes))
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


#With plenty of one specific keyword
def RetweetTopic():

    for tweet in tweepy.Cursor(api.search, searchGlobal).items(tweetQty):
        try:
            print("Tweet Retweeted with the keyword: ", search)
            tweet.retweet()
            time.sleep(random.choice(thyTimes))
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def FavoriteTopic():

    for tweet in tweepy.Cursor(api.search, searchGlobal).items(tweetQty):
        try:
            print("Tweet Liked with the keyword: ", search)
            tweet.favorite()
            time.sleep(random.choice(thyTimes))
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

#Following / Getting Followers
def followTechie():  
    # Try using RegEx here
    print(api.search_users("Web Developer"[2][10]))
    # for follower in tweepy.Cursor(api.followers).items(): #Prints out all the users
    #     print(follower.name).encode("utf-8")
    # for follower in tweepy.Cursor(api.followers).items():
    #     follower.follow()


def randomness(argument):
    print(argument)
    randomFunks = [RetweetRandom(10), FavoriteRandom(10), FavoriteTopic(), RetweetTopic() ]
    random.choice(randomFunks)



randomness("Argument")