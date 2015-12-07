# -*- coding: UTF-8 -*- 
import time
import threading
import serial
import logging 
class SerOpt:
  ser = 0
  comInfo = ''
  BandRate = 0
  __LastRecv = 0
  __PackDat = []
  __recvStatus = 0
  __status = {'SOP':0,'LEN':1,'DAT':2}
  __packetLen = 0
  __ParseDatFun = 0
  def __init__(self,comInfo,Bandrate):
    self.comInfo = comInfo;
    self.Bandrate = Bandrate;
    self.__recvStatus = self.__status['SOP']
  def SetCallBack(self,ParseDatFun):
    self.__ParseDatFun = ParseDatFun
  def OpenSer(self):
    if self.ser and self.ser.isOpen():
      self.ser.Close();
    self.ser = serial.Serial(self.comInfo,self.Bandrate,timeout=3)   
    if self.ser:
      t1 = threading.Thread(target=self.recvThreadFun)
      t1.daemon = True
      t1.start()
      logging.info("open "+self.comInfo+" success")
      return 1;
    else:
      logging.warning("open "+self.comInfo+" failure")
      return 0;
      
  def getDat(self):
    if self.ser == 0:
      return ''
  def Send(self,dat):
    #print ('send'+str(self.ser))
    if self.ser:
      SendLen = self.ser.write(dat)
      return SendLen
    return 0
  def CleanDat(self):
    self.__PackDat = [0]*64
    self.__recvStatus = self.__status['SOP']
  
  def recvThreadFun(self):
    while 1:
      if self.ser:
        dat = self.ser.read(1)
        if len(dat) == 0:
          continue  
        dat = ord(dat)
        print hex(dat)
        __LastRecv = time.clock()
        if self.__recvStatus == self.__status['SOP']:
          print('1')
          if dat == 0xFE:
            print('2')
            self.__recvStatus = self.__status['LEN']
        elif self.__recvStatus == self.__status['LEN']:
          print('3')
          self.__recvStatus = self.__status['DAT']
          self.__PackDat.append(dat)
          self.__packetLen = dat + 5
        elif self.__recvStatus == self.__status['DAT']:
          self.__PackDat.append(dat)
          self.__packetLen -= 1
          if self.__packetLen == 0:
            print('data len'+str(len(self.__PackDat)))
            self.__ParseDatFun(self.__PackDat)
            self.CleanDat(); 
            
        print self.__recvStatus,self.__packetLen
  def Close(self):
    self.ser.close()
    self.ser = 0;

def PrintDat(Dat):
  print 'data:'
  print Dat  
if __name__=='__main__':
  opt = SerOpt('com7',115200)
  time.clock()
  opt.SetCallBack(PrintDat)
  if not opt.OpenSer():
    print 'open failure'
  else:
    while 1:
      time.sleep(0.1)
      
  