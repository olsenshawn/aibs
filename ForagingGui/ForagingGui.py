'''
Created on Oct 18, 2012

@author: derricw

This PyQt4 gui is designed to allow a user to select a background and foreground stimulus,
    then create a set of training criteria to train the mouse to find the correct stimulus.

'''

import os
import sys
from PyQt4 import QtCore as qt, QtGui
from PyQt4.QtCore import QObject as qo
from ForagingGuiLayout import Ui_MainWindow
from rewarddiaglayout import Ui_Form
from psychopy import visual
from ScriptGenerator import Script
import subprocess
from datetime import datetime
from aibs.Terrain import Terrain
try:
    from aibs.Reward import Reward
except Exception,e:
    print "Couldn't import reward:",e
from aibs.Core import *

 
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        """Constructor for main form."""
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Set up other forms
        self.rewarddiag = None
        
        # Set up some directories
        self.library = getdirectories()
        self.logDir = os.path.join(self.library,'BehaviorLogs')
        self.experimentslib = os.path.join(self.library,'Experiments')
        self.stimulilib = os.path.join(self.library,'Stimuli')
        self.terrainlib = os.path.join(self.library,'Terrain')
        self.scriptlog = os.path.join(self.library,'ScriptLog')
        
        # Set up some important variables
        self.params = {}
        self.bgSweep = {}
        self.fgSweep = {}
        self.terrainText = None #currently unused
        self.bgStimText = None
        self.fgStimText = None

        # Set up some file names to remember
        self.expfile,self.bgfile,self.fgfile,self.terrain = "","","",""

        # Set up some defaults (can be overwritten by config file)
        self.nidevice = 'Dev1'
        self.rewardport = 1
        self.rewardline = 1
        self.encodervsigchannel = 0
        self.encodervinchannel = 1
        self.backupdir = ''
        self.screen = 0
        self.monitor = 'testMonitor'
        self.protocol = ""
        self.stage = ""
        self.task = ""
        
        # Read config file
        try:
            f = open("foraging.cfg")
            for rl in f.readlines():
                line = rl.split(" = ",1)
                setattr(self,line[0], eval(line[1]))
            f.close()
        except:
            print "Could not read config file.  Using default values."
        
        # Add information to relevant fields
        self.ui.lineEdit_logDir.setText(self.logDir)
        self.ui.lineEdit_task.setText(self.task)
        self.ui.lineEdit_stage.setText(self.stage)
        self.ui.lineEdit_foragingProtocol.setText(self.protocol)
        
        # Ensure important directories exist, create them if not.
        checkDirs(self.logDir,self.library,self.stimulilib,self.experimentslib,self.terrainlib,self.scriptlog)

        # Connect signals
        self.ui.pushButton_loadExperiment.clicked.connect(self._loadExperiment)
        self.ui.pushButton_loadBGStimulus.clicked.connect(self._loadBG)
        self.ui.pushButton_loadFGStimulus.clicked.connect(self._loadFG)
        self.ui.pushButton_loadTerrain.clicked.connect(self._loadTerrain)
        self.ui.pushButton_run.clicked.connect(self._run)
        self.ui.pushButton_displayTerrain.clicked.connect(self._preview)
        self.ui.pushButton_rewardDiagnostic.clicked.connect(self._rewarddiag)

        self.ui.tableWidget_experiment.itemChanged.connect(self._experimentChanged)
        self.ui.tableWidget_BGStimulus.itemChanged.connect(self._BGStimulusChanged)
        self.ui.tableWidget_FGStimulus.itemChanged.connect(self._FGStimulusChanged)
        self.ui.tableWidget_terrain.itemChanged.connect(self._terrainChanged)

        self.ui.lineEdit_mouseid.textChanged.connect(self._mouseidChanged)

        #Load previous experiment
        self._loadLast()

    def _loadLast(self):
        """Loads the last experiment that was run."""
        try:
            f = open('last.dat','r+')
            lines = f.readlines()
            self.ui.lineEdit_mouseid.setText(lines[0].strip("\n"))
            self._loadExperiment(lines[1].strip("\n"))
            self._loadBG(lines[2].strip("\n"))
            self._loadFG(lines[3].strip("\n"))
            self._loadTerrain(lines[4].strip("\n"))
        except Exception, e:
            print "Could not load last experiment.",e

    def _saveLast(self):
        """Saves the last experiment that was run."""
        try:
            f = open('last.dat','w+')
            f.write(str(self.ui.lineEdit_mouseid.text())+"\n")
            f.write(self.expfile+"\n")
            f.write(self.bgfile+"\n")
            f.write(self.fgfile+"\n")
            f.write(self.terrainfile+"\n")
        except Exception, e:
            print "Couldn't save last.dat file:",e
        
    def _loadExperiment(self,fname=False):
        """Load an experiment file."""
        if fname is False:
            fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',self.experimentslib)
        self.expfile = fname
        try:
            f = open(fname, 'r')
            self.ui.tableWidget_experiment.clear()
            with f:        
                data = f.read()
                try:
                    exec(data)
                    index = 0
                    for k,v in params.iteritems():
                        self.ui.tableWidget_experiment.setItem(index,0,QtGui.QTableWidgetItem(str(k)))
                        self.ui.tableWidget_experiment.setItem(index,1,QtGui.QTableWidgetItem(str(v)))
                        index +=1
                    self.ui.tableWidget_experiment.sortByColumn(0,0)
                    _,tail = os.path.split(str(fname)) #get just the file name
                    self.ui.groupBox_experiment.setTitle(tail)
                except Exception, e:
                    print "Data is incorrectly formatted.",e
        except Exception, e:
            print "Couldn't open file:",e
    
    def _loadBG(self,fname=False):
        """Load a stimulus file as the background stimulus."""
        if fname is False:
            fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',self.stimulilib)
        self.bgfile = fname
        try:
            f = open(fname, 'r')
            self.ui.tableWidget_BGStimulus.clear()
            with f:        
                data = f.read()
                stim = data.split('PARAMETERS',1) #only care about parameters
                self.bgStimText = stim[0]
                try:
                    exec(stim[1]) #excupt only parameters
                    index = 0
                    for k,v in bgSweep.iteritems():
                        self.ui.tableWidget_BGStimulus.setItem(index,0,QtGui.QTableWidgetItem(str(k)))
                        self.ui.tableWidget_BGStimulus.setItem(index,1,QtGui.QTableWidgetItem(str(v)))
                        index +=1
                    self.ui.tableWidget_experiment.sortByColumn(0,0)
                    _,tail = os.path.split(str(fname)) #get just the file name
                    self.ui.groupBox_BGStimulus.setTitle(tail)
                except Exception, e:
                    print "Data is incorreclty formatted.",e
                    
        except Exception, e:
            print "Couldn't open file:",e
    
    def _loadFG(self,fname=False):
        """Load a stimulus file as the foreground stimulus."""
        if fname is False:
            fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',self.stimulilib)
        self.fgfile = fname
        try:
            f = open(fname, 'r')
            self.ui.tableWidget_FGStimulus.clear()
            with f:        
                data = f.read()
                stim = data.split('PARAMETERS',1) #only care about parameters
                self.fgStimText = stim[0]
                try:
                    exec(stim[1]) #execute only parameters
                    index = 0
                    for k,v in fgSweep.iteritems():
                        self.ui.tableWidget_FGStimulus.setItem(index,0,QtGui.QTableWidgetItem(str(k)))
                        self.ui.tableWidget_FGStimulus.setItem(index,1,QtGui.QTableWidgetItem(str(v)))
                        index +=1
                    self.ui.tableWidget_experiment.sortByColumn(0,0)
                    _,tail = os.path.split(str(fname)) #get just the file name
                    self.ui.groupBox_FGStimulus.setTitle(tail)
                except Exception, e:
                    print "Data is incorreclty formatted.",e
                    
        except Exception, e:
            print "Couldn't open file:",e
        
    def _loadTerrain(self, fname=False):
        """Load a terrain file as the terrain."""
        if fname is False:
            fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',self.terrainlib)
        self.terrainfile = fname
        try:
            f = open(fname, 'r')
            self.ui.tableWidget_terrain.clear()
            with f:        
                data = f.read()
                try:
                    exec(data) #execute only parameters
                    index = 0
                    for k,v in terrain.__dict__.iteritems():
                        self.ui.tableWidget_terrain.setItem(index,0,QtGui.QTableWidgetItem(str(k)))
                        self.ui.tableWidget_terrain.setItem(index,1,QtGui.QTableWidgetItem(str(v)))
                        index +=1
                    self.ui.tableWidget_experiment.sortByColumn(0,0) #sorts the dictionary
                    _,tail = os.path.split(str(fname)) #get just the file name
                    self.ui.groupBox_terrain.setTitle(tail) #sets the title
                except Exception, e:
                    print "Data is incorreclty formatted.",e
        except Exception, e:
            print "Couldn't open file:",e

    def _experimentChanged(self):
        """Experiment parameter changed callback. """
        current = str(self.ui.groupBox_experiment.title())
        if current[-1] is not "*":
            current +="*"
            self.ui.groupBox_experiment.setTitle(current)

    def _BGStimulusChanged(self):
        """BGStimulus sweep parameter changed callback."""
        current = str(self.ui.groupBox_BGStimulus.title())
        if current[-1] is not "*":
            current +="*"
            self.ui.groupBox_BGStimulus.setTitle(current)

    def _FGStimulusChanged(self):
        """FGStimulus sweep parameter changed callback."""
        current = str(self.ui.groupBox_FGStimulus.title())
        if current[-1] is not "*":
            current +="*"
            self.ui.groupBox_FGStimulus.setTitle(current)

    def _terrainChanged(self):
        """Terrain parameter changed callback."""
        current = str(self.ui.groupBox_terrain.title())
        if current[-1] is not "*":
            current +="*"
            self.ui.groupBox_terrain.setTitle(current)

    def _mouseidChanged(self):
        mouseid = str(self.ui.lineEdit_mouseid.text())
        self._checkSchedule() #should this be done here?
        self._getRecords(mouseid)

    def _checkSchedule(self):
        pass

    def _getRecords(self,mouseid):
        if len(mouseid)>3:
            try:
                records = os.listdir(self.backupdir)
                pruned = [r for r in records if mouseid in r]
                self._populateRecords(pruned)
            except Exception, e:
                print e
        else:
            self.ui.tableWidget_mouse.clear()

    def _populateRecords(self,files):
        for f in files:
            path = os.path.join(self.backupdir,f)
            print path

    def _run(self):
        """Runs an experiment."""
        print "Generating script..."
        script = self._generateScript()
        print "*"*80+"\n"
        print script.script
        print "*"*80+"\n"
        print "Checking script..."
        #self._checkScript()
        print "Saving script..."
        dt = datetime.now().strftime('%y%m%d%H%M%S')
        path = os.path.join(self.scriptlog,dt+"-"+str(self.ui.lineEdit_mouseid.text())+".py")
        script.save(path)
        print "Script saved at",path
        print "Running experiment..."
        execstring = "python "+path
        sp = subprocess.Popen(execstring.split())
        self._saveLast() #saves last experiment
        

        
    def _generateScript(self):
        """"Generates a Foraging script based on GUI input fields."""
        #CREATE SCRIPT
        script = Script()

        #ADD SOME PARAMS MANUALLY
        self.params['userid'] = ""
        self.params['mouseid'] = str(self.ui.lineEdit_mouseid.text())
        self.params['logdir'] = str(self.ui.lineEdit_logDir.text())
        self.params['task'] = str(self.ui.lineEdit_task.text())
        self.params['stage'] = str(self.ui.lineEdit_stage.text())
        self.params['protocol'] = str(self.ui.lineEdit_foragingProtocol.text())
        self.params['nidevice'] = self.nidevice
        self.params['rewardport'] = self.rewardport
        self.params['rewardline'] = self.rewardline
        self.params['encodervsigchannel'] = self.encodervsigchannel
        self.params['encodervinchannel'] = self.encodervinchannel
        self.params['backupdir'] = self.backupdir
        #ADD SOME PARAMS AUTOMATICALLY
        for i in range(self.ui.tableWidget_experiment.rowCount()):
            keystr = self.ui.tableWidget_experiment.item(i,0)
            valstr = self.ui.tableWidget_experiment.item(i,1)
            if (keystr is not None) and (keystr.text() not in ("",'',None)):
                try:
                    self.params[str(keystr.text())] = eval(str(valstr.text())) #not a string
                except:
                    self.params[str(keystr.text())] = str(valstr.text()) #string

        paramstr = "params = "+repr(self.params) + "\n" + "params['script']=__file__\n"
        script.add(paramstr)
        script.add()
        
        #ADD TERRAIN
        script.add("\nterrain = Terrain()")
        for i in range(self.ui.tableWidget_terrain.rowCount()):
            keystr = self.ui.tableWidget_terrain.item(i,0)
            valstr = self.ui.tableWidget_terrain.item(i,1)
            if (keystr is not None) and (keystr.text() not in ("",'',None)):
                terrainstr = 'terrain.'+keystr.text()+"="+valstr.text()
                script.add(terrainstr)

        #ADD WINDOW
        windowstr = "\nwindow = visual.Window(units='norm',monitor='"+ \
            self.monitor+"',fullscr=True,screen="+str(self.screen)+")"
        script.add(windowstr)

        #ADD BGSTIM
        script.add(self.bgStimText)

        #ADD BGSWEEPS
        script.add('bgSweep={}')
        for i in range(self.ui.tableWidget_BGStimulus.rowCount()):
            keystr = self.ui.tableWidget_BGStimulus.item(i,0)
            valstr = self.ui.tableWidget_BGStimulus.item(i,1)
            if (keystr is not None) and (keystr.text() not in ("",'',None)):
                    bgsweepstr = "bgSweep['"+keystr.text()+"']="+valstr.text()
                    script.add(bgsweepstr)        

        #ADD FGSTIM
        script.add(self.fgStimText)

        #ADD FGSWEEPS
        script.add('fgSweep={}')
        for i in range(self.ui.tableWidget_FGStimulus.rowCount()):
            keystr = self.ui.tableWidget_FGStimulus.item(i,0)
            valstr = self.ui.tableWidget_FGStimulus.item(i,1)
            if (keystr is not None) and (keystr.text() not in ("",'',None)):
                fgsweepstr = "fgSweep['"+keystr.text()+"']="+valstr.text()
                script.add(fgsweepstr)

        #CREATE FORAGING INSTANCE
        foragingstr = "g=Foraging(window=window,terrain=terrain," + \
            "params=params,bgStim=bgStim,bgFrame=bgFrame," + \
            "bgSweep=bgSweep,fgStim=fgStim)"
        script.add(foragingstr)

        #ADD RUN()
        script.add("g.run()")

        return script

    def _preview(self):
        """Generates a preview in a small window"""
        from psychopy import visual,event,monitors,misc

        window = visual.Window(monitor='testMonitor')
        width,height = window.size
        esctext = visual.TextStim(window,text='Press ESC or Q to exit...',
            pos=[-(width/2),(height/2-20)],color='red',units='pix',
            alignHoriz='left')

        if self.bgStimText is not None: exec(self.bgStimText)
        if self.fgStimText is not None: exec(self.fgStimText)
        ##TODO: SET PARAMETERS FOR FIRST SWEEP
        while True:
            try:
                if self.bgStimText is not None: bgStim.draw()
                if self.fgStimText is not None: fgStim.draw()
                esctext.draw()
                window.flip()
                for keys in event.getKeys(timeStamped=True):
                    if keys[0]in ['escape','q']:
                        window.close()
            except Exception, e:
                print "Exiting preview window...",e
                break
                      

    def _rewarddiag(self):
        if self.rewarddiag is None:
            self.rewarddiag = RewardDiagnostic()
        self.rewarddiag.show()


