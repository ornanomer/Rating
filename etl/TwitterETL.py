
import tweepy as tw
import configparser

from etl.AbstractETL import AbstractEtl


class TwitterETL(AbstractEtl):

    def __init__(self):
        self.api = self.getTwitterApiAccess()

    def getTwitterApiAccess(self):
        config = configparser.RawConfigParser()
        config.read('/Users/omero/Library/Preferences/PyCharm2019.1/scratches/tweeter.ini')
        consumerKey = config['TWITTER']['consumer_key']
        consumerSecret = config['TWITTER']['consumer_secret']
        accessToken = config['TWITTER']['access_token']
        accessTokenSecret = config['TWITTER']['access_token_secret']
        auth = tw.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        return tw.API(auth)

    def extract(self):
        return  self.api.search("ynetalerts")

    def transfer(self, data):
        for status in data :
            if(if thereUrl)
            likes = status.favority
            url =











