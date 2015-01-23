#!/usr/bin/python
#coding:utf-8

import unittest
from control.accesstoken import AccessTokenGenerator

class AccessTokenTest(unittest.TestCase):
    thainews_appid='wx1c1f7fb38578563e'
    thainews_secret='0a41e5475704b5723d7f2f87d2d07202'

    def testGenAccessToken(self):
        appid = AccessTokenTest.thainews_appid
        secret= AccessTokenTest.thainews_secret
        atg=AccessTokenGenerator(appid,
            secret
        )
        s = atg.GenAccessToken() 
        #print s
        self.assertTrue(s is not None)
        tokenmap=AccessTokenGenerator.tokenmap
        self.assertTrue(tokenmap.has_key(appid))
        objAccessToken = tokenmap[appid]
        
        self.assertTrue(objAccessToken.isValid)
        #print objAccessToken.access_token
        #print objAccessToken.generate_time
        #print objAccessToken.token_time_out
