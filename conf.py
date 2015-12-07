# -*- coding: UTF-8 -*- 
import xml.dom.minidom
import logging
class conf:
  comName =''
  comSpeed = 115200
  comEnable=0
  def __init__(self):
    comName=''
  def LoadConf(self):
    dom = xml.dom.minidom.parse('config.xml')
    root = dom.documentElement
    cc=dom.getElementsByTagName('ComName')
    c1=cc[0]
    self.comName = c1.firstChild.data
    cc=dom.getElementsByTagName('ComSpeed')
    c1=cc[0]
    self.comSpeed = c1.firstChild.data
    cc=dom.getElementsByTagName('ComEnable')
    c1=cc[0]
    self.comEnable = c1.firstChild.data
    logging.info("LoadConf comName: "+self.comName+" comSpeed:"+str(self.comSpeed))
    logging.info("LoadConf comEnable: "+ str(self.comEnable))
  def __repr__(self):
    print 'ComName:'+self.comName
    print 'conSpeed'+str(self.comSpeed)
  def __str__(self):
    print 'ComName:'+self.comName
    print 'comSpeed:'+str(self.comSpeed)
    print 'comEnable:'+str(self.comEnable)    
    return ''
if __name__=='__main__':
  a = conf()
  a.LoadConf()
  print a