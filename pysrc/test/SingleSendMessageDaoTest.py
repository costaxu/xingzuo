#!/usr/bin/python
#coding: utf-8

import unittest

from module.SingleSendMessageDao import SingleSendMessageDao
from module.SingleSendMessage    import SingleSendMessage
import datetime
import time

class SingleSendMessageDaoTest(unittest.TestCase):
    ssmdao=SingleSendMessageDao()
    tNow = int(time.time())
    print tNow
    ssm=SingleSendMessage()
    ssm.SetFromUin(10000)
    ssm.SetFromUsername('costaxu')
    ssm.SetToUin(20000)
    ssm.SetToUsername('harriet')
    ssm.SetMessageContent('go to hell')
    ssm.SetMessageUrl('http://baidu.com')
    ssm.SetCreateTime(tNow)
    ssm.SetSent(1)
    ssm.SetSendTime(tNow+10)
  
    def testInsert(self):
        ssm = SingleSendMessageDaoTest.ssm
        ssmdao=SingleSendMessageDaoTest.ssmdao
        ssmid = ssmdao.Insert(ssm) 
        self.assertTrue(ssmid>=0) 
        ssmdao.Delete(ssmid)
   
    def testQueryById(self):
        ssm = SingleSendMessageDaoTest.ssm
        ssmdao=SingleSendMessageDaoTest.ssmdao
        ssmid = ssmdao.Insert(ssm) 
        ssm1  = ssmdao.QueryById(ssmid)
        self.assertTrue(ssm1 is not None)
        print ssm1
        print ssm

        self.assertTrue(ssm1.iFromUin          == ssm.iFromUin)
        self.assertTrue(ssm1.sFromUsername     == ssm.sFromUsername)
        self.assertTrue(ssm1.iToUin            == ssm.iToUin)
        self.assertTrue(ssm1.sToUsername       == ssm.sToUsername)
        self.assertTrue(ssm1.sMessageContent   == ssm.sMessageContent)
        self.assertTrue(ssm1.sMessageUrl       == ssm.sMessageUrl)
        self.assertTrue(ssm1.iCreateTime       == ssm.iCreateTime)
        self.assertTrue(ssm1.iSent             == ssm.iSent)
        self.assertTrue(ssm1.iSendTime         == ssm.iSendTime)
        self.assertTrue(ssm1.sPicPath          == ssm.sPicPath) 
        
        ssmdao.Delete(ssmid)
       
    def testUpdate(self):
        ssm = SingleSendMessageDaoTest.ssm
        ssmdao=SingleSendMessageDaoTest.ssmdao
        ssmid = ssmdao.Insert(ssm) 
        ssm.SetToUsername('myself')
        ssm.SetSendTime=SingleSendMessageDaoTest.tNow 
        
        ret = ssmdao.Update(ssm)
        self.assertTrue(ret==0)
        ssm1  = ssmdao.QueryById(ssmid)
        self.assertTrue(ssm1 is not None)
        self.assertTrue(ssm1.iFromUin          == ssm.iFromUin)
        self.assertTrue(ssm1.sFromUsername     == ssm.sFromUsername)
        self.assertTrue(ssm1.iToUin            == ssm.iToUin)
        self.assertTrue(ssm1.sToUsername       == ssm.sToUsername)
        self.assertTrue(ssm1.sMessageContent   == ssm.sMessageContent)
        self.assertTrue(ssm1.sMessageUrl       == ssm.sMessageUrl)
        self.assertTrue(ssm1.iCreateTime       == ssm.iCreateTime)
        self.assertTrue(ssm1.iSent             == ssm.iSent)
        self.assertTrue(ssm1.iSendTime         == ssm.iSendTime)
        self.assertTrue(ssm1.sPicPath          == ssm.sPicPath) 
        ssmdao.Delete(ssmid)
       
    def testDelete(self):        
        ssm = SingleSendMessageDaoTest.ssm
        ssmdao=SingleSendMessageDaoTest.ssmdao
        ssmid = ssmdao.Insert(ssm) 
        ret = ssmdao.Delete(ssmid)
        self.assertTrue(ret==0)
        ret = ssmdao.Delete(ssmid)
        self.assertTrue(ret==-1)
