
import tweepy as tw
import facebook
import configparser

from etl.AbstractETL import AbstractEtl


class FacebookETL(AbstractEtl):

    def __init__(self):
        self.api = self.getFacebookAccess()

    def getFacebookAccess(self):
        config = configparser.RawConfigParser()
        config.read('/Users/omero/Library/Preferences/PyCharm2019.1/scratches/credential.ini')
        consumerKey = config['FACEBOOK']['facebook_access_token']
        return facebook.GraphAPI(consumerKey)




    def extract(self):
        return self.api.search("ynet")










