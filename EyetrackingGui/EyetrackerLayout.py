# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu May 02 16:05:06 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(788, 689)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_7 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.groupBox_camera = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_camera.setObjectName(_fromUtf8("groupBox_camera"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_camera)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_camera_hue = QtGui.QLabel(self.groupBox_camera)
        self.label_camera_hue.setObjectName(_fromUtf8("label_camera_hue"))
        self.gridLayout_2.addWidget(self.label_camera_hue, 0, 0, 1, 1)
        self.horizontalSlider_camera_hue = QtGui.QSlider(self.groupBox_camera)
        self.horizontalSlider_camera_hue.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_camera_hue.setObjectName(_fromUtf8("horizontalSlider_camera_hue"))
        self.gridLayout_2.addWidget(self.horizontalSlider_camera_hue, 0, 1, 1, 1)
        self.label_camera_hue_value = QtGui.QLabel(self.groupBox_camera)
        self.label_camera_hue_value.setObjectName(_fromUtf8("label_camera_hue_value"))
        self.gridLayout_2.addWidget(self.label_camera_hue_value, 0, 2, 1, 1)
        self.label_camera_saturation = QtGui.QLabel(self.groupBox_camera)
        self.label_camera_saturation.setObjectName(_fromUtf8("label_camera_saturation"))
        self.gridLayout_2.addWidget(self.label_camera_saturation, 1, 0, 1, 1)
        self.horizontalSlider_camera_saturation = QtGui.QSlider(self.groupBox_camera)
        self.horizontalSlider_camera_saturation.setMaximum(150)
        self.horizontalSlider_camera_saturation.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_camera_saturation.setObjectName(_fromUtf8("horizontalSlider_camera_saturation"))
        self.gridLayout_2.addWidget(self.horizontalSlider_camera_saturation, 1, 1, 1, 1)
        self.label_camera_saturation_value = QtGui.QLabel(self.groupBox_camera)
        self.label_camera_saturation_value.setObjectName(_fromUtf8("label_camera_saturation_value"))
        self.gridLayout_2.addWidget(self.label_camera_saturation_value, 1, 2, 1, 1)
        self.label_camera_brightness = QtGui.QLabel(self.groupBox_camera)
        self.label_camera_brightness.setObjectName(_fromUtf8("label_camera_brightness"))
        self.gridLayout_2.addWidget(self.label_camera_brightness, 2, 0, 1, 1)
        self.horizontalSlider_camera_brightness = QtGui.QSlider(self.groupBox_camera)
        self.horizontalSlider_camera_brightness.setMinimum(0)
        self.horizontalSlider_camera_brightness.setMaximum(200)
        self.horizontalSlider_camera_brightness.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_camera_brightness.setObjectName(_fromUtf8("horizontalSlider_camera_brightness"))
        self.gridLayout_2.addWidget(self.horizontalSlider_camera_brightness, 2, 1, 1, 1)
        self.label_camera_brightness_value = QtGui.QLabel(self.groupBox_camera)
        self.label_camera_brightness_value.setObjectName(_fromUtf8("label_camera_brightness_value"))
        self.gridLayout_2.addWidget(self.label_camera_brightness_value, 2, 2, 1, 1)
        self.label_camera_gain = QtGui.QLabel(self.groupBox_camera)
        self.label_camera_gain.setObjectName(_fromUtf8("label_camera_gain"))
        self.gridLayout_2.addWidget(self.label_camera_gain, 3, 0, 1, 1)
        self.horizontalSlider_camera_gain = QtGui.QSlider(self.groupBox_camera)
        self.horizontalSlider_camera_gain.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_camera_gain.setObjectName(_fromUtf8("horizontalSlider_camera_gain"))
        self.gridLayout_2.addWidget(self.horizontalSlider_camera_gain, 3, 1, 1, 1)
        self.label_camera_gain_value = QtGui.QLabel(self.groupBox_camera)
        self.label_camera_gain_value.setObjectName(_fromUtf8("label_camera_gain_value"))
        self.gridLayout_2.addWidget(self.label_camera_gain_value, 3, 2, 1, 1)
        self.label_camera_contrast = QtGui.QLabel(self.groupBox_camera)
        self.label_camera_contrast.setObjectName(_fromUtf8("label_camera_contrast"))
        self.gridLayout_2.addWidget(self.label_camera_contrast, 4, 0, 1, 1)
        self.horizontalSlider_camera_contrast = QtGui.QSlider(self.groupBox_camera)
        self.horizontalSlider_camera_contrast.setMinimum(0)
        self.horizontalSlider_camera_contrast.setMaximum(20)
        self.horizontalSlider_camera_contrast.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_camera_contrast.setObjectName(_fromUtf8("horizontalSlider_camera_contrast"))
        self.gridLayout_2.addWidget(self.horizontalSlider_camera_contrast, 4, 1, 1, 1)
        self.label_camera_contrast_value = QtGui.QLabel(self.groupBox_camera)
        self.label_camera_contrast_value.setObjectName(_fromUtf8("label_camera_contrast_value"))
        self.gridLayout_2.addWidget(self.label_camera_contrast_value, 4, 2, 1, 1)
        self.label_camera_exposure = QtGui.QLabel(self.groupBox_camera)
        self.label_camera_exposure.setObjectName(_fromUtf8("label_camera_exposure"))
        self.gridLayout_2.addWidget(self.label_camera_exposure, 5, 0, 1, 1)
        self.horizontalSlider_camera_exposure = QtGui.QSlider(self.groupBox_camera)
        self.horizontalSlider_camera_exposure.setMinimum(-20)
        self.horizontalSlider_camera_exposure.setMaximum(10)
        self.horizontalSlider_camera_exposure.setProperty("value", 0)
        self.horizontalSlider_camera_exposure.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_camera_exposure.setObjectName(_fromUtf8("horizontalSlider_camera_exposure"))
        self.gridLayout_2.addWidget(self.horizontalSlider_camera_exposure, 5, 1, 1, 1)
        self.label_camera_exposure_value = QtGui.QLabel(self.groupBox_camera)
        self.label_camera_exposure_value.setObjectName(_fromUtf8("label_camera_exposure_value"))
        self.gridLayout_2.addWidget(self.label_camera_exposure_value, 5, 2, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_camera, 0, 0, 1, 1)
        self.groupBox_general = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_general.setObjectName(_fromUtf8("groupBox_general"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_general)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_general_blur = QtGui.QLabel(self.groupBox_general)
        self.label_general_blur.setObjectName(_fromUtf8("label_general_blur"))
        self.gridLayout_3.addWidget(self.label_general_blur, 0, 0, 1, 1)
        self.horizontalSlider_general_blur = QtGui.QSlider(self.groupBox_general)
        self.horizontalSlider_general_blur.setMaximum(5)
        self.horizontalSlider_general_blur.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_general_blur.setObjectName(_fromUtf8("horizontalSlider_general_blur"))
        self.gridLayout_3.addWidget(self.horizontalSlider_general_blur, 0, 1, 1, 1)
        self.label_general_blur_value = QtGui.QLabel(self.groupBox_general)
        self.label_general_blur_value.setObjectName(_fromUtf8("label_general_blur_value"))
        self.gridLayout_3.addWidget(self.label_general_blur_value, 0, 2, 1, 1)
        self.label_general_zoom = QtGui.QLabel(self.groupBox_general)
        self.label_general_zoom.setObjectName(_fromUtf8("label_general_zoom"))
        self.gridLayout_3.addWidget(self.label_general_zoom, 1, 0, 1, 1)
        self.horizontalSlider_general_zoom = QtGui.QSlider(self.groupBox_general)
        self.horizontalSlider_general_zoom.setMaximum(49)
        self.horizontalSlider_general_zoom.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_general_zoom.setObjectName(_fromUtf8("horizontalSlider_general_zoom"))
        self.gridLayout_3.addWidget(self.horizontalSlider_general_zoom, 1, 1, 1, 1)
        self.label_general_zoom_value = QtGui.QLabel(self.groupBox_general)
        self.label_general_zoom_value.setObjectName(_fromUtf8("label_general_zoom_value"))
        self.gridLayout_3.addWidget(self.label_general_zoom_value, 1, 2, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_general, 0, 1, 1, 1)
        self.groupBox_led = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_led.setObjectName(_fromUtf8("groupBox_led"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_led)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_led_binary = QtGui.QLabel(self.groupBox_led)
        self.label_led_binary.setObjectName(_fromUtf8("label_led_binary"))
        self.gridLayout_4.addWidget(self.label_led_binary, 0, 0, 1, 1)
        self.horizontalSlider_led_binary = QtGui.QSlider(self.groupBox_led)
        self.horizontalSlider_led_binary.setMinimum(180)
        self.horizontalSlider_led_binary.setMaximum(255)
        self.horizontalSlider_led_binary.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_led_binary.setObjectName(_fromUtf8("horizontalSlider_led_binary"))
        self.gridLayout_4.addWidget(self.horizontalSlider_led_binary, 0, 1, 1, 1)
        self.label_led_binary_value = QtGui.QLabel(self.groupBox_led)
        self.label_led_binary_value.setObjectName(_fromUtf8("label_led_binary_value"))
        self.gridLayout_4.addWidget(self.label_led_binary_value, 0, 2, 1, 1)
        self.label_led_min = QtGui.QLabel(self.groupBox_led)
        self.label_led_min.setObjectName(_fromUtf8("label_led_min"))
        self.gridLayout_4.addWidget(self.label_led_min, 1, 0, 1, 1)
        self.horizontalSlider_led_min = QtGui.QSlider(self.groupBox_led)
        self.horizontalSlider_led_min.setMinimum(1)
        self.horizontalSlider_led_min.setMaximum(30)
        self.horizontalSlider_led_min.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_led_min.setObjectName(_fromUtf8("horizontalSlider_led_min"))
        self.gridLayout_4.addWidget(self.horizontalSlider_led_min, 1, 1, 1, 1)
        self.label_led_min_value = QtGui.QLabel(self.groupBox_led)
        self.label_led_min_value.setObjectName(_fromUtf8("label_led_min_value"))
        self.gridLayout_4.addWidget(self.label_led_min_value, 1, 2, 1, 1)
        self.label_led_max = QtGui.QLabel(self.groupBox_led)
        self.label_led_max.setObjectName(_fromUtf8("label_led_max"))
        self.gridLayout_4.addWidget(self.label_led_max, 2, 0, 1, 1)
        self.horizontalSlider_led_max = QtGui.QSlider(self.groupBox_led)
        self.horizontalSlider_led_max.setMinimum(3)
        self.horizontalSlider_led_max.setMaximum(60)
        self.horizontalSlider_led_max.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_led_max.setObjectName(_fromUtf8("horizontalSlider_led_max"))
        self.gridLayout_4.addWidget(self.horizontalSlider_led_max, 2, 1, 1, 1)
        self.label_led_max_value = QtGui.QLabel(self.groupBox_led)
        self.label_led_max_value.setObjectName(_fromUtf8("label_led_max_value"))
        self.gridLayout_4.addWidget(self.label_led_max_value, 2, 2, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_led, 1, 0, 1, 1)
        self.groupBox_pupil = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_pupil.setObjectName(_fromUtf8("groupBox_pupil"))
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_pupil)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_pupil_binary = QtGui.QLabel(self.groupBox_pupil)
        self.label_pupil_binary.setObjectName(_fromUtf8("label_pupil_binary"))
        self.gridLayout_5.addWidget(self.label_pupil_binary, 0, 0, 1, 1)
        self.horizontalSlider_pupil_binary = QtGui.QSlider(self.groupBox_pupil)
        self.horizontalSlider_pupil_binary.setMinimum(180)
        self.horizontalSlider_pupil_binary.setMaximum(255)
        self.horizontalSlider_pupil_binary.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_pupil_binary.setObjectName(_fromUtf8("horizontalSlider_pupil_binary"))
        self.gridLayout_5.addWidget(self.horizontalSlider_pupil_binary, 0, 1, 1, 1)
        self.label_pupil_binary_value = QtGui.QLabel(self.groupBox_pupil)
        self.label_pupil_binary_value.setObjectName(_fromUtf8("label_pupil_binary_value"))
        self.gridLayout_5.addWidget(self.label_pupil_binary_value, 0, 2, 1, 1)
        self.label_pupil_min = QtGui.QLabel(self.groupBox_pupil)
        self.label_pupil_min.setObjectName(_fromUtf8("label_pupil_min"))
        self.gridLayout_5.addWidget(self.label_pupil_min, 1, 0, 1, 1)
        self.horizontalSlider_pupil_min = QtGui.QSlider(self.groupBox_pupil)
        self.horizontalSlider_pupil_min.setMinimum(1)
        self.horizontalSlider_pupil_min.setMaximum(200)
        self.horizontalSlider_pupil_min.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_pupil_min.setObjectName(_fromUtf8("horizontalSlider_pupil_min"))
        self.gridLayout_5.addWidget(self.horizontalSlider_pupil_min, 1, 1, 1, 1)
        self.label_pupil_min_value = QtGui.QLabel(self.groupBox_pupil)
        self.label_pupil_min_value.setObjectName(_fromUtf8("label_pupil_min_value"))
        self.gridLayout_5.addWidget(self.label_pupil_min_value, 1, 2, 1, 1)
        self.label_pupil_max = QtGui.QLabel(self.groupBox_pupil)
        self.label_pupil_max.setObjectName(_fromUtf8("label_pupil_max"))
        self.gridLayout_5.addWidget(self.label_pupil_max, 2, 0, 1, 1)
        self.horizontalSlider_pupil_max = QtGui.QSlider(self.groupBox_pupil)
        self.horizontalSlider_pupil_max.setMinimum(50)
        self.horizontalSlider_pupil_max.setMaximum(600)
        self.horizontalSlider_pupil_max.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_pupil_max.setObjectName(_fromUtf8("horizontalSlider_pupil_max"))
        self.gridLayout_5.addWidget(self.horizontalSlider_pupil_max, 2, 1, 1, 1)
        self.label_pupil_max_value = QtGui.QLabel(self.groupBox_pupil)
        self.label_pupil_max_value.setObjectName(_fromUtf8("label_pupil_max_value"))
        self.gridLayout_5.addWidget(self.label_pupil_max_value, 2, 2, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox_pupil, 1, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_6 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.checkBox_triangle = QtGui.QCheckBox(self.groupBox)
        self.checkBox_triangle.setObjectName(_fromUtf8("checkBox_triangle"))
        self.gridLayout_6.addWidget(self.checkBox_triangle, 0, 0, 1, 1)
        self.checkBox_printOutput = QtGui.QCheckBox(self.groupBox)
        self.checkBox_printOutput.setObjectName(_fromUtf8("checkBox_printOutput"))
        self.gridLayout_6.addWidget(self.checkBox_printOutput, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.groupBox, 2, 0, 1, 1)
        self.groupBox_Output = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_Output.setObjectName(_fromUtf8("groupBox_Output"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_Output)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.checkBox_toFile = QtGui.QCheckBox(self.groupBox_Output)
        self.checkBox_toFile.setObjectName(_fromUtf8("checkBox_toFile"))
        self.gridLayout.addWidget(self.checkBox_toFile, 0, 0, 1, 1)
        self.lineEdit_output = QtGui.QLineEdit(self.groupBox_Output)
        self.lineEdit_output.setObjectName(_fromUtf8("lineEdit_output"))
        self.gridLayout.addWidget(self.lineEdit_output, 0, 1, 1, 2)
        self.checkBox_toVideo = QtGui.QCheckBox(self.groupBox_Output)
        self.checkBox_toVideo.setObjectName(_fromUtf8("checkBox_toVideo"))
        self.gridLayout.addWidget(self.checkBox_toVideo, 1, 0, 1, 2)
        self.lineEdit_video = QtGui.QLineEdit(self.groupBox_Output)
        self.lineEdit_video.setObjectName(_fromUtf8("lineEdit_video"))
        self.gridLayout.addWidget(self.lineEdit_video, 1, 2, 1, 1)
        self.checkBox_toConsole = QtGui.QCheckBox(self.groupBox_Output)
        self.checkBox_toConsole.setObjectName(_fromUtf8("checkBox_toConsole"))
        self.gridLayout.addWidget(self.checkBox_toConsole, 2, 0, 1, 3)
        self.pushButton_output = QtGui.QPushButton(self.groupBox_Output)
        self.pushButton_output.setObjectName(_fromUtf8("pushButton_output"))
        self.gridLayout.addWidget(self.pushButton_output, 3, 0, 1, 3)
        self.gridLayout_7.addWidget(self.groupBox_Output, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.horizontalSlider_led_binary, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_led_binary_value.setNum)
        QtCore.QObject.connect(self.horizontalSlider_led_max, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_led_max_value.setNum)
        QtCore.QObject.connect(self.horizontalSlider_led_min, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_led_min_value.setNum)
        QtCore.QObject.connect(self.horizontalSlider_general_blur, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_general_blur_value.setNum)
        QtCore.QObject.connect(self.horizontalSlider_general_zoom, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_general_zoom_value.setNum)
        QtCore.QObject.connect(self.horizontalSlider_pupil_binary, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_pupil_binary_value.setNum)
        QtCore.QObject.connect(self.horizontalSlider_pupil_max, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_pupil_max_value.setNum)
        QtCore.QObject.connect(self.horizontalSlider_pupil_min, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_pupil_min_value.setNum)
        QtCore.QObject.connect(self.horizontalSlider_camera_hue, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_camera_hue_value.setNum)
        QtCore.QObject.connect(self.horizontalSlider_camera_saturation, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_camera_saturation_value.setNum)
        QtCore.QObject.connect(self.horizontalSlider_camera_brightness, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_camera_brightness_value.setNum)
        QtCore.QObject.connect(self.horizontalSlider_camera_gain, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_camera_gain_value.setNum)
        QtCore.QObject.connect(self.horizontalSlider_camera_contrast, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_camera_contrast_value.setNum)
        QtCore.QObject.connect(self.horizontalSlider_camera_exposure, QtCore.SIGNAL(_fromUtf8("sliderMoved(int)")), self.label_camera_exposure_value.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Eyetracker", None))
        self.groupBox_camera.setTitle(_translate("MainWindow", "Camera", None))
        self.label_camera_hue.setText(_translate("MainWindow", "Hue", None))
        self.label_camera_hue_value.setText(_translate("MainWindow", "0.0", None))
        self.label_camera_saturation.setText(_translate("MainWindow", "Saturation", None))
        self.label_camera_saturation_value.setText(_translate("MainWindow", "0.0", None))
        self.label_camera_brightness.setText(_translate("MainWindow", "Brightness", None))
        self.label_camera_brightness_value.setText(_translate("MainWindow", "0.0", None))
        self.label_camera_gain.setText(_translate("MainWindow", "Gain", None))
        self.label_camera_gain_value.setText(_translate("MainWindow", "0.0", None))
        self.label_camera_contrast.setText(_translate("MainWindow", "Contrast", None))
        self.label_camera_contrast_value.setText(_translate("MainWindow", "0.0", None))
        self.label_camera_exposure.setText(_translate("MainWindow", "Exposure", None))
        self.label_camera_exposure_value.setText(_translate("MainWindow", "0.0", None))
        self.groupBox_general.setTitle(_translate("MainWindow", "General", None))
        self.label_general_blur.setText(_translate("MainWindow", "Blur", None))
        self.label_general_blur_value.setText(_translate("MainWindow", "0", None))
        self.label_general_zoom.setText(_translate("MainWindow", "Zoom", None))
        self.label_general_zoom_value.setText(_translate("MainWindow", "0", None))
        self.groupBox_led.setTitle(_translate("MainWindow", "LED", None))
        self.label_led_binary.setText(_translate("MainWindow", "Binary Thresh", None))
        self.label_led_binary_value.setText(_translate("MainWindow", "0.0", None))
        self.label_led_min.setText(_translate("MainWindow", "Min Size", None))
        self.label_led_min_value.setText(_translate("MainWindow", "0.0", None))
        self.label_led_max.setText(_translate("MainWindow", "Max Size", None))
        self.label_led_max_value.setText(_translate("MainWindow", "0.0", None))
        self.groupBox_pupil.setTitle(_translate("MainWindow", "Pupil", None))
        self.label_pupil_binary.setText(_translate("MainWindow", "Binary Thresh", None))
        self.label_pupil_binary_value.setText(_translate("MainWindow", "0.0", None))
        self.label_pupil_min.setText(_translate("MainWindow", "Min Size", None))
        self.label_pupil_min_value.setText(_translate("MainWindow", "0.0", None))
        self.label_pupil_max.setText(_translate("MainWindow", "Max Size", None))
        self.label_pupil_max_value.setText(_translate("MainWindow", "0.0", None))
        self.groupBox.setTitle(_translate("MainWindow", "Options", None))
        self.checkBox_triangle.setText(_translate("MainWindow", "Show triangle", None))
        self.checkBox_printOutput.setText(_translate("MainWindow", "Print output", None))
        self.groupBox_Output.setTitle(_translate("MainWindow", "Output", None))
        self.checkBox_toFile.setText(_translate("MainWindow", "To File:", None))
        self.lineEdit_output.setText(_translate("MainWindow", "C:\\eyetracking.dat", None))
        self.checkBox_toVideo.setText(_translate("MainWindow", "To Video:", None))
        self.lineEdit_video.setText(_translate("MainWindow", "C:\\eyetracking.avi", None))
        self.checkBox_toConsole.setText(_translate("MainWindow", "To Console", None))
        self.pushButton_output.setText(_translate("MainWindow", "Output", None))

