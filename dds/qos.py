'''
Created on Apr 25, 2015

@author: kydos
'''
import dds
def PublisherQos():
    return dds.runtime().defaultDP.getDefaultPublisherQos()

def SubscriberQos():
    return dds.runtime().defaultDP.getDefaultSubscriberQos()

def TopicQos():
    return dds.runtime().defaultDP.getDefaultTopicQoS()

def ReaderQos():
    return dds.runtime().defaultS.getDefaultDataReaderQoS()

def WriterQos():
    return dds.runtime().defaultP.getDefaultDataWriterQoS()

def Partition(names):
    return dds.runtime().pf.Partition().withName(names)

class ReliabilityKind(object):
    def __init__(self):
        self.pf = dds.runtime().pf
        
    def BestEffort(self):
        return self.pf.Reliability().withBestEffort()
        
    def Reliable(self):
        return self.pf.Reliability().withReliable()

        
def Reliability(kind = ReliabilityKind()):
    return kind

class DurabilityKind(object):
    def __init__(self):
        self.pf = dds.runtime().pf
        
    def Volatile(self):
        return self.pf.Durability().withVolatile()
        
    def TransientLocal(self):
        return self.pf.Durability().withTransientLocal()

    def Transient(self):
        return self.pf.Durability().withTransient()
        
    def Persistent(self):
        return self.pf.Durability().withPersistent()
        
def Durability(kind = DurabilityKind()):
    return kind


class HistoryKind(object):
    def __init__(self):
        self.pf = dds.runtime().pf
    
    def KeepLast(self, n):
        return self.pf.History().withKeepLast(n)
        
    def KeepAll(self, n):
        return self.pf.History().withKeepAll()
    
def History(kind = HistoryKind()):
    return kind
    
    