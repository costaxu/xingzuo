#!/usr/bin/python
#coding: utf-8

import urllib2
from logapi import log
import json
from module.Luck import luck
from module.LuckDao import LuckDao
import time
Days=[
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
    ]

Horoscopes=[
    'Capricorn',
    'Aquarius',
    'Pisces',
    'Aries',
    'Taurus',
    'Gemini',
    'Cancer',
    'Leo',
    'Virgo',
    'Libra',
    'Scorpius',
    'Sagitarius',
        ]

class HoroscopeGrabber:
    def __init__(self):
        self.daily_url = 'http://m.sanook.com/feed/weblog/horo/daily?format=json'
        self.weekly_url = 'http://m.sanook.com/feed/weblog/horo/weekly?format=json'

    def Save(name,link,image_link,luck):
        lk=Luck()
        lk.SetLuckName(name)
        lk.SetLuckLink(link)
        lk.SetLuckPicLink(image_link)
        luck=luck.replace("<p>","")
        luck=luck.replace("</p>","\n")
        luck=luck.replace("<strong>","")
        luck=luck.replace("</strong>"," ")
        lk.SetLuckContent(luck)
        
        ret = LuckDao.Update(lk):
        log.info("LuckDao.Update()=(%d,%s)" % (ret,LuckDao.GetErrorMsg()))
        if ret :
            ret = LuckDao.insert(lk)
            log.error("LuckDao.Insert()=(%d,%s)" % (ret,LuckDao.GetErrorMsg())) 
        pass

    def GrabDaily(self):
        try:
            f = urllib2.url_open(self.daily_url,5)        
            objJson = json.loads(f.read())
            i=0
            for item in objJson['item']:
                name=Day[i]
                link=item['link']
                image_link=item['image']            
                luck=item['content_encodec'].encode('utf-8')
                Save(name,link,image_link,luck)
                i+=1
            f.close()
                
                
        except urllib2.HTTPError,e:
            print "HTTP ERROR: %d" % e.code
            return False 
        except urllib2.URLError, e:
            print "URL ERROR:%s" % e.strerror
            return False
        except Exception, e:
            print e.strerror
            return False

    
     def GrabWeekly(self):
        try:
            f = urllib2.url_open(self.weekly_url,5)        
            objJson = json.loads(f.read())
            i=0
            for item in objJson['item']:
                name=Horoscope[i]
                link=item['link']
                image_link=item['image']            
                luck=item['content_encodec']
                Save(name,link,image_link,luck)
                i+=1
            f.close()
                
                
        except urllib2.HTTPError,e:
            print "HTTP ERROR: %d" % e.code
            return False 
        except urllib2.URLError, e:
            print "URL ERROR:%s" % e.strerror
            return False
        except Exception, e:
            print e.strerror
            return False

if __name__=='__main__':
    grabber = HoroscopeGrabber()
    while True:
        grabber.GrabWeekly()
        grabber.GrabDaily()                  
        time.sleep(60)
