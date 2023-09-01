# This file will hold the implementation to scraping data from twitter.
import os
from datetime import datetime, timezone
import logging
import tweepy


logger = logging.getLogger("twitter")

# From tweepy docs: This creates a handler that simplifies the communication with twitter's API.
auth = tweepy.OAuthHandler(
    os.environ.get("TWITTER_API_KEY"), os.environ.get("TWITTER_API_SECRET")
)
auth.set_access_token(
    os.environ.get("TWITTER_ACCESS_TOKEN"), os.environ.get(
        "TWITTER_ACCESS__SECRET")
)
api = tweepy.API(auth)


def scrape_user_tweets(username, num_tweets=100):
    """Scrapes a user's tweets and returns them in a list of dicts.
    Each dict contains the following fields:
    - time_posted(relative to now)
    - text
    - url
    """

    # user_timeline gets the latest tweets from a user.
    tweets = api.user_timeline(screen_name=username, count=num_tweets)

    tweet_list = []

    # filter retweets and replies. return a list with only original tweets from the user.
    for tweet in tweets:
        if "RT @" not in tweet.text and not tweet.text.startswith("@"):
            tweet_dict = {}
            tweet_dict["time_posted"] = str(
                datetime.now(timezone.utc) - tweet.created_at
            )
            tweet_dict["text"] = tweet.text
            tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet.id}"
            tweet_list.append(tweet_dict)

    return tweet_list
