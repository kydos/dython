'''
Created on Apr 25, 2015

@author: kydos
'''
# from dython.dds import Topic, Reader
import dds
import sys

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
    dr = dds.Reader(t)
    dr.onDataAvailable = readData 