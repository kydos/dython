'''
Created on Apr 25, 2015

@author: Angelo Corsaro
'''

import dds
from dds.qos import *
import sys
from dds.dds import Subscriber

def showShapeType(s):
    if s != None:
        msg = "(color: %s, x: %d, y: %d, size: %d)\n" % (s.color, s.x, s.y, s.shapesize)        
        sys.stdout.write(msg)
        sys.stdout.flush()
        
def readData(dr):    
    samples = dr.read()
    while samples.hasNext():
        s = samples.next()            
        showShapeType(s.getData())
       
    
if __name__ == '__main__':
    t = dds.Topic("Circle", "org.omg.dds.demo.ShapeType")    
    s = SubscriberQos()
    sqos = s.withPolicy(Partition("demo@vortex.com"))
    s = Subscriber(sqos)
    dr = dds.Reader(topic = t, sub = s)
    dr.onDataAvailable = readData 
    