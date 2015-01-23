#!/usr/bin/python
#coding: utf-8

import json
from horoscopegrabber import Days
from horoscopegrabber import Horoscopes
from datetime import date

HoroscopeGaps=[
    (114,212),
    (213,313),
    (314,412),
    (413,513),
    (514,613),
    (614,714),
    (715,816),
    (817,916),
    (917,1016),
    (1017,1115),
    (1116,1215),
    (1216,0),
]

MessageHandlers=[HoroMessageHandler,SubscribeMessageHandler]
DefaultHandlers=[DefaultMessageHandler]

def Handle(strMsg):
    handleTimes = 0
    for handler in MessageHandlers:
        objHandler=handler(strMsg)
        if objHandler.IsHandled(): handleTimes += 1
    if handleTimes>0: return  handleTimes

    for handler in DefaultHandlers:
        objHandler = handler(strMsg)
        if objHandler.IsHandled(): handleTimes += 1
    return handleTimes
         
        
class MessageHandler:
    def __init__(self,strMsg):
        self.m_objJsonMsg = json.loads(strMsg)
        self.__isHandled  = self.__Handle()
        
    def __Handle(self):
        return False

    def IsHandled(self):
        return __isHandled
#{
#"type": "text",
#"from_user": "oXjmaflNNxoim22",
#"content": "Hello, world!"
#"message_id": 123456789,
#"created_at": 134325435556
#}
class HoroMessageHandler:
    def SendLuck(username,luckname):
        lk = LuckDao.QueryByName(luckname)
        if lk:
            ret = SendMessage('sanook',username,
                lk.sLuckContent,
                lk.sLuckLink,
                lk.sLuckPicLink) 
            log.info("SendMessage(%s)=%d" % (username,ret))
        else:
            log.error("Luck.QueryByName(%s) is None" % luckname)
    
    def text2date(text):
        try:
            day,month,year=text.split('/',2)
            return date(year,month,day)
        except Exception, e:
            return None
    
    def date2horoscope(odate): 
        magic = odate.month*100+odate.day
        i=0
        for begin,end in HoroscopeGaps:
            if begin<=magic<=end:
                return Horoscopes[i]            
            else:
                i+=1
        return Horoscopes[11]

    def __handle(self):
        objJsonMsg = self.m_objJsonMsg
        if objJsonMsg['type']=='text' :
            content = objJsonMsg['content']
            username= objJsonMsg['from_user']
            
            birthday = text2date(objJsonMsg['content'])        
            if birthday==None:
                pass
            else:
                weekday = birthday.isoweekday()
                if weekday==7:weekday=0
                self.SendLuck(Days[weekday])
                horoscope = date2horoscope(birthday) 
                self.SendLuck(horoscope)
            
            
class SubscribeMessageHandler(Handler):
    def __handler(self):
        objJsonMsg = self.m_objJsonMsg
        if objJsonMsg['type']=='subscribe':
            messagesender.SendMessage('sanook',objJsonMsg['username'],'hello','','')
            return 
