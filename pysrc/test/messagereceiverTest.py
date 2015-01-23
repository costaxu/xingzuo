#!/usr/bin/python
#coding: utf-8

import unittest
import control.messagereceiver
from control.messagereceiver import MessageReceiver
class MessageReceiverTest(unittest.TestCase):

    thainews_appid='wx1c1f7fb38578563e'
    thainews_secret='0a41e5475704b5723d7f2f87d2d07202'
    def testConnectStream(self):
        appid=MessageReceiverTest.thainews_appid
        secret=MessageReceiverTest.thainews_secret
        mr=MessageReceiver(appid,secret)  
        mr.Connect()
    def testHandle(self):
        appid=MessageReceiverTest.thainews_appid
        secret=MessageReceiverTest.thainews_secret
        mr=MessageReceiver(appid,secret)
        mr.Connect()
        mr.Handle()
