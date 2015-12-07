# -*- coding: UTF-8 -*- 
import struct
import act_def
import SerialOpt
class CtrlData:
  nDir    = 0;
  nSpeed  = 0;
  nLen    = 0;

class Protocol:
  data =[]
  def __init__(self):
    for i in range(0,4):
      dat = CtrlData();
      self.data.append(dat)

  def SetData(self,i,nDir,nSpeed,nLen):
    self.data[i].nDir = nDir
    self.data[i].nSpeed = nSpeed
    self.data[i].nLen = nLen
  
  def PackDat(self):
    strAll = ''
    strDat = '';
    Datlen = 0
    for i in range(0,4):
      strTmp = struct.pack('BBH',self.data[i].nDir,self.data[i].nSpeed,self.data[i].nLen)
      strDat = strDat + strTmp;
    Datlen =  len(strDat)
    strAll = struct.pack('BBBBBhh%ds'%(Datlen),0xEF,10,0,1,1,0xAA,0xBB,strDat)
    return strAll
  def AddAct(CtrlData):
    for i in range(0,4):
      pass

if __name__=='__main__':
  a = Protocol();
  a.SetData(0,1,100,100);
  a.SetData(1,1,100,100);
  a.SetData(2,1,100,100);
  a.SetData(3,1,100,100);
  
  z = a.PackDat()
  logfile = file('.\\dat.log','wb')
  logfile.write(z)
  logfile.close()
  
  
  