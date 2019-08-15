
import tweepy as tw
import configparser

from etl import Utils
from etl.AbstractETL import AbstractEtl
from etl.RatingData import RatingData


class TwitterETL(AbstractEtl):

    def __init__(self):
        super().__init__()
        self.api = self.getTwitterApiAccess()
        self.source = 'Tweeter'

    def getTwitterApiAccess(self):
        config = configparser.RawConfigParser()
        config.read('/Users/omero/Library/Preferences/PyCharm2019.1/scratches/credential.ini')
        consumerKey = config['TWITTER']['consumer_key']
        consumerSecret = config['TWITTER']['consumer_secret']
        accessToken = config['TWITTER']['access_token']
        accessTokenSecret = config['TWITTER']['access_token_secret']
        auth = tw.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        return tw.API(auth)

    def extract(self):
        return  self.api.user_timeline("ynetalerts")

    def transfer(self, tweetResult):
        data = []
        for status in tweetResult:
            if Utils.isThereAurl(status.text):
                likes = status.retweet_count + status.favorite_count
                url = Utils.getUrl(status.text)
                data.append(RatingData(url, likes))
        return data










