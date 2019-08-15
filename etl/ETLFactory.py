
from enum import Enum

from etl.FacebookETL import FacebookETL
from etl.TwitterETL import TwitterETL


class EtlEnum(Enum):
    TWITTER = 1,
    FACEBOOK = 2

def getEtlInstance(val):
    if val == EtlEnum.TWITTER:
        return TwitterETL()
    if val == EtlEnum.FACEBOOK:
        return FacebookETL()

