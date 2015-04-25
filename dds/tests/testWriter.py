'''
Created on Apr 24, 2015

@author: Angelo Corsaro
'''
import dds
from org.omg.dds.demo import ShapeType
import time
import sys

if __name__ == '__main__':
    t = dds.Topic("Circle", "org.omg.dds.demo.ShapeType")
    dw = dds.Writer(t)
    xs = [10*i for i in range(10, 40)]    
    size = 60
    shapes = [ShapeType("RED", x, x, size) for x in xs]
         
    for s in shapes:
        sys.stdout.write("<") 
        sys.stdout.flush
        dw.write(s)
        sys.stdout.write(">")
        sys.stdout.flush 
        time.sleep(1)
        