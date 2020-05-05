#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import time

auth = tweepy.OAuthHandler("A0rCRsOD3ThFxX74LhmGrnlRN","l9v6dNA3fy9kFkaWjasc4lKPTfdXb7cQNNfgb2Ny0wul4HG9qN")

auth.set_access_token("324455633-MUvZwwyxRhVeSwEfcJ35xAo0dqgBE574x56Kg54X","a0RDrZ5NNMvouGNdVExc6tOtWxZiQ3ZnUzoTsb1kKbWoh")

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# print(user) #Brings back user data

for follower in tweepy.Cursor(api.followers).items(): #Prints out all the users
    print(follower.name).encode("utf-8")

