#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  =================================================
# Trigger
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - dim. mars 11:29 2017
#   - Initial Version 1.0
#  =================================================
import mysql.connector
from mysql.connector import errorcode

class dataBase:

    def __init__(self,_user,_password,_host,_database):

        try:
            self.cnx = mysql.connector.connect(user=_user, password=_password, host=_host, database=_database)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            print "connection OK"
        
    def Put(self,What,Values):
        while not self.cnx.is_connected():
            self.cnx.reconnect()
            # print "reconnecting to db"
        cursor = self.cnx.cursor()
        cursor.execute(What,Values)
        self.cnx.commit()
        cursor.close()

    def GetOne(self,What):
        while not self.cnx.is_connected():
            self.cnx.reconnect()
        cursor = self.cnx.cursor()
        cursor.execute(What)
        out =  cursor.fetchone()
        cursor.close()
        if out==None:
            return 0
        else:
            return out[0]

    ## --------------------------------------------------------------
    ## Description :get
    ## NOTE :
    ## -
    ## Author : jouke hylkema
    ## date   : 08-23-2017 22:23:39
    ## --------------------------------------------------------------
    def Get (self,What):
        while not self.cnx.is_connected():
            self.cnx.reconnect()
        cursor = self.cnx.cursor()
        cursor.execute(What)
        out = []
        for c in cursor:
            out.append(c)
        cursor.close()
        return out
        
