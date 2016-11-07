markovBot is a simple Twitter bot that will generate a sentence using Markov chains and then tweet it.

Follow [@_murakamibot](https://twitter.com/_murakamibot) and [@jamesjoycebot](https://twitter.com/jamesjoycebot) to see it in action!


# Getting Started
## Dependencies

Install the [markovify](https://github.com/jsvine/markovify) and [tweepy](http://www.tweepy.org/) packages:

`pip install markovify`

`pip install tweepy`

## Fill corpus of example text

This project comes with a copy of Charles Dickens's _A Tale of Two Cities_ as its example corpus.

Lots of good sources are available from [Project Gutenberg](https://www.gutenberg.org/).

Save the text file as `corpus.txt`

## Test Markov chain

`python tweet.py` to see an example tweet.


## Connecting Twitter

Create a Twitter account.

Sign in to the [Apps page](https://apps.twitter.com/) and get four pieces of data:

* Consumer Key
* Consumer Secret
* Access Token
* Access Token Secret

Run

`make credentials_file`

And edit the `twitter_credentials.json` file with the above four pieces of data.

Change the `PUBLISH` variable in `tweet.py` from `False` to `True` to have the bot post to Twitter.


# Deploy to [AWS Lambda](https://aws.amazon.com/lambda) (Optional)

Steps for setting up auto-tweet account (using OS X or Linux):

1. Add PyPI dependencies to `requirements.txt`.
2. Run `make prepare` to generate `lambda_bundle.zip`.
3. In the AWS console, create a Python 2.7 function with `tweet.send_tweet` as the handler. Upload `lambda_bundle.zip` to use as the code. Add a "Scheduled Event" event source.
