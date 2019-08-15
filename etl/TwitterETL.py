
import tweepy as tw
import pandas as pd
import configparser

class TwitterETL(AbstractEtl):


    def getTwitterApiAccess(self):
        config = configparser.RawConfigParser()
        config.read('ConfigFile.properties')
        consumerKey = config.get("consumer_key")
        consumerSecret = config.get("consumer_secret")
        accessToken = config.get("access_token")
        accessTokenSecret = config.get("access_token_secret")
        auth = tw.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        return  tw.API(auth)

    def __init__(self):
        tw = self.getTwitterApiAccess()



