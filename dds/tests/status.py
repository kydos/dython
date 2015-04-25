'''
Created on Apr 26, 2015

@author: kydos
'''
class DeviceStatus(object):
    def __init__(self, did, temp, on):
        self.key = did
        self.temp = temp
        self.on = on            
    
    def __str__(self, *args, **kwargs):
        return "{ key = %s, temp = %s, on = %s }" % (self.key, self.temp, self.on)