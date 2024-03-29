'''
Created on Oct 26, 2012

@author: derricw
#------------------------------------------------------------------------------ 
AnalogIODAQ.py
#------------------------------------------------------------------------------ 

Derric's wrapper for analog input/output* from an NIDAQ board using the PyDAQmx library.

Dependencies:
Python27
PyDAQmx (http://pypi.python.org/pypi/PyDAQmx)
numpy (http://www.scipy.org/Download)

Examples usage:
#------------------------------------------------------------------------------ 
    import time
    
    task=AnalogInput('Dev1',[0,1,2], 1000) #device 1, channels 0, 1, 2, buffer size 1000
    task.StartTask() #NI begins data collection
    
    #At any time after .StartTask() you can sample data from the current buffer which is
        #task.data
    
    task.accumulate = True #begin gathering data
    
    time.sleep(0.5) #collect .5 second of data
    
    task.accumulate = False #stop gathering data
    
    print task.dataArray[0] #print first sample in data array
    print len(task.dataArray) #number of samples taken while accumulate was true
    
    task.StopTask() #stops the task (can be restarted)
    task.ClearTask() #clears the task
#------------------------------------------------------------------------------ 

*output needs some work.  my NIDAQ board doesn't have analog output so I can't test it
'''
#----------------------------------------------------------------------- Imports
from PyDAQmx import Task
from PyDAQmx.DAQmxConstants import *
from PyDAQmx.DAQmxFunctions import *
from numpy import zeros, sin, arange, pi

#-------------------------------------------------------------- Config Functions
def GetDevices():
    """Gets all NIDAQ devices and returns a list of their names"""
    buffersize = 1024 #set max buffer size
    devicenames = " "*buffersize #build device string
    DAQmxGetSysDevNames(devicenames, buffersize) #fill string with names
    return devicenames.strip().strip('\x00').split(', ')  #strip off null char for each

def GetAIChannels(device):
    """ Returns a list of Analog Input Channels for the specified device """
    buffersize = 1024
    channels = " "*buffersize
    DAQmxGetDevAIPhysicalChans(device,channels,buffersize)
    return channels.strip().strip('\x00').split(', ')
    
def GetAOChannels(device):
    """ Returns a list of analog output channels for the specified device """
    buffersize = 1024
    channels = " "*buffersize
    DAQmxGetDevAOPhysicalChans(device,channels,buffersize)
    return channels.strip().strip('\x00').split(', ')

#-------------------------------------------------------------------- Input Task
class AnalogInput(Task):
    '''
    Gets analog input from NIDAQ device.  Tested using several buffer sizes and channels
        on a NI USB-6210.
        
    Default device is 1
    Default channel(s) is 0
    Default data buffer size is 500
        
    Set self.accumulate on/off to accumulate all data into self.dataArray
    
    '''
    def __init__(self,device = 'Dev1',channels = [0],bufferSize = 500,clockSpeed=10000.0):
        #construct task
        Task.__init__(self)
        
        #set up task properties
        self.bufferSize = bufferSize
        self.clockSpeed = clockSpeed
        self.channels = channels
        self.data = zeros((bufferSize,len(self.channels))) #data buffer
        self.dataArray = []
        self.accumulate = False
        
        #create dev str for various channels
        devStr = ""
        for channel in channels:
            devStr += str(device) + "/ai" + str(channel) + ","
        devStr = devStr[:-1]
        
        self.CreateAIVoltageChan(devStr,"",DAQmx_Val_RSE,-10.0,10.0,DAQmx_Val_Volts,None)
        
        ''' #Configures channel
        "Dev1/ai0"         #string for device and channel
        ""                 #handle name (not used in this example, only when using tasks without task class)
        DAQmx_Val_RSE      #Referenced Single-Ended
        -10.0              #min voltage
        10.0               #max voltage
        DAQmx_Val_Volts    #measure in volts
        None               #i have no idea what this does update:reserved for future use
        
        '''
        self.CfgSampClkTiming("",self.clockSpeed,DAQmx_Val_Rising,DAQmx_Val_ContSamps,self.bufferSize)
        
        ''' #Configures sampling
        ""                   #external clock (for example "/Dev1/PFIO") or "" for internal clock
        self.clockSpeed      #rate of internal clock or expected rate of external clock
        DAQmx_Val_Rising     #aquire on rising or falling edge of clock ticks
        DAQmx_Val_ContSamps  #continuous or finite samples
        self.bufferSize      #if continuous samples, this is the buffer size.  if finite, this is total sample size
        
        '''
        self.AutoRegisterEveryNSamplesEvent(DAQmx_Val_Acquired_Into_Buffer,self.bufferSize,0) #set up data buffer callback
        self.AutoRegisterDoneEvent(0) #set up task complete callback (unused since this class takes continuous samples)
    def EveryNCallback(self):
        read = int32()
        self.ReadAnalogF64(self.bufferSize,10.0,DAQmx_Val_Auto,self.data,(self.bufferSize*len(self.channels)),byref(read),None)
        
        ''' #Configures sampling
        self.bufferSize    #samples per channel
        10.0               #timeout
        DAQmx_Val_Auto     #fill mode alternatives are DAQmx_Val_GroupByChannel and DAQmx_Val_GroupByScanNumber
        self.data          #buffer
        1000               #size of buffer
        byref(read)        #no idea what this does can't find it in the documentation may not be needed
        None               #reserved
        '''
        if (self.accumulate == True):
            self.dataArray.extend(self.data.tolist())  #collect all data
        
    def DoneCallback(self, status):
        print "Status",status.value
        return 0 # The function should return an integer

#------------------------------------------------------------------- Output Task
class AnalogOutput(Task):
    '''
    Untested. The code below is for a single case.  Need to add support for input waveform,
        custom buffer size, etc.
    '''
    def __init__(self, device = 'Dev1', channels = [0]):
        Task.__init__(self)
        
        #create dev str for various channels
        devStr = ""
        for channel in channels:
            devStr += str(device) + "/ao" + str(channel) + ","
        devStr = devStr[:-1]
        #print devStr #for troubleshooting
        
        self.data = 9.95*sin(arange(1000, dtype=float64)*2*pi/1000) #create waveform of some sort
        self.CreateAOVoltageChan(devStr,"",-10.0,10.0,DAQmx_Val_Volts,None)
        self.CfgSampClkTiming("",1000.0,DAQmx_Val_Rising,DAQmx_Val_ContSamps,1000)
        self.AutoRegisterDoneEvent(0)
        self.WriteAnalogF64("",1000,0,-1,DAQmx_Val_GroupByChannel,self.data.ctypes.data,None,None)
    def DoneCallback(self,status):
        print "Status", status.value
        return 0

#-------------------------------------------------------------------------- Main
def main():
    pass
    
#----------------------------------------------------------------------- IF MAIN
if __name__ == "__main__":
    main()
