
import tweepy as tw
import pandas as pd
import configparser

from etl.AbstractETL import AbstractEtl


class TwitterETL(AbstractEtl):

    def __init__(self):
        self.api = self.getTwitterApiAccess()

    def getTwitterApiAccess(self):
        config = configparser.RawConfigParser()
        config.read('ConfigFile.properties')
        consumerKey = config.get("consumer_key")
        consumerSecret = config.get("consumer_secret")
        accessToken = config.get("access_token")
        accessTokenSecret = config.get("access_token_secret")
        auth = tw.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        return tw.API(auth)

    def extract(self):
        for statuses in tw.Cursor(self.api.user_timeline).pages(3)
            print(statuses)
        pass










