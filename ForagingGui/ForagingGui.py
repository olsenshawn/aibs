'''
Created on Oct 18, 2012

@author: derricw
'''

import os
import sys
from PyQt4 import QtCore as qt, QtGui
from PyQt4.QtCore import QObject as qo
from ForagingGuiLayout import Ui_MainWindow
from psychopy import visual
from ScriptGenerator import Script
import subprocess

 
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Set up some directories
        self.library = getdirectories()
        self.logDir = os.path.join(self.library,'BehaviorLogs')
        self.experimentslib = os.path.join(self.library,'Experiments')
        self.stimulilib = os.path.join(self.library,'Stimuli')
        self.terrainlib = os.path.join(self.library,'Terrain')
        self.scriptlog = os.path.join(self.library,'ScriptLog')

        ''' Delete if above works on windows
        self.library = "C:\\AibsStim\\"
        self.logDir = "C:\\BehaviorLogs\\"
        self.experiments = "C:\\AibsStim\\Experiments\\"
        self.stimuli = "C:\\AibsStim\\Stimuli\\"
        self.terrain = "C:\\AibsStim\\Terrain\\"
        '''
        
        # Set up some important variables
        self.params = {}
        self.bgSweep = {}
        self.fgSweep = {}
        self.terrain = None
        self.bgStimText = None
        self.fgStimText = None
        
        # Read config file
        try:
            f = open("foraging.cfg")
            for rl in f.readlines():
                line = rl.split("=")
                setattr(self,line[0], line[1])
            f.close()
        except:
            print "Could not read config file.  Using default values."
        
        # Add information to relevant fields
        self.ui.lineEdit_logDir.setText(self.logDir)
        
        # Ensure important directories exist, create them if not.
        checkDirs(self.logDir,self.library,self.stimulilib,self.experimentslib,self.terrainlib,self.scriptlog)
        
        # Connect signals
        qo.connect(self.ui.pushButton_loadExperiment,qt.SIGNAL("clicked()"), self._loadExperiment)
        qo.connect(self.ui.pushButton_loadBGStimulus,qt.SIGNAL("clicked()"), self._loadBG)
        qo.connect(self.ui.pushButton_loadFGStimulus,qt.SIGNAL("clicked()"), self._loadFG)
        qo.connect(self.ui.pushButton_loadTerrain,qt.SIGNAL("clicked()"), self._loadTerrain)
        qo.connect(self.ui.pushButton_run,qt.SIGNAL("clicked()"), self._run)
        
        ''' Examples of connecting signals (assumes your form has a pushButton, lineEdit, and textEdit)
        #QtCore.QObject.connect(self.ui.pushButton, QtCore.SIGNAL("clicked()"), self.ui.textEdit.clear )
        #QtCore.QObject.connect(self.ui.lineEdit, QtCore.SIGNAL("returnPressed()"), self.add_entry)
        '''
        ''' Example of signal callback (performed when return is pressed on lineEdit, see above)
    def add_entry(self):
        self.ui.lineEdit.selectAll()
        self.ui.lineEdit.cut()
        self.ui.textEdit.append("")
        self.ui.textEdit.paste()
        '''
        
    def _loadExperiment(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',self.experimentslib)
        try:
            f = open(fname, 'r')
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
                except Exception, e:
                    print "Data is incorrectly formatted.",e
        except Exception, e:
            print "Couldn't open file:",e

    
    def _loadBG(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',self.stimulilib)
        try:
            f = open(fname, 'r')
            with f:        
                data = f.read()
                stim = data.split('PARAMETERS',1) #only care about parameters
                try:
                    exec(stim[1]) #excupt only parameters
                    index = 0
                    for k,v in bgSweep.iteritems():
                        self.ui.tableWidget_bgStimulus.setItem(index,0,QtGui.QTableWidgetItem(str(k)))
                        self.ui.tableWidget_bgStimulus.setItem(index,1,QtGui.QTableWidgetItem(str(v)))
                        index +=1
                    self.ui.tableWidget_experiment.sortByColumn(0,0)
                except Exception, e:
                    print "Data is incorreclty formatted.",e
                    
        except Exception, e:
            print "Couldn't open file:",e
    
    def _loadFG(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',self.stimulilib)
        try:
            f = open(fname, 'r')
            with f:        
                data = f.read()
                stim = data.split('PARAMETERS',1) #only care about parameters
                try:
                    exec(stim[1]) #execute only parameters
                    index = 0
                    for k,v in fgSweep.iteritems():
                        self.ui.tableWidget_fgStimulus.setItem(index,0,QtGui.QTableWidgetItem(str(k)))
                        self.ui.tableWidget_fgStimulus.setItem(index,1,QtGui.QTableWidgetItem(str(v)))
                        index +=1
                    self.ui.tableWidget_experiment.sortByColumn(0,0)
                except Exception, e:
                    print "Data is incorreclty formatted.",e
                    
        except Exception, e:
            print "Couldn't open file:",e
        
    def _loadTerrain(self):
        fname = QtGui.QFileDialog.getOpenFileName(self, 'Open file',self.terrainlib)
        try:
            f = open(fname, 'r')
            with f:        
                data = f.read()
                try:
                    exec(data) #execute only parameters
                    index = 0
                    for k,v in terrain.__dict__.iteritems():
                        self.ui.tableWidget_terrainParams.setItem(index,0,QtGui.QTableWidgetItem(str(k)))
                        self.ui.tableWidget_terrainParams.setItem(index,1,QtGui.QTableWidgetItem(str(v)))
                        index +=1
                    self.ui.tableWidget_experiment.sortByColumn(0,0)
                except Exception, e:
                    print "Data is incorreclty formatted.",e
        except Exception, e:
            print "Couldn't open file:",e
    
    def _run(self):
        print "Generating script..."
        _generateScript()
        print "Running experiment"
        
    def _generateScript(self):
        #CREATE SCRIPT
        script = Script()
        #ADD PARAMS
        self.params['mouseid'] = self.ui.lineEdit_mouseid.text
        self.params['logDir'] = self.ui.lineEdit_logDir.text
        self.params['task'] = self.ui.lineEdit_task.text
        self.params['stage'] = self.ui.lineEdit_stage.text
        self.params['protocol'] = self.ui.lineEdit_foragingProtocol.text
        self.params['nidevice'] = self.nidevice
        self.params['rewardport'] = self.rewardport
        self.params['rewardline'] = self.rewardline
        self.params['encodervsigchannel'] = self.encodervsigchannel
        self.params['encodervinchannel'] = self.encodervinchannel
        self.params['backupdir'] = self.backupdir
        
        paramstring = "params = "+repr(self.params)
        script.add(paramstring)
        print script.script


if __name__ == "__main__":
    #sys.path.append('/home/derricw/GitHub')  #get rid of this when I'm coding in windows
    sys.path.append(r'C:\Users\derricw\Documents\GitHub')
    from aibs.Terrain import Terrain
    from aibs.Core import *
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())