class RewardDiagnostic(QtGui.QWidget):
    """docstring for RewardDiagnostic"""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    
        self.ui.pushButton_dispense.clicked.connect(self._dispense)
        self.ui.pushButton_calibrate.clicked.connect(self._calibrate)
        
        #TODO: Get reward settings from config file
        try:
            reward = Reward()
        except Exception, e:
            print "Could not create reward object:",e

        ##TODO: Get/set calibration from/to file
        self.calibration = 1000 #uL/s

        # Read config file
        try:
            f = open("foraging.cfg")
            for rl in f.readlines():
                if "rewardcal" in rl:
                    line = rl.split("=")
                    setattr(self,line[0], eval(line[1]))
            f.close()
        except:
            print "Could not read config file.  Using default calibration values."

    def _dispense(self):
        """Dispenses using the selected settings."""
        reward.start()
        value = float(self.ui.lineEdit_volume.text())
        unit = str(self.ui.comboBox_unit.selectedItem())
        if unit is "uL":
            reward.rewardtime = value*self.calibration
            reward.reward()
        elif unit is "sec":
            reward.rewardtime = value
            reward.reward()
        reward.stop()

    def _calibrate(self):
        """Calibrates the dispense volume."""
        print "Calibrating dispense volume..."
        self._dispense()
        


if __name__ == "__main__":
    #sys.path.append('/home/derricw/GitHub')  #comment this in windows
    #sys.path.append(r'C:\Users\derricw\Documents\GitHub') #comment this in linux
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())