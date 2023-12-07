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

        self.conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='Inaba', db='Kuko', charset='utf8mb4')

    def getConnect(self):
        return self.conn

    def getCursor(self):
        return self.conn.cursor(pymysql.cursors.DictCursor)

# conf = ConfigParser()
# conf.read("../resources/pdbc.ini")
# host = conf["pdbc"]["host"]
# port = conf["pdbc"]["port"]
# user = conf["pdbc"]["user"]
# passwd = conf["pdbc"]["passwd"]
# db = conf["pdbc"]["db"]
# charset = conf["pdbc"]["charset"]
#
# conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='Inaba', db='Kuko', charset='utf8mb4')
#
# def getConnect():
#     return conn
#
# def getCursor():
#     return conn.cursor(pymysql.cursors.DictCursor)