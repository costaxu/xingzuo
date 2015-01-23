#!/usr/bin/python
#coding: utf-8

import datetime
from module.singlesendmessagedao import SingleSendMessageDao
from module.singlesendmessage    import SingleSendMessage
from logapi import log

ssmdao=SingleSendMessageDao()

def CreateSubscribeMessage(sUser):
    ssm = SingleSendMessage()
    ssm.SetFromUsername()
    ssm.SetToUsername(sUser)
    ssm.SetMessageContent('Thailand welcome you')
    ssm.SetCreateTime(datetime.now())
    
    ret = ssmdao.insert(ssm)     
    if ret<0 :
        log.error("dao.insert(ssm:(%s,%s,%s ))=(%d,%s)" % 
        (   ssm.GetUsername(),
            ssm.GetToUsername(), 
            ssm.GetMessageContent(),
            ret,
            ssmdao.GetErrMsg()
        ))
    log.info("dao.insert(ssm:(%s,%s,%s ))=(ssmid:%d,%s)" % 
        (   ssm.GetUsername(),
            ssm.GetToUsername(), 
            ssm.GetMessageContent(),
            ret,
            ssmdao.GetErrMsg()
        ))

    return 0    


