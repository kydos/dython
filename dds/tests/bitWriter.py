'''
Created on Apr 26, 2015

@author: kydos
'''
import dds
from dds.tests.status import DeviceStatus
import sys
import time 

if __name__ == '__main__':
    topic = dds.Topic("DeviceStatus")
    writer = dds.Writer(topic) 
    
    for i in range(1, 100):
        sys.stdout.write(".")
        sys.stdout.flush()
        s = DeviceStatus("101", i, True)
        writer.write(dds.encode(s))       
        time.sleep(1)
 
        
    