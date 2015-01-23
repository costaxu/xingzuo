#!/usr/bin/python
#coding: utf-8

from dao import Dao
class LuckDao(Dao):
        
    def Insert(self,oLuck):
        conn=self.conn
        rs=self.DBQuery("""insert into Luck(\
            LuckName,LuckLink,LuckPicLink,LuckLuck,UpdateTime 
)\
             values(%s,%s,%s,%s,from_unixtime(%s))""",
            (
                conn.escape_string(oLuck.sLuckName),
                conn.escape_string(oLuck.sLuckLink),
                conn.escape_string(oLuck.sLuckPicLink),
                conn.escape_string(oLuck.sLuckLuck).
                oLuck.iUpdateTime
            )
        )
        if rs is None:
            return -1
        else: return 0

    def Delete(self,sLuckName):
        rs=self.DBQuery("Delete from Luck where LuckName=%s" ,
             (conn.escape_string(sLuckName)) ) 
        if rs is None: return -1
        if rs[0][0]!=1: return 1
        else: return 0

    def Update(self,lk):
        conn=self.conn
        rs=self.DBQuery("""Update Luck set \
                            LuckLink=%s,\
                            LuckPicLink=%s,\
                            LuckLuck= %s,\
                            UpdateTime = from_unixtime(%s)\
                            where LuckName= %s""",
                            (
                                conn.escape_string(lk.sLuckPicLink),
                                conn.escape_string(lk.sLuckLink),
                                conn.escape_string(lk.sLuckLuck),
                                lk.iUpdateTime,
                                conn.escape_string(lk.sLuckName),    
                            )
                        )
        if rs is None:return -1
        else: return 0

    def QueryByName(self,sLuckName):
        conn=self.conn
        rs = self.DBQuery("""Select LuckLink,LuckPicLink,LuckLuck,unix_timestamp(UpdateTime) \
                from Luck where LuckName=%s""",(sLuckName) )
        if rs is None or len(rs)!=1:
            return None
        else:
            result = rs[0]
            lk = Luck()
            lk.SetLuckName(sLuckName)
            lk.SetLuckLink(result[0])
            lk.SetLuckPicLink(result[1])
            lk.SetLuckLuck(result[2])
            lk.iUpdateTime(int(result[3]))
            return lk 
