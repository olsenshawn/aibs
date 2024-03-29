"""
author: derricw
2/4/13

core.py

"""
import itertools

def buildSweepTable(sweep, runs = 1, blanksweeps = 0):
    """ Builds an ordered table of every permutation of input dictionary of tuples. """
    sweepcount = 1
    dimensions = len(sweep)
    dimarray = []
    dimnames = []
    
    for key,values in sweep.iteritems():
        sweepcount *= len(values[0]) # get number of sweeps
    
    for d in range(dimensions):
        for k,v in sweep.iteritems():
            if v[1] == d:
                dimarray.append(len(v[0])) # get ordered dimenstion array
                dimnames.append(k) # get ordered name array
                
    dimlist = [sweep[k][0] for k in dimnames] # get ordered value array
    sweeptable = list(itertools.product(*dimlist)) # get full ordered table
    sweeporder = range(sweepcount)
    if blanksweeps is not 0:
    	segments = [sweeporder[i:i+blanksweeps] for i in range(0, len(sweeporder), blanksweeps)]
    	sweeporder = []
    	for x in segments:
    		for y in x:
    			sweeporder.append(y)
    		if len(x) == blanksweeps:
    			sweeporder.append(-1)
    return sweeptable, sweeporder*runs, dimnames
    
def getMonitorInfo(monitor):
    """ Creates a dictionary fo relevent monitor information. """
    info = {}
    info['gamm'] = monitor.getGamma()
    info['gammagrid'] = monitor.getGammaGrid().tolist()
    info['distancecm'] = monitor.getDistance()
    info['sizepix'] = monitor.getSizePix()
    info['widthcm'] = monitor.getWidth()
    info['calibrationdate'] = str(monitor.getCalibDate())
    info['name'] = monitor.name
    return info
    
def getSweepFrames(sweeporder,sweeptime,preexpsec,postexpsec,postsweepsec):
    """ Gets the sweep frame (start,stop) list """
    sweepframelist = []
    frame = int(preexpsec*60)
    for i in range(len(sweeporder)):
        frames = (frame, frame+int(60*sweeptime)-1)
        sweepframelist.append(frames)
        frame = frames[1] + 60*postsweepsec +1
    return sweepframelist
    
class prettyfloat(float):
    """ Prettier format for float text output. """
    def __repr__(self):
        return "%0.4f" % self

def setpriority():
    """ Set The Priority of a Windows Process to highest priority. """
    import psutil,os
    p = psutil.Process(os.getpid())
    #print "Current process priority is:",str(p.nice)
    p.set_nice(psutil.HIGH_PRIORITY_CLASS)
    #print "Set process priority to:",str(psutil.REALTIME_PRIORITY_CLASS)
    
def getdirectories():
    import sys
    import os
    if 'linux' in sys.platform:
        topdir = os.path.expanduser('~/Aibstim/')
    else:
        topdir = 'C:\\AibStim\\'
    return topdir
  
def checkDirs(*args):
    """ Checks to see if any of the directories exist.  Creates them if they don't"""
    import os
    for arg in [x for x in args if x is not None]:
        if not os.path.isdir(arg):
            os.makedirs(arg)
            print "Creating new path:",arg

if __name__ == "__main__":
    d = getdirectories()
    print d
    import sys
    #sys.path.append('/home/derricw/GitHub/aibs')
    print sys.path
    