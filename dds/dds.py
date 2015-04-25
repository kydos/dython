'''
Created on Apr 24, 2015

@author: Angelo Corsaro
'''

from java.lang import System as JSystem
from java.lang import Class as JClass
from java.lang import Thread as JThread
from org.omg.dds.core import ServiceEnvironment   
from org.omg.dds.domain import DomainParticipantFactory
from org.omg.dds.sub import DataReaderListener  as JDataReaderListener 
from dython.bit import KDython
import cPickle
# from org.omg.dython.sub import InstanceState


     
class Runtime:
    runtimeImpl = None
    def __init__(self, ddsImpl = "com.prismtech.cafe.core.ServiceEnvironmentImpl"):        
        JSystem.setProperty(ServiceEnvironment.IMPLEMENTATION_CLASS_NAME_PROPERTY, 
                            ddsImpl);
        self.env = ServiceEnvironment.createInstance(JThread.currentThread().getContextClassLoader())
        self.pf = self.env.getSPI().getPolicyFactory()
        self.dpf = DomainParticipantFactory.getInstance(self.env)        
        self.defaultDP = self.dpf.createParticipant(0)
        self.defaultP = self.defaultDP.createPublisher()
        self.defaultS = self.defaultDP.createSubscriber()
        self.builtInTopicType = "dython.bit.KDython"
        # self.allStatusKind = self.env.getSPI().allStatusKinds()
    

def runtime():
    if (Runtime.runtimeImpl == None):
        Runtime.runtimeImpl = Runtime()
    return Runtime.runtimeImpl
        

def Participant(did):
    dpf = runtime.dpf
    return dpf.createParticipant(did)
    
def Publisher(qos = None, dp = runtime().defaultDP):
    if qos == None:
        return dp.createPublisher()
    else:
        return dp.createPublisher(qos)

def Subscriber(qos = None, dp = runtime().defaultDP):
    if qos == None:
        return dp.createSubscriber()
    else:
        return dp.createSubscriber(qos)

    
def Topic(name, ttype = runtime().builtInTopicType, qos = None, dp = runtime().defaultDP):    
    tcls = JClass.forName(ttype)
    if qos == None:
        return dp.createTopic(name, tcls)
    else:
        return dp.createTopic(name, tcls, qos)

def Writer(topic, qos = None, pub = runtime().defaultP):    
    if qos == None:
        return  pub.createDataWriter(topic)
    else:
        return pub.createDataWriter(topic, qos)   

class ReaderListener(JDataReaderListener):
    def __init__(self, reader):
        self.dr = reader

    def onRequestedDeadlineMissed(self, e):
        if self.dr.onRequestedDeadlineMissed != None:
            self.dr.onRequestedDeadlineMissed(e)

    def onRequestedIncompatibleQos(self, e):
        if self.dr.onRequestedIncompatibleQos != None:
            self.dr.onRequestedIncompatibleQos(e)


    def onSampleRejected(self, e):
        if self.dr.onSampleRejected != None:
            self.dr.onSampleRejected(e)
            
    def onLivelinessChanged(self, e):
        if self.dr.onLivelinessChanged != None:
            self.dr.onLivelinessChanged(e)
      


    def onDataAvailable(self, e):
        if self.dr.onDataAvailable != None:
            # Pass the DataReader
            self.dr.onDataAvailable(e.getSource())
            
    def onSubscriptionMatched(self, e):
        if self.dr.onSubscriptionMatched != None:
            self.dr.onSubscriptionMatched(e)
            
            
    def onSampleLost(self, e):
        if self.dr.onSampleLost != None:
            self.dr.onSampleLost(e)
    
    

class Reader:
    def __init__(self, topic, qos = None, sub = runtime().defaultS):        
        if qos == None:
            self.dr = sub.createDataReader(topic)            
        else:
            self.dr =  sub.createDataReader(topic, qos)
                    
        self.onDataAvailable = None  
        self.onRequestedDeadlineMissed = None 
        self.onRequestedIncompatibleQos = None
        self.onSampleRejected = None
        self.onLivelinessChanged = None
        self.onDataAvailable = None
        self.onSubscriptionMatched = None
        self.onSampleLost = None
        self.dr.setListener(ReaderListener(self))
    
    def reader(self):
        return self.dr
             
    def read(self):
        return self.dr.read()
    
    def take(self):
        return self.dr.take()
            
        
        
def encode(pyo): 
    k = "None"
    if hasattr(pyo, 'key'):
        k = pyo.key
    s = cPickle.dumps(pyo)
    return KDython(k, s)
    
def decode(dyo):
    return cPickle.loads(dyo.value)    

            