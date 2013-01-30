# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Jan 29 17:37:27 2013
#      by: PyQt4 UI code generator 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(885, 847)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Foraging", None, QtGui.QApplication.UnicodeUTF8))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.groupBox_mouse = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_mouse.setGeometry(QtCore.QRect(20, 10, 411, 371))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_mouse.setFont(font)
        self.groupBox_mouse.setTitle(QtGui.QApplication.translate("MainWindow", "Mouse Info", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_mouse.setObjectName(_fromUtf8("groupBox_mouse"))
        self.pushButton_loadMouse = QtGui.QPushButton(self.groupBox_mouse)
        self.pushButton_loadMouse.setGeometry(QtCore.QRect(240, 0, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_loadMouse.setFont(font)
        self.pushButton_loadMouse.setText(QtGui.QApplication.translate("MainWindow", "Load Mouse", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_loadMouse.setObjectName(_fromUtf8("pushButton_loadMouse"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_mouse)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton_sessionPerformance = QtGui.QPushButton(self.groupBox_mouse)
        self.pushButton_sessionPerformance.setGeometry(QtCore.QRect(20, 310, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_sessionPerformance.setFont(font)
        self.pushButton_sessionPerformance.setText(QtGui.QApplication.translate("MainWindow", "Session Performance", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_sessionPerformance.setObjectName(_fromUtf8("pushButton_sessionPerformance"))
        self.pushButton_lifetimePerformance = QtGui.QPushButton(self.groupBox_mouse)
        self.pushButton_lifetimePerformance.setGeometry(QtCore.QRect(210, 310, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_lifetimePerformance.setFont(font)
        self.pushButton_lifetimePerformance.setText(QtGui.QApplication.translate("MainWindow", "Lifetime Performance", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_lifetimePerformance.setObjectName(_fromUtf8("pushButton_lifetimePerformance"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_mouse)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 50, 391, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Logs", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.tableWidget_mouse = QtGui.QTableWidget(self.groupBox_4)
        self.tableWidget_mouse.setGeometry(QtCore.QRect(10, 20, 371, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_mouse.setFont(font)
        self.tableWidget_mouse.setRowCount(10)
        self.tableWidget_mouse.setColumnCount(2)
        self.tableWidget_mouse.setObjectName(_fromUtf8("tableWidget_mouse"))
        self.tableWidget_mouse.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_mouse.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_mouse.horizontalHeader().setMinimumSectionSize(26)
        self.groupBox_bgStimulus = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_bgStimulus.setGeometry(QtCore.QRect(20, 390, 411, 401))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_bgStimulus.setFont(font)
        self.groupBox_bgStimulus.setTitle(QtGui.QApplication.translate("MainWindow", "Background Stimulus", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_bgStimulus.setObjectName(_fromUtf8("groupBox_bgStimulus"))
        self.pushButton_loadStimulus = QtGui.QPushButton(self.groupBox_bgStimulus)
        self.pushButton_loadStimulus.setGeometry(QtCore.QRect(230, 0, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_loadStimulus.setFont(font)
        self.pushButton_loadStimulus.setText(QtGui.QApplication.translate("MainWindow", "Load Stimulus", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_loadStimulus.setObjectName(_fromUtf8("pushButton_loadStimulus"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_bgStimulus)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 40, 391, 331))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.tableWidget_bgStimulus = QtGui.QTableWidget(self.groupBox_3)
        self.tableWidget_bgStimulus.setGeometry(QtCore.QRect(10, 20, 371, 291))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_bgStimulus.setFont(font)
        self.tableWidget_bgStimulus.setRowCount(10)
        self.tableWidget_bgStimulus.setColumnCount(2)
        self.tableWidget_bgStimulus.setObjectName(_fromUtf8("tableWidget_bgStimulus"))
        self.tableWidget_bgStimulus.horizontalHeader().setDefaultSectionSize(150)
        self.groupBox_foraging = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_foraging.setGeometry(QtCore.QRect(440, 10, 431, 781))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_foraging.setFont(font)
        self.groupBox_foraging.setTitle(QtGui.QApplication.translate("MainWindow", "Foraging", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_foraging.setObjectName(_fromUtf8("groupBox_foraging"))
        self.lineEdit_userId = QtGui.QLineEdit(self.groupBox_foraging)
        self.lineEdit_userId.setGeometry(QtCore.QRect(82, 30, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_userId.setFont(font)
        self.lineEdit_userId.setObjectName(_fromUtf8("lineEdit_userId"))
        self.pushButton_run = QtGui.QPushButton(self.groupBox_foraging)
        self.pushButton_run.setGeometry(QtCore.QRect(260, 0, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_run.setFont(font)
        self.pushButton_run.setStyleSheet(_fromUtf8("background-color: rgb(255, 170, 0);"))
        self.pushButton_run.setText(QtGui.QApplication.translate("MainWindow", "RUN", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_run.setObjectName(_fromUtf8("pushButton_run"))
        self.label = QtGui.QLabel(self.groupBox_foraging)
        self.label.setGeometry(QtCore.QRect(20, 30, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "User ID:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox_foraging)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 46, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Log dir:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_logDir = QtGui.QLineEdit(self.groupBox_foraging)
        self.lineEdit_logDir.setGeometry(QtCore.QRect(80, 70, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_logDir.setFont(font)
        self.lineEdit_logDir.setText(QtGui.QApplication.translate("MainWindow", "C:\\", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_logDir.setObjectName(_fromUtf8("lineEdit_logDir"))
        self.label_3 = QtGui.QLabel(self.groupBox_foraging)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Task:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_task = QtGui.QLineEdit(self.groupBox_foraging)
        self.lineEdit_task.setGeometry(QtCore.QRect(80, 110, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_task.setFont(font)
        self.lineEdit_task.setObjectName(_fromUtf8("lineEdit_task"))
        self.lineEdit_stage = QtGui.QLineEdit(self.groupBox_foraging)
        self.lineEdit_stage.setGeometry(QtCore.QRect(80, 150, 321, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_stage.setFont(font)
        self.lineEdit_stage.setObjectName(_fromUtf8("lineEdit_stage"))
        self.label_4 = QtGui.QLabel(self.groupBox_foraging)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Stage:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_loadProtocol = QtGui.QPushButton(self.groupBox_foraging)
        self.pushButton_loadProtocol.setGeometry(QtCore.QRect(260, 190, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_loadProtocol.setFont(font)
        self.pushButton_loadProtocol.setText(QtGui.QApplication.translate("MainWindow", "Load Protocol", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_loadProtocol.setObjectName(_fromUtf8("pushButton_loadProtocol"))
        self.pushButton_protocolEditor = QtGui.QPushButton(self.groupBox_foraging)
        self.pushButton_protocolEditor.setGeometry(QtCore.QRect(100, 190, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_protocolEditor.setFont(font)
        self.pushButton_protocolEditor.setText(QtGui.QApplication.translate("MainWindow", "Protocol Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_protocolEditor.setObjectName(_fromUtf8("pushButton_protocolEditor"))
        self.label_5 = QtGui.QLabel(self.groupBox_foraging)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Foraging Protocol:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_foragingProtocol = QtGui.QLineEdit(self.groupBox_foraging)
        self.lineEdit_foragingProtocol.setGeometry(QtCore.QRect(140, 250, 261, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_foragingProtocol.setFont(font)
        self.lineEdit_foragingProtocol.setObjectName(_fromUtf8("lineEdit_foragingProtocol"))
        self.pushButton_displayTerrain = QtGui.QPushButton(self.groupBox_foraging)
        self.pushButton_displayTerrain.setGeometry(QtCore.QRect(150, 710, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_displayTerrain.setFont(font)
        self.pushButton_displayTerrain.setText(QtGui.QApplication.translate("MainWindow", "Display Terrain", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_displayTerrain.setObjectName(_fromUtf8("pushButton_displayTerrain"))
        self.pushButton_rewardDiagnostic = QtGui.QPushButton(self.groupBox_foraging)
        self.pushButton_rewardDiagnostic.setGeometry(QtCore.QRect(290, 710, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_rewardDiagnostic.setFont(font)
        self.pushButton_rewardDiagnostic.setText(QtGui.QApplication.translate("MainWindow", "Reward Diagnostic", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_rewardDiagnostic.setObjectName(_fromUtf8("pushButton_rewardDiagnostic"))
        self.pushButton_TBD = QtGui.QPushButton(self.groupBox_foraging)
        self.pushButton_TBD.setGeometry(QtCore.QRect(10, 710, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_TBD.setFont(font)
        self.pushButton_TBD.setText(QtGui.QApplication.translate("MainWindow", "TBD", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_TBD.setObjectName(_fromUtf8("pushButton_TBD"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_foraging)
        self.groupBox.setGeometry(QtCore.QRect(10, 490, 411, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Stimulus Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tableWidget_fgStimulus = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_fgStimulus.setGeometry(QtCore.QRect(10, 20, 391, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.tableWidget_fgStimulus.setFont(font)
        self.tableWidget_fgStimulus.setRowCount(10)
        self.tableWidget_fgStimulus.setColumnCount(2)
        self.tableWidget_fgStimulus.setObjectName(_fromUtf8("tableWidget_fgStimulus"))
        self.tableWidget_fgStimulus.horizontalHeader().setDefaultSectionSize(160)
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox_foraging)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 280, 411, 211))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Terrain Parameters", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tableWidget_terrainParams = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidget_terrainParams.setGeometry(QtCore.QRect(10, 20, 391, 181))
        self.tableWidget_terrainParams.setRowCount(10)
        self.tableWidget_terrainParams.setColumnCount(2)
        self.tableWidget_terrainParams.setObjectName(_fromUtf8("tableWidget_terrainParams"))
        self.tableWidget_terrainParams.horizontalHeader().setDefaultSectionSize(160)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 885, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFiles = QtGui.QMenu(self.menuBar)
        self.menuFiles.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFiles.setObjectName(_fromUtf8("menuFiles"))
        self.menuHelp = QtGui.QMenu(self.menuBar)
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFiles.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass

