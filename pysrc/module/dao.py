#!/usr/bin/python
#coding:utf-8

from config import config
import MySQLdb
from logapi import log
class Dao:
    try:
        __conn=None
        __conn=MySQLdb.connect(host=config.db['ip'],
                            db= config.db['db'],
                            user=config.db['username'],
                            passwd=config.db['password'])
    except MySQLdb.Error, e:
        print "Connect MySQL error: %s" % e.args[1] 
        log.error("Connect MySQL error: %s" % e.args[1] 
)

    def __init__(self):
        self.sErrorMsg='OK'
        self.cursor=None
        self.conn=Dao.__conn
        self.DBQuery('SET NAMES utf8')

    def GetErrorMsg(self):
        return self.sErrorMsg

    def DBQuery(self,sql,param=()):
        conn=Dao.__conn
        if self.cursor!=None:
            self.cursor.close()
            self.cursor=None
        self.cursor=conn.cursor()
        cursor=self.cursor

        try:
            n=cursor.execute(sql,param)
            result_set=cursor.fetchall()
            return result_set
        except MySQLdb.Error, e:
            self.sErrorMsg='MySQL Error %d: %s' % (e.args[0],e.args[1]) 
            return None

    def DBClose(self):
        Dao.__conn.close()
        
