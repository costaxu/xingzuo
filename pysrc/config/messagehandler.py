#!/usr/bin/python
#coding: utf-8

import json

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

class HoroMessageHandler:
    def __handle(self):
        objJsonMsg = self.m_objJsonMsg
        if objJsonMsg['type']=='text' :
            if objJsonMsg['content']  

