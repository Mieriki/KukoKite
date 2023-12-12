from configparser import ConfigParser

import pymysql

class dbUtil:
    def __init__(self):
        conf = ConfigParser()
        conf.read("../resources/pdbc.ini")
        self.host = conf["pdbc"]["host"]
        self.port = conf["pdbc"]["port"]
        self.user = conf["pdbc"]["user"]
        self.passwd = conf["pdbc"]["passwd"]
        self.db = conf["pdbc"]["db"]
        self.charset = conf["pdbc"]["charset"]

        self.conn = pymysql.connect(host=self.host, port=int(self.port), user=self.user, passwd=self.passwd, db=self.db, charset=self.charset)

    def getConnect(self):
        return self.conn

    def getCursor(self):
        return self.conn.cursor(pymysql.cursors.DictCursor)