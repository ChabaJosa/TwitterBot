import  tweepy
import  time
import  random
from    configparser import ConfigParser
import  pprint

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
def RetweetRandomTopics(NumberOfRetweets):
    
    for i in range(0,NumberOfRetweets):
        search   = random.choice(topics)
        for tweet in tweepy.Cursor(api.search, searchGlobal).items(1):
            try:
                print("Tweet Retweeted with the random keyword: ", search)
                tweet.retweet()
                time.sleep(random.choice(thyTimes))
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

def FavoriteRandomTopics(NumberOfLikes):

    for i in range(0,NumberOfLikes):
        for tweet in tweepy.Cursor(api.search, searchGlobal).items(1):
            try:
                print("Tweet Liked with the random keyword: ", searchGlobal)
                tweet.favorite()
                time.sleep(random.choice(thyTimes))
            except tweepy.TweepError as e:
                print(e.reason)
            except StopIteration:
                break

#With plenty of one specific keyword
def RetweetAboutSpecificTopic(topicOfChoice, NumberOfRetweets):
    
    for tweet in tweepy.Cursor(api.search, topicOfChoice).items(NumberOfRetweets):
        try:
            print("Tweet Retweeted with the specific keyword: ", topicOfChoice)
            tweet.retweet()
            time.sleep(random.choice(thyTimes))
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

def FavoriteAboutSpecificTopic(topicOfChoice, NumberOfLikes):

    for tweet in tweepy.Cursor(api.search, topicOfChoice).items(NumberOfLikes):
        try:
            print("Tweet Liked with the specific keyword: ", topicOfChoice)
            tweet.favorite()
            time.sleep(random.choice(thyTimes))
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

#Following / Getting Followers
def followTechies():  
    # Try using RegEx here
    # print(api.search_users("Web Developer"[2][10]))
    # for follower in tweepy.Cursor(api.followers).items(): #Prints out all the users
    #     print(follower.name).encode("utf-8")
    for follower in tweepy.Cursor(api.followers).items():
        pprint.pprint(follower.description)
        # follower.follow()


def randomness():
    print("Hello")
    # The arguments are for each are how many 
    randomFunks = [RetweetRandomTopics(1), FavoriteRandomTopics(2), RetweetAboutSpecificTopic("ReactJS", 1), FavoriteAboutSpecificTopic("ReactNative", 1), followTechies() ]

randomness()

