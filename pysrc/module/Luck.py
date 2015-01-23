#!/usr/bin/python
#coding: utf-8    


from LuckModule import LuckModule
class Luck(LuckModule):
    def GetLuckName(self):
        return self.sLuckName

    def SetLuckName(self,sLuckName):
        self.sLuckName = sLuckName

    def GetLuckLink(self):
        return self.sLuckLink

    def SetLuckLink(self,sLuckLink):
        self.sLuckLink = sLuckLink

    def GetLuckPicLink(self):
        return self.sLuckPicLink

    def SetLuckPicLink(self,sLuckPicLink):
        self.sLuckPicLink = sLuckPicLink

    def GetLuckContent(self):
        return self.sLuckContent

    def SetLuckContent(self,sLuckContent):
        self.sLuckContent = sLuckContent

    def GetUpdateTime(self):
        return self.iUpdateTime

    def SetUpdateTime(self,iUpdateTime):
        self.iUpdateTime = iUpdateTime

