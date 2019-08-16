from etl import ETLFactory
from etl.ETLFactory import EtlEnum
from etl.TwitterETL import TwitterETL



if __name__ == '__main__':
    etls = [ETLFactory.getEtlInstance(EtlEnum.FACEBOOK), ETLFactory.getEtlInstance(EtlEnum.TWITTER)]
    for etl in etls:
        etl.execute()