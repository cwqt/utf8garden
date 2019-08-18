#!/usr/bin/python3
import random
import os
import tweepy
import time

from dotenv import load_dotenv
load_dotenv(".env")

CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#max dimensions = 16x16 grid = 256 characters

fmap = []
for y in range(0, 4):
	fmap.append([])
	for x in range(0, 4):
		fmap[y].append(random.randint(0,8))

# horizontal flip
fmap2 = []
for y in fmap:
	fmap2.append(y[::-1])

# join
for y in range(len(fmap)):
	fmap[y] = fmap[y] + fmap2[y]

#vertical flip
fmap2 = fmap.copy()
for y in reversed(fmap2):
	fmap.append(y)

print("\n")

plantmap = ['🌷','🌸','🌹','🌺','🌻','🌼','🌱','🌳','🌲']
string = ""

for y in fmap:
	for x in y:
		string += str(plantmap[x])
	string += "\n"

api.update_status(status=string)
print("Posted!")
print(string)
