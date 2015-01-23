#!/usr/bin/python
#coding: utf-8

from module.SingleSendMessage import SingleSendMessage
from module.SingleSendMessageDao import SingleSendMessageDao
from logapi import log
import messageapi
def SendMessage(fromusername,tousername,content,url,picUrl):
    ssm=SingleSendMessage()
    ssm.SetFromUsername(fromusername)
    ssm.SetToUsername(tousername)
    ssm.SetMessageContent(content)
    ssm.SetMessageLink(url)
    ssm.SetPicLink(picUrl)
    ret = SingleSendMessageDao.Insert(ssm)
    log.info("SingleSendMessageDao.Insert()=%d" % (ret))
    return

def RealSendMessage(ssm):
    picFile = DownloadPic(ssm.GetPicLink())
    if picFile is None:
        log.error("DownloadPic(%s) fail" % )
        return -1
    mediaid=messageapi.UploadPicture(picFile)
    picFile.close()
    if mediaid==-1:
        log.error("ERR: UploadPic fail")
        return -1
    ret = messageapi.Send(ssm.GetFromUsername,ssm.GetToUsername(),
            ssm.GetMessageContent(),
            ssm.GetMessageLink(),
            mediaid)
    log.info("messageapi.Send(%d)=%d" % (ssm.GetSSMId(),ret))
    if ret:return -1
    return 0

class MessageSender:
    def __init__(self):
        dao=SingleSendMessageDao()
    
    def RunOnce(self):
        msg_list = dao.QueryUnSendMessage()
        if msg_list is None:
            log.error("dao.QueryUnSendMessage error: %s" % dao.GetErrMessage())
        if len(msg_list)==0:
            log.info("dao.QueryUnSendMessage 0 message to send")
        succ_count = 0
        fail_count = 0
        for msg in msg_list:
            ret = RealSendMessage(msg)
            if ret ==0:succ_count +=1
            else:      fail_count +=1
        log.info("MessageSend.Send: [All %d. Send %d. Fail %d]" % (succ_count+fail_count,
            succ_count,fail_count))

    def Run(self):
        while True:
            self.RunOnce()
            os.sleep(5)
        
if __name__=='__main__':
    sender = MessageSender()
    sender.run()
