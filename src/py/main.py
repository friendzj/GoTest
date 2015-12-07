# -*- coding: UTF-8 -*- 
from protocol import *
import SerialOpt
import time
import conf
import logging 

def RobotRun():
  import MotoCtrl
  ret=MotoCtrl.AddMotoCtrl((1,1,1),(2,2,2),(3,3,3),(4,4,4)) 
  retDat = MotoCtrl.SerialPkt();
  print len(retDat)
  
def Main():
  logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='robot.log',
                filemode='w')
  console = logging.StreamHandler()
  console.setLevel(logging.INFO)
  formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
  console.setFormatter(formatter)
  logging.getLogger('').addHandler(console)
  
  logging.info("SYSTEM START")
  RobotCon = conf.conf()
  RobotCon.LoadConf()
  ser = SerialOpt.SerOpt(RobotCon.comName,RobotCon.comSpeed) 
  
if __name__=='__main__':
  Main()