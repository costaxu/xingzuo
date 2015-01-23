#!/usr/bin/python
#coding:utf-8

import urllib2
from urlgrabber.keepalive import HTTPHandler
import json

from control.accesstoken import AccessTokenGenerator
from logapi import log
import fcntl

class MessageReceiver:
    def __init__(self,appid,secret):
        self.m_token_generator=AccessTokenGenerator(appid,secret)
        self.f = None
    def HandleMessage(message):
        if message['type']=='text':
            HandleTextMessage(message)
        elif message['type']=='subscribe':
            HandleSubscribeMessage(message)

    def HandleTextMessage(self,message):
        sContent = message['content']
        sUser    = message['from_user']
        SingleSendMessageManager.CreateTextMessage(sUser,sContent)  

    def HandleSubscribeMessage(self,message):
        for message_content in message['content']:
            sUser = message_content['from_user']
            iSub  = message_content['subscribe']
            if iSub == 1:
                SingleSendMessageManager.CreateSubscribeMessage(sUser)  
    def Connect(self):
        keepalive_handler = HTTPHandler()
        opener = urllib2.build_opener(keepalive_handler)
        urllib2.install_opener(opener)
        sAccessToken = self.m_token_generator.GetAccessToken()
        
        try: 
            url="https://stream.weixin.qq.com/messages?access_token=%s" % sAccessToken 
            log.debug(url)
            self.f=urllib2.urlopen(url)
            #fd = self.f.fp.fileno()

            #flag = fcntl.fcntl(fd,fcntl.F_GETFD)
            #ret = fcnt.fcnt(fd,fcntl.F_SETFD,flag|fcntl.O_NONBLOCK)
            #print "fcntl return %d" % ret
            return True
        except urllib2.HTTPError, e:
            log.error("urlopen = %d" % e.code)
            return False

    def Handle(self):
        str=''
        while True:
            try:
                if str.endswith('\r\n'):
                    messagehandler.Handle(message)   
                    str=''
                str += self.f.read(1)
                continue 
                if str=='\r\n\r\n':continue
            except Exception,e:
                log.error(e) 
                return False
    def Run(self):
        while True:
           if self.Handle()==False:
                self.Connect() 
        
if __name__=='__main__':
    mr=MessageReceiver()
    mr.Run()
