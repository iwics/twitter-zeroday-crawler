import tweepy
import os
from datetime import datetime

bearer_token = os.environ['TWITTER_BEARER']
client = tweepy.Client(bearer_token)

# Get User's Tweets

# This endpoint/method returns Tweets composed by a single user, specified by
# the requested user ID

with open('user_list.txt', 'r') as file:
    user_list = file.read().splitlines()

for user_id in user_list:
    try:
        response = client.get_users_tweets(user_id, max_results=10, start_time=datetime.fromisoformat('2022-04-12T00:05:23+01:00'))

    # By default, only the ID and text fields of each Tweet will be returned
        if response.data:
            for tweet in response.data:
                if "zeroday".lower() in tweet.text or "0day".lower() in tweet.text:
                    print(tweet.text)
    except Exception as e:
        print('Error while getting tweets: {}'.format(str(e)))