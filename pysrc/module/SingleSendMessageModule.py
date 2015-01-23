#!!/usr/bin/python 
#coding:utf-8
class SingleSendMessageModule:
    def __init__(self):
        self.iSSMId=0
        self.iFromUin=0
        self.sFromUsername=''
        self.iToUin=0
        self.sToUsername=''
        self.sMessageContent=''
        self.sMessageLink=''
        self.iCreateTime=0
        self.iSent=0
        self.iSendTime=0
        self.sPicLink=''

    def __repr__(self):
        str="""(id:%d, FromUin:%d, FromUsername %s, ToUin: %d, ToUsername: %s,\n""" % (self.iSSMId,self.iFromUin,self.sFromUsername,self.iToUin,self.sToUsername)
        str+= """MsgContent: %s,\n""" % self.sMessageContent
        str+= """CreateTime: %d, Sent: %d, SendTime: %d, PicLink: %s)\n""" % (self.iCreateTime,self.iSent,self.iSendTime,self.sPicLink)
        return str
