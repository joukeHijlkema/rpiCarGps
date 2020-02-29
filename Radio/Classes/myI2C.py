#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  =================================================
#   - Author jouke hijlkema <jouke.hijlkema@onera.fr>
#   - jeu. août 10:30 2019
#   - Initial Version 1.0
#  =================================================
import quick2wire.i2c as i2c

class myI2C(object):
    """Documentation for myI2C

    """
    def __init__(self,i2c_address,i2C_bus,inRegs,outRegs):
        super(myI2C, self).__init__()
        self.i2c_address = i2c_address
        self.i2C_bus     = i2C_bus
        self.inRegs      = inRegs
        self.outRegs     = outRegs

        c = 0
        for k,v in self.inRegs.items():
            c=max(c,v[0][0],v[-1][0])
        self.In  = bytearray(c+1)
        c = 0
        for k,v in self.outRegs.items():
            c=max(c,v[0][0],v[-1][0])
        self.Out  = bytearray(c+1)

        
    ## --------------------------------------------------------------
    ## Description : print info on the In/Out registers
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 14-24-2019 11:24:05
    ## --------------------------------------------------------------
    def Info (self,w):
        f = self.outRegs if w=="SEND" else self.inRegs
        d = self.Out     if w=="SEND" else self.In
        print("=== %s ==="%w)
        # print("FREQ: %.1f"%self.getFreq(out=(w=="SEND")))
        
        for k,v in f.items():
            print("%s: %s"%(k,self.Get(d,v)))
            
        print("=== BYTES ===")
        for i,b in enumerate(d):
            print("BYTE %s: %s"%(i,format(b,'08b')))


    ## --------------------------------------------------------------
    ## Description : get a range
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 15-49-2019 11:49:13
    ## --------------------------------------------------------------
    def Range (self,what):
        out = []
        
        r = what[0][0]
        b = what[0][1]
        rs = what[-1][0]
        bs = what[-1][1]
        while 1:
            out.append((r,b))
            # print(r,b)
            if r>=rs and b<=bs:
                break
            b-=1
            if b<0:
                r+=1
                b =7
        return out
        
    ## --------------------------------------------------------------
    ## Description : set a value in the Out register and send it
    ## NOTE : the In register is for reading only
    ## -
    ## Author : jouke hylkema
    ## date   : 14-54-2019 12:54:32
    ## --------------------------------------------------------------
    def Set (self,what,value):
        bv = bin(value)[2:]
        # print("set %s to %s"%(what,bv))
        for i,r in enumerate(self.Range(self.outRegs[what])):
            # print("set bit %s of reg %s to %s"%(r[1],r[0],bv[i]))
            self.setKthBit(r[0],r[1],int(bv[i]))

    ## --------------------------------------------------------------
    ## Description : Get a value from the registers
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 15-47-2019 11:47:16
    ## --------------------------------------------------------------
    def Get (self,regs,what):
        out = ""
        for r in self.Range(what):
            # print("read from reg %s, bit %s"%(r[0],r[1]))
            if self.getKthBit(regs[r[0]],r[1]):
                out+="1"
            else:
                out+="0"
        return int(out,2)

    ## --------------------------------------------------------------
    ## Description : get data by name
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 15-42-2019 13:42:19
    ## --------------------------------------------------------------
    def getByName (self,Reg,Name):
        if Reg=="Out":
            return self.Get(self.Out,self.outRegs[Name])
        else:
            return self.Get(self.In,self.inRegs[Name])
        
    ## --------------------------------------------------------------
    ## Description : set the kth bit of of the nth byte to v in the Out register
    ## NOTE : the In register is for reading only
    ## -
    ## Author : jouke hylkema
    ## date   : 14-02-2019 13:02:08
    ## --------------------------------------------------------------
    def setKthBit (self,n,k,v):
        if v==1:
            self.Out[n] |= pow(2,k)
        else:
            self.Out[n] &= (255-pow(2,k))
        
    
    ## --------------------------------------------------------------
    ## Description : get the kth bit from byte
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 14-14-2019 14:14:42
    ## --------------------------------------------------------------
    def getKthBit (self,d,k):
        # print(type(d))
        if isinstance(d,bytes):
            d = d[0]
            # print(type(d))
        return ((d & pow(2,k)) > 0)

    ## --------------------------------------------------------------
    ## Description : send data
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 11-49-2019 13:49:38
    ## --------------------------------------------------------------
    def Send (self):
        self.Info("SEND")
        with i2c.I2CMaster(1) as bus:
            bus.transaction(
                i2c.writing_bytes(self.i2c_address,self.Out[0],self.Out[1],self.Out[2],
                                  self.Out[3],self.Out[4]))

    ## --------------------------------------------------------------
    ## Description : Read from the tea
    ## NOTE : 
    ## -
    ## Author : jouke hylkema
    ## date   : 14-33-2019 14:33:33
    ## --------------------------------------------------------------
    def Read (self):
        with i2c.I2CMaster(1) as bus:
            tmp = bus.transaction(i2c.reading(self.i2c_address, len(self.In)))
        self.In = tmp[0]
        self.Info("READ")

        

