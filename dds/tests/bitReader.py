'''
Created on Apr 26, 2015

@author: kydos
'''

import dds
import sys
    
def readData(dr):    
    sys.stdout.write("-------------------------------\n")
    sys.stdout.flush()
    samples = dr.read()
    while samples.hasNext():
        s = samples.next()            
        ds = dds.decode(s.getData())
        sys.stdout.write(str(ds))
        sys.stdout.write("\n")
        
    
if __name__ == '__main__':
    t = dds.Topic("DeviceStatus")
    dr = dds.Reader(t)
    dr.onDataAvailable = readData 