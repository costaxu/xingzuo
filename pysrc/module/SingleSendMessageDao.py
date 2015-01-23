#!/usr/bin/python
#coding:utf-8

from dao import Dao
from SingleSendMessage import SingleSendMessage
class SingleSendMessageDao(Dao):
    def Insert(self,ssm):
        conn=self.conn
        rs = self.DBQuery("""insert into SingleSendMessage\
    (FromUin,FromUsername,ToUin,ToUsername,MessageContent,MessageLink,CreateTime,Sent,SendTime,PicLink) \
    values(%s,%s,%s,%s,%s,%s,from_unixtime(%s),%s,from_unixtime(%s),%s)""",
        (
        ssm.iFromUin,
        conn.escape_string(ssm.sFromUsername),
        ssm.iToUin,
        conn.escape_string(ssm.sToUsername),
        conn.escape_string(ssm.sMessageContent),
        conn.escape_string(ssm.sMessageLink),
        ssm.iCreateTime,
        ssm.iSent,
        ssm.iSendTime,
        ssm.sPicLink,
        )
        )

        print ssm.iCreateTime
        if rs is None:
            return -1
        
        rs=self.DBQuery("""select last_insert_id()""");
        if rs is None:
            return -2
            
        return int(rs[0][0])    
         
       
    def Delete(self,ssmid):
        rs=self.DBQuery("Delete from SingleSendMessage where SSMId=%d" % ssmid)
        if rs is None:
            return -1
        else:
            return 0

    def Update(self,ssm):
        conn=self.conn
        rs=self.DBQuery("""Update SingleSendMessage set FromUin=%s,\
                FromUsername=%s,\
                ToUin=%s,\
                ToUsername=%s,\
                MessageContent=%s,\
                MessageLink=%s,\
                CreateTime=from_unixtime(%s),\
                Sent=%s,\
                SendTime=from_unixtime(%s) \
                PicLink=%s where SSMId=%s""",
            (
                ssm.iFromUin,
                conn.escape_string(ssm.sFromUsername),
                ssm.iToUin,
                conn.escape_string(ssm.sToUsername),
                conn.escape_string(ssm.sMessageContent),
                conn.escape_string(ssm.sMessageLink),
                ssm.iCreateTime,
                ssm.iSent,
                ssm.iSendTime,
                ssm.sPicLink,
                ssm.iSSMId
             )

            )
        if rs is None:
            return -1
        else:
            return 0

    FIELDS ="""SSMId,FromUin,FromUsername,ToUin,ToUsername,MessageContent,MessageLink,unix_timestamp(CreateTime),Sent,unix_timestamp(SendTime),PicLink""" 

    def __Result2SingleSendMessage(self,result):
        ssm=SingleSendMessage()
        ssm.SetSSMId(int(result[0]))
        ssm.SetFromUin(int(result[1]))
        ssm.SetFromUsername(str(result[2]))
        ssm.SetToUin(int(result[3]))
        ssm.SetToUsername(str(result[4]))
        ssm.SetMessageContent(str(result[5]))
        ssm.SetMessageLink(str(result[6]))
        ssm.SetCreateTime(int(result[7]))
        ssm.SetSent(int(result[8]))
        ssm.SetSendTime(int(result[9]))
        ssm.SetPicLink(result[10])
        return ssm

    def QueryById(self,ssmid):
        FIELDS = SingleSendMessageDao.FIELDS
        rs=self.DBQuery("""Select %s from SingleSendMessage where SSMId=%s""",(FIELDS,ssmid))
        if rs is None or len(rs)!=1:
            print self.GetErrorMsg()
            return None
        else:
            result=rs[0]
            return self.__Result2SinglSendMessage(result) 

    def QueryUnsendMessage(self):
        FIELDS = SingleSendMessageDao.FIELDS
        rs=self.DBQuery("""select %s from SingleSendMessage where Sent=0""" % FIELDS)
        if rs is None :
            print self.GetErrorMsg()
            return None
        else:
            ssm_list=[]
            for result in rs:
                ssm_list.append(__Result2SingleSendMessage(result))
            return ssm_list    
                    
