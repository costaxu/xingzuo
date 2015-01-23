#!/usr/bin/pytho
#coding: utf-8
import urllib2
import json
from datetime import datetime
from datetime import timedelta


class AccessToken:
    def __init__(self,sToken,oGenTime,sTimeout):
        self.access_token=sToken
        self.generate_time=oGenTime
        self.token_time_out=int(sTimeout)

    def isValid(self):
        now=datetime.now()
        if self.generate_time is None:
            return False
        if now<self.generate_time:
            return False
        if now - self.generate_time > timedelta(seconds=self.token_time_out):
            return False
        return True 

class AccessTokenGenerator:
    tokenmap={}
    def __init__(self,appid,secret):
        self.appid=appid
        self.secret=secret

    def GenAccessToken(self):
        url="http://api.weixin.qq.com/token.json?appid=%s&grant_type=client_credential&secret=%s" % \
            (self.appid,self.secret)
        try:    
            f = urllib2.urlopen(url,timeout=5)
        except urllib2.HTTPError , e:
            print e.code
            return None

        except urllib2.URLError , e:
            print e.strerror
            return None

        result = json.loads(f.read())
        oAccessToken = AccessToken(result['access_token'],datetime.now(),result['expires_in'])
        tokenmap=AccessTokenGenerator.tokenmap
        tokenmap[self.appid]=oAccessToken
        return result['access_token']

    def GetAccessToken(self):
        tokenmap=AccessTokenGenerator.tokenmap
        if tokenmap.has_key(self.appid):
            token=tokenmap[self.appid] 
            if token.isValid():
                return token.access_token
        return self.GenAccessToken() 
