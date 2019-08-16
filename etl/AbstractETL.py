
import configparser
import pymysql


class AbstractEtl:
    mySql_insert_query = """INSERT INTO rpt_config.rating_estimation (URL, SOURCE, rating_val) 
                                    VALUES (%s, %s, %s) """
    def __init__(self):
        self.sqlConnection = self.getMysQLConnection()
        self.source ='DEFAULT'
    def extract(self):
        pass

    def transfer(self, data):
        pass

    def load(self, dataList):
        cursor = self.sqlConnection.cursor()
        for data in dataList:
            recordTuple = (data.url, self.source, data.likes)
            cursor.execute(self.mySql_insert_query, recordTuple)
        self.sqlConnection.commit()

    def getMysQLConnection(self):
        config = configparser.RawConfigParser()
        config.read('/Users/omero/Library/Preferences/PyCharm2019.1/scratches/credential.ini')
        user = config['MYSQL']['user']
        password = config['MYSQL']['password']
        host = config['MYSQL']['host']
        return pymysql.connect(
            host,
            user,
            password
        )

    def execute(self):
        extactData = self.extract()
        transferData = self.transfer(extactData)
        loadData = self.load(transferData)