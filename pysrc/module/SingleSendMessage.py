#!/usr/bin/python
#coding: utf-8    


from SingleSendMessageModule import SingleSendMessageModule
class SingleSendMessage(SingleSendMessageModule):
    def GetSSMId(self):
        return self.iSSMId

    def SetSSMId(self,iSSMId):
        self.iSSMId = iSSMId

    def GetFromUin(self):
        return self.iFromUin

    def SetFromUin(self,iFromUin):
        self.iFromUin = iFromUin

    def GetFromUsername(self):
        return self.sFromUsername

    def SetFromUsername(self,sFromUsername):
        self.sFromUsername = sFromUsername

    def GetToUin(self):
        return self.iToUin

    def SetToUin(self,iToUin):
        self.iToUin = iToUin

    def GetToUsername(self):
        return self.sToUsername

    def SetToUsername(self,sToUsername):
        self.sToUsername = sToUsername

    def GetMessageContent(self):
        return self.sMessageContent

    def SetMessageContent(self,sMessageContent):
        self.sMessageContent = sMessageContent

    def GetMessageLink(self):
        return self.sMessageLink

    def SetMessageLink(self,sMessageLink):
        self.sMessageLink = sMessageLink

    def GetCreateTime(self):
        return self.iCreateTime

    def SetCreateTime(self,iCreateTime):
        self.iCreateTime = iCreateTime

    def GetSent(self):
        return self.iSent

    def SetSent(self,iSent):
        self.iSent = iSent

    def GetSendTime(self):
        return self.iSendTime

    def SetSendTime(self,iSendTime):
        self.iSendTime = iSendTime

    def GetPicLink(self):
        return self.sPicLink

    def SetPicLink(self,sPicLink):
        self.sPicLink = sPicLink

