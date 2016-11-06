import json
import markovify
import tweepy
import logging

PUBLISH = False

logger = logging.getLogger()
logger.setLevel(logging.DEBUG) # options: logging.ERROR, logging.DEBUG, logging.INFO


def tweet_content():
    """Generate tweet string (140 characters or less)
    """

    # Get raw text as string.
    logging.debug("Loading corpus...")
    with open("./corpus.txt") as f:
        text = f.read()

    # Build the model.
    logging.debug("Building markov model...")
    text_model = markovify.Text(text, state_size=2)

    tweet = text_model.make_short_sentence(140)

    return tweet


def send_tweet(event, context):
    """Post tweet
    """
    logging.debug("Loading credentials...")
    with open("twitter_credentials.json", "r") as f:
        credentials = json.load(f)

    logging.debug("Authenticating to Twitter...")
    auth = tweepy.OAuthHandler(credentials["consumer_key"], credentials["consumer_secret"])
    auth.set_access_token(credentials["access_token_key"], credentials["access_token_secret"])
    api = tweepy.API(auth)

    try:
        status = tweet_content()
        logging.debug("Sending tweet...")
        api.update_status(status)

        logging.info("Tweeted '{}'".format(status))
        return "Tweeted {}".format(status)
    except Exception as e:
        logging.error(e.message)
        return e.message


if __name__ == '__main__':
    if PUBLISH:
        print(send_tweet(None, None))
    else:
        print(tweet_content())