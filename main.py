from requests_oauthlib import OAuth1Session
import logging
import json


class Twitter(object):
    def __init__(self, status):
        creds = open('creds.txt').readlines()
        self.session = OAuth1Session(creds[0].strip(), creds[1].strip(),
                                     creds[2].strip(), creds[3].strip()
                                     )
        self.tweet_url = "https://api.twitter.com/1.1/statuses/update.json"
        self.get_choices()


    def get_choices(self):
        choice = input("What you wanna do? \n (2) Post Tweet \n (2) Post tweet with media")
        choices = {1: self.tweet_post, 2: self.tweet_status}.get(choice, self.error)
        choices()


    def tweet_status(self):
        logger.info("Twitter: Tweet Status ")
        params = {'status': self.status} 
        post = self.session.post(self.tweet_url, params=params)

        if post.status_code == 200:
            logger.info("Status posted ")
        else:
            logger.error("Status not posted {}".format(post.json()))


    def error(self):
        print("error ")




if __name__ == "__main__":
    status = input("Enter your status ")
    if len(status) > 280:
        print("Twitter only allows 280char, tweets")
        logging.error("Can't have tweets over 280 characters")
    else:
        twitter = Twitter(status)

