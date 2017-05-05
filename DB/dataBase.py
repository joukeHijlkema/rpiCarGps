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
import arrow
import math
import threading
from blinker import signal

class dataBase(threading.Thread):

    def __init__(self,user,password,host,database):
        super(dataBase, self).__init__()
        self.user  = user
        self.pwd   = password
        self.host  = host
        self.db    = database

    ## --------------------------------------------------------------
    ## Description : run the thread
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 03-59-2017 09:59:37
    ## --------------------------------------------------------------
    def run (self):
        
        try:
            self.cnx = mysql.connector.connect(user=self.user, password=self.pwd, host=self.host, database=self.db)
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
        print "add %s to %s"%(Values,What)
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
        # print What
        while not self.cnx.is_connected():
            self.cnx.reconnect()
        cursor = self.cnx.cursor()
        cursor.execute(What)
        out = []
        for c in cursor:
            out.append(c)
        cursor.close()
        return out
        
    ## --------------------------------------------------------------
    ## Description : add data point
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 02-29-2017 08:29:11
    ## --------------------------------------------------------------
    def addPoint (self,data):
        lastPoint  = self.Get("SELECT Lat,Lon FROM Gps ORDER BY id DESC LIMIT 1")
        d          = 100.0
        
        if len(lastPoint)!=0:
            d  = self.Distance(data["lat"],data["lon"],lastPoint[0][0],lastPoint[0][1])
        if d>50.0:
            self.Put(("INSERT INTO Gps (Lat,Lon,Time) VALUES (%s,%s,%s)"),
                    (data["lat"],data["lon"],data["time"]))
            return True
        return False

    ## --------------------------------------------------------------
    ## Description : Distance
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 02-59-2017 10:59:34
    ## --------------------------------------------------------------
    def Distance (self,lat1,lon1,lat2,lon2):
        R = 6371e3
        f1 = math.radians(lat1)
        f2 = math.radians(lat2)
        d1 = math.radians(lon1)
        d2 = math.radians(lon2)

        df = f2-f1
        dd = d2-d1
        
        a = math.pow(math.sin(df/2),2)+math.cos(f1)*math.cos(f2)*math.pow(math.sin(dd/2),2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        return float(R * c)
    def NDistance(self,n1,n2):
        return self.Distance(n1[0],n1[1],n2[0],n2[1])
    def SDistance(self,Nodes):
	if len(Nodes) < 2:
	    D = 0.0
        else:
	    n1 = Nodes[0]
            D  = 0.0
            for n2 in Nodes[1:]:
                D+=self.NDistance(n1,n2)
                n1=n2
        return D

    ## --------------------------------------------------------------
    ## Description : calculate day distance
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 02-20-2017 13:20:45
    ## --------------------------------------------------------------
    def dayDist (self):
        return self.SDistance(self.Get("SELECT Lat,Lon FROM `Gps` WHERE DATE(Time) = CURDATE() ORDER BY Id DESC"))

    ## --------------------------------------------------------------
    ## Description : calculate total distance
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 02-33-2017 13:33:26
    ## --------------------------------------------------------------
    def totDist (self):
        return self.SDistance(self.Get("SELECT Lat,Lon FROM `Gps`"))
        
