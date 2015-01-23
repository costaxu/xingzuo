#!/bin/sh
ip='localhost'
user='root'
pass=''
echo "CREATE DATABASE IF NOT EXISTS xingzuo;" | mysql -h$ip -u$user -p$pass

echo "CREATE TABLE IF NOT EXISTS xingzuo.SingleSendMessage (
        SSMId             INT UNSIGNED NOT NULL AUTO_INCREMENT,
        FromUin           INT UNSIGNED NOT NULL,
        FromUsername      varchar(128) NOT NULL,
        ToUin             INT UNSIGNED NOT NULL,
        ToUsername        varchar(128) NOT NULL,
        MessageContent    text NOT NULL, 
        MessageLink       varchar(1024), 
        CreateTime        TIMESTAMP NOT NULL,
        Sent              INT UNSIGNED NOT NULL,
        SendTime          TIMESTAMP,
        PicLink           varchar(1024),
        PRIMARY KEY( SSMId) ); " | mysql -h$ip -u$user 

echo "CREATE TABLE IF NOT EXISTS xingzuo.Luck(
        LuckName   varchar(128) NOT NULL,
        LuckLink          varchar(1024) NOT NULL,
        LuckPicLink       varchar(1024),
        LuckContent       text NOT NULL,
        UpdateTime        TIMESTAMP NOT NULL,
        PRIMARY KEY( LuckName) ); " | mysql -h$ip -u$user 

echo "Grant all privileges on xingzuo.* to xingzuo@localhost identified by 'ibgwechat123'"|mysql -h$ip -u$user
