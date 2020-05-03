from PyQt5 import QtGui, QtCore
import pyqtgraph as pg
from enum import Enum
import numpy as np
import bluetooth
import sys
import gui
from time import sleep as slp


#%%
nextCommand = 0x24  
x = 0


#%%

class DSOApp(QtGui.QMainWindow, gui.Ui_MainWindow):
        def __init__(self):
                super(self.__class__, self).__init__()
                self.setupUi(self)
                
                self.startButton.clicked.connect(self.Start)
                self.exitButton.clicked.connect(self.Exit)
                
                self.ch1_enable_button.clicked.connect(self.ch1_enable)
                self.ch2_enable_button.clicked.connect(self.ch2_enable)
                self.ch3_enable_button.clicked.connect(self.ch3_enable)
                self.ch4_enable_button.clicked.connect(self.ch4_enable)
                
                self.ch1_vDiv_dial.valueChanged.connect(self.ch1_vDiv)
                self.ch2_vDiv_dial.valueChanged.connect(self.ch2_vDiv)
                self.ch3_vDiv_dial.valueChanged.connect(self.ch3_vDiv)
                self.ch4_vDiv_dial.valueChanged.connect(self.ch4_vDiv)
                
                self.ch1_coupling.currentIndexChanged.connect(self.ch1_cpl)
                self.ch2_coupling.currentIndexChanged.connect(self.ch2_cpl)
                self.ch3_coupling.currentIndexChanged.connect(self.ch3_cpl)
                self.ch4_coupling.currentIndexChanged.connect(self.ch4_cpl)
                
                self.ch1_vertical_dial.valueChanged.connect(self.ch1_vert)
                self.ch2_vertical_dial.valueChanged.connect(self.ch2_vert)
                self.ch3_vertical_dial.valueChanged.connect(self.ch3_vert)
                self.ch4_vertical_dial.valueChanged.connect(self.ch4_vert)
                
                self.trigger_edge.currentIndexChanged.connect(self.trig_edge)
                self.trigger_source.currentIndexChanged.connect(self.trig_source)
                self.tirgger_level_dial.valueChanged.connect(self.trig_value)
                
                self.timeDiv_dial.valueChanged.connect(self.timeDiv)
                
                self.ch1_vert_prev_val = 0
                self.ch2_vert_prev_val = 0
                self.ch3_vert_prev_val = 0
                self.ch4_vert_prev_val = 0
                
                
                self.trig_level_prev_val = 0
                
                self.dso1 = DSO()
                
                self.sock = bluetooth.BluetoothSocket( bluetooth.RFCOMM )

		
                
        def ch1_enable(self):
                if(self.dso1.ch1.enabled == 0):
                        self.dso1.ch1.enabled = 1
                else:
                        self.dso1.ch1.enabled = 0
                        
                self.updateEnabled()
                updateSetup()    
                
        def ch2_enable(self):
                if(self.dso1.ch2.enabled == 0):
                        self.dso1.ch2.enabled = 1
                else:
                        self.dso1.ch2.enabled = 0
                        
                self.updateEnabled()
                updateSetup()
                        
        def ch3_enable(self):
                if(self.dso1.ch3.enabled == 0):
                        self.dso1.ch3.enabled = 1
                else:
                        self.dso1.ch3.enabled = 0
                        
                self.updateEnabled()
                updateSetup()
                        
        def ch4_enable(self):
                if(self.dso1.ch4.enabled == 0):
                        self.dso1.ch4.enabled = 1
                else:
                        self.dso1.ch4.enabled = 0
                        
                self.updateEnabled()
                updateSetup()
        
        def ch1_vDiv(self):
                self.dso1.ch1.voltsDiv = self.ch1_vDiv_dial.value()   
                self.ch1_vDivText()
                updateSetup()
                
        def ch1_vDivText(self):
                if(self.dso1.ch1.voltsDiv == 0):
                        self.ch1_vDiv_label.setText("100mV")
                        
                elif(self.dso1.ch1.voltsDiv == 1):
                        self.ch1_vDiv_label.setText("200mV")
                        
                elif(self.dso1.ch1.voltsDiv == 2):
                        self.ch1_vDiv_label.setText("500mV")
                        
                elif(self.dso1.ch1.voltsDiv == 3):
                        self.ch1_vDiv_label.setText("1V")
                        
                elif(self.dso1.ch1.voltsDiv == 4):
                        self.ch1_vDiv_label.setText("2V")
                        
                elif(self.dso1.ch1.voltsDiv == 5):
                        self.ch1_vDiv_label.setText("5V")
                
        def ch2_vDiv(self):
                self.dso1.ch2.voltsDiv = self.ch2_vDiv_dial.value()
                self.ch2_vDivText()
                updateSetup()
        
        def ch2_vDivText(self):
                
                if(self.dso1.ch2.voltsDiv == 0):
                        self.ch2_vDiv_label.setText("100mV")
                        
                elif(self.dso1.ch2.voltsDiv == 1):
                        self.ch2_vDiv_label.setText("200mV")
                        
                elif(self.dso1.ch2.voltsDiv == 2):
                        self.ch2_vDiv_label.setText("500mV")
                        
                elif(self.dso1.ch2.voltsDiv == 3):
                        self.ch2_vDiv_label.setText("1V")
                        
                elif(self.dso1.ch2.voltsDiv == 4):
                        self.ch2_vDiv_label.setText("2V")
                        
                elif(self.dso1.ch2.voltsDiv == 5):
                        self.ch2_vDiv_label.setText("5V")
                
        def ch3_vDiv(self):
                self.dso1.ch3.voltsDiv = self.ch3_vDiv_dial.value()
                self.ch3_vDivText()
                updateSetup()
                
        def ch3_vDivText(self):
                if(self.dso1.ch3.voltsDiv == 0):
                        self.ch3_vDiv_label.setText("100mV")
                        
                elif(self.dso1.ch3.voltsDiv == 1):
                        self.ch3_vDiv_label.setText("200mV")
                        
                elif(self.dso1.ch3.voltsDiv == 2):
                        self.ch3_vDiv_label.setText("500mV")
                        
                elif(self.dso1.ch3.voltsDiv == 3):
                        self.ch3_vDiv_label.setText("1V")
                        
                elif(self.dso1.ch3.voltsDiv == 4):
                        self.ch3_vDiv_label.setText("2V")
                        
                elif(self.dso1.ch3.voltsDiv == 5):
                        self.ch3_vDiv_label.setText("5V")
        
        def ch4_vDiv(self):
                self.dso1.ch4.voltsDiv = self.ch4_vDiv_dial.value()
                self.ch4_vDivText()
                updateSetup()
        
        def ch4_vDivText(self):
                if(self.dso1.ch4.voltsDiv == 0):
                        self.ch4_vDiv_label.setText("100mV")
                        
                elif(self.dso1.ch4.voltsDiv == 1):
                        self.ch4_vDiv_label.setText("200mV")
                        
                elif(self.dso1.ch4.voltsDiv == 2):
                        self.ch4_vDiv_label.setText("500mV")
                        
                elif(self.dso1.ch4.voltsDiv == 3):
                        self.ch4_vDiv_label.setText("1V")
                        
                elif(self.dso1.ch4.voltsDiv == 4):
                        self.ch4_vDiv_label.setText("2V")
                        
                elif(self.dso1.ch4.voltsDiv == 5):
                        self.ch4_vDiv_label.setText("5V")
                else:
                        self.ch4_vDiv_label.setText("err")
                
        def ch1_cpl(self):
                self.dso1.ch1.coupling = self.ch1_coupling.currentIndex()
                updateSetup()
        
        def ch2_cpl(self):
                self.dso1.ch2.coupling = self.ch2_coupling.currentIndex()
                updateSetup()

        def ch3_cpl(self):
                self.dso1.ch3.coupling = self.ch3_coupling.currentIndex()
                updateSetup()
                
        def ch4_cpl(self):
                self.dso1.ch4.coupling = self.ch4_coupling.currentIndex()
                updateSetup()
                
        def ch1_vert(self):
                if((self.ch1_vert_prev_val == 8) and (self.ch1_vertical_dial.value() == 0)):
                        self.dso1.ch1.vertical += 4
               
                elif((self.ch1_vert_prev_val == 0) and (self.ch1_vertical_dial.value() == 8)):
                        self.dso1.ch1.vertical -= 4
                
                elif(self.ch1_vert_prev_val > self.ch1_vertical_dial.value()):
                        self.dso1.ch1.vertical -= 4
                
                elif(self.ch1_vert_prev_val < self.ch1_vertical_dial.value()):
                        self.dso1.ch1.vertical += 4
                
                self.ch1_vert_prev_val = self.ch1_vertical_dial.value()
                updateSetup()
                
        def ch2_vert(self):
                if((self.ch2_vert_prev_val == 8) and (self.ch2_vertical_dial.value() == 0)):
                        self.dso1.ch2.vertical += 4
               
                elif((self.ch2_vert_prev_val == 0) and (self.ch2_vertical_dial.value() == 8)):
                        self.dso1.ch2.vertical -= 4
                
                elif(self.ch2_vert_prev_val > self.ch2_vertical_dial.value()):
                        self.dso1.ch2.vertical -= 4
                
                elif(self.ch2_vert_prev_val < self.ch2_vertical_dial.value()):
                        self.dso1.ch2.vertical += 4
                
                self.ch2_vert_prev_val = self.ch2_vertical_dial.value()
                updateSetup()
                
        def ch3_vert(self):
                if((self.ch3_vert_prev_val == 8) and (self.ch3_vertical_dial.value() == 0)):
                        self.dso1.ch3.vertical += 4
               
                elif((self.ch3_vert_prev_val == 0) and (self.ch3_vertical_dial.value() == 8)):
                        self.dso1.ch3.vertical -= 4
                
                elif(self.ch3_vert_prev_val > self.ch3_vertical_dial.value()):
                        self.dso1.ch3.vertical -= 4
                
                elif(self.ch3_vert_prev_val < self.ch3_vertical_dial.value()):
                        self.dso1.ch3.vertical += 4
                
                self.ch3_vert_prev_val = self.ch3_vertical_dial.value()
                updateSetup()
                
        def ch4_vert(self):
                if((self.ch4_vert_prev_val == 8) and (self.ch4_vertical_dial.value() == 0)):
                        self.dso1.ch4.vertical += 4
               
                elif((self.ch4_vert_prev_val == 0) and (self.ch4_vertical_dial.value() == 8)):
                        self.dso1.ch4.vertical -= 4
                
                elif(self.ch4_vert_prev_val > self.ch4_vertical_dial.value()):
                        self.dso1.ch4.vertical -= 4
                
                elif(self.ch4_vert_prev_val < self.ch4_vertical_dial.value()):
                        self.dso1.ch4.vertical += 4
                
                self.ch4_vert_prev_val = self.ch4_vertical_dial.value()
                updateSetup()
                
        def trig_edge(self):
                self.dso1.triggerEdge = self.trigger_edge.currentIndex()
                updateSetup()
                
        def trig_source(self):
                self.dso1.trggerSource = self.trigger_source.currentIndex()+1
                updateSetup()
                
        def trig_value(self):
                inc = False
                if((self.trig_level_prev_val == 8) and (self.tirgger_level_dial.value() == 0)):
                        inc = True
               
                elif((self.trig_level_prev_val == 0) and (self.tirgger_level_dial.value() == 8)):
                        inc = False
                
                elif(self.trig_level_prev_val > self.tirgger_level_dial.value()):
                        inc = False
                
                elif(self.trig_level_prev_val < self.tirgger_level_dial.value()):
                        inc = True
                
               # print self.trig_level_prev_val
                self.trig_level_prev_val = self.tirgger_level_dial.value()
               # print self.trig_level_prev_val
#                channel = []
#                if self.dso1.trggerSource == 1 :
#                        channel = self.dso1.ch1
#                elif self.dso1.trggerSource == 2 :
#                        channel = self.dso1.ch2
#                elif self.dso1.trggerSource == 3 :
#                        channel = self.dso1.ch3
#                elif self.dso1.trggerSource == 4 :
#                        channel = self.dso1.ch4
#                
#                if channel.voltsDiv == vDivs.v_100mDiv:
                if(inc):
                        self.dso1.triggerValue += 27 
                else:
                        self.dso1.triggerValue -= 27
                
                updateSetup()
                        
                
        def timeDiv(self):
                self.dso1.horizontal = self.timeDiv_dial.value()
                updateSetup()
                self.setHorizText()
                 
        def setHorizText(self):
                if(self.dso1.horizontal == 0):
                        self.timeDiv_label.setText("1 ms")
                        
                elif(self.dso1.horizontal == 1):
                        self.timeDiv_label.setText("500 us")
                        
                elif(self.dso1.horizontal == 2):
                        self.timeDiv_label.setText("250 us")
                        
                elif(self.dso1.horizontal == 3):
                        self.timeDiv_label.setText("100 us")
                        
                elif(self.dso1.horizontal == 4):
                        self.timeDiv_label.setText("50 us")
                        
                elif(self.dso1.horizontal == 5):
                        self.timeDiv_label.setText("25 us")
                        
                elif(self.dso1.horizontal == 6):
                        self.timeDiv_label.setText("10 us")
                        
                elif(self.dso1.horizontal == 7):
                        self.timeDiv_label.setText("5 us")
                        
                elif(self.dso1.horizontal == 8):
                        self.timeDiv_label.setText("2.5 us")
                        
                elif(self.dso1.horizontal == 9):
                        self.timeDiv_label.setText("1 us")
                else:
                        self.timeDiv_label.setText("err")
                        
        def sendSetup(self):
                s = np.zeros(11, dtype = 'int8')
                x1 = self.dso1.triggerEdge << 4
                x2 = self.dso1.quad << 5
                x3 = self.dso1.dual1 << 6
                x4 = self.dso1.dual2 << 7
                s[0] = self.dso1.horizontal + x1 + x2 + x3 + x4
                s[1] = self.dso1.triggerValue & 0x00FF
                s[2] = ((self.dso1.triggerValue & 0x0F00) >> 8) + (self.dso1.trggerSource << 4)
#                print "s1:", s[1]
#                print "s2:", s[2]
               # print self.dso1.triggerValue
                
                s[3] = self.dso1.ch1.enabled + (self.dso1.ch1.voltsDiv << 1)+ (self.dso1.ch1.coupling << 4)
                s[4] = self.dso1.ch1.vertical
                
                s[5] = self.dso1.ch2.enabled + (self.dso1.ch2.voltsDiv << 1) + (self.dso1.ch2.coupling << 4)
                s[6] = self.dso1.ch2.vertical
                
                s[7] = self.dso1.ch3.enabled + (self.dso1.ch3.voltsDiv << 1) + (self.dso1.ch3.coupling << 4)
                s[8] = self.dso1.ch3.vertical
                
                s[9] = self.dso1.ch4.enabled + (self.dso1.ch4.voltsDiv << 1) + (self.dso1.ch4.coupling << 4)
                s[10] = self.dso1.ch4.vertical
                
#                print s.shape
#                s = str(s)
                
                self.sock.send(s)
                
        def receiveSetup(self):
#                com = chr(commands.requestSetup)
                self.sock.send(chr(0xAA))
                k = self.sock.recv(11)
                self.dso1.horizontal = ord(k[0]) & 0x0F
                self.timeDiv_dial.setValue(self.dso1.horizontal)
                self.setHorizText()
                self.dso1.triggerEdge = (ord(k[0]) & 0x10) >> 4
                self.trigger_edge.setCurrentIndex(self.dso1.triggerEdge)
                self.dso1.quad = (ord(k[0]) & 0x20) >> 5
                self.dso1.dual1 = (ord(k[0]) & 0x40) >> 6
                self.dso1.dual2 = (ord(k[0]) & 0x80) >> 7
                
                self.dso1.triggerValue = ord(k[1]) + ((ord(k[2]) & 0x0f) << 8)
                self.dso1.trggerSource = ((ord(k[2]) & 0x30) >> 4) - 1
                self.trigger_source.setCurrentIndex(self.dso1.trggerSource)
#                print self.dso1.triggerValue
                self.dso1.ch1.enabled = ord(k[3]) & 0x01
                self.dso1.ch1.voltsDiv = (ord(k[3]) & 0x0E) >> 1
                self.ch1_vDiv_dial.setValue(self.dso1.ch1.voltsDiv)
                self.ch1_vDivText()
                self.dso1.ch1.coupling =  (ord(k[3]) & 0x30) >> 4
                self.ch1_coupling.setCurrentIndex(self.dso1.ch1.coupling)
                self.dso1.ch1.vertical =  ord(k[4])
                
                self.dso1.ch2.enabled = ord(k[5]) & 0x01
                self.dso1.ch2.voltsDiv = (ord(k[5]) & 0x0E) >> 1
                self.ch2_vDiv_dial.setValue(self.dso1.ch2.voltsDiv)
                self.ch2_vDivText()
                self.dso1.ch2.coupling =  (ord(k[5]) & 0x30) >> 4
                self.ch2_coupling.setCurrentIndex(self.dso1.ch2.coupling)
                self.dso1.ch2.vertical =  ord(k[6])
                
                self.dso1.ch3.enabled = ord(k[7]) & 0x01
                self.dso1.ch3.voltsDiv = (ord(k[7]) & 0x0E) >> 1
                self.ch3_vDiv_dial.setValue(self.dso1.ch3.voltsDiv)
                self.ch3_vDivText()
                self.dso1.ch3.coupling =  (ord(k[7]) & 0x30) >> 4
                self.ch3_coupling.setCurrentIndex(self.dso1.ch3.coupling)
                self.dso1.ch3.vertical =  ord(k[8])
                
                self.dso1.ch4.enabled = ord(k[9]) & 0x01
                self.dso1.ch4.voltsDiv = (ord(k[9]) & 0x0E) >> 1
                self.ch4_vDiv_dial.setValue(self.dso1.ch4.voltsDiv)
                self.ch4_vDivText()
                self.dso1.ch4.coupling =  (ord(k[9]) & 0x30) >> 4
                self.ch4_coupling.setCurrentIndex(self.dso1.ch4.coupling)
                self.dso1.ch4.vertical =  ord(k[10])
                
        def updateEnabled(self):
                global x
                x = self.dso1.ch1.enabled
                x += self.dso1.ch2.enabled << 1
                x += self.dso1.ch3.enabled << 2
                x += self.dso1.ch4.enabled << 3
                
        def Start(self):
            bd_addr = "00:14:01:06:14:17"
            port = 9
            self.sock.connect((bd_addr, port))
            print('Connected')
            self.sock.settimeout(1.0)
            slp(3)
#		self.ser.open()
            self.receiveSetup()
            self.updateEnabled()
            timer.start(5)
                
        def Exit(self):
                Exit()
        

        
class timeDivs(Enum):
        timeDiv_1ms = 0
        timeDiv_500us = 1
        timeDiv_250us = 2
        timeDiv_100us = 3
        timeDiv_50us = 4
        timeDiv_25us = 5
        timeDiv_10us = 6
        timeDiv_5us = 7
        timeDiv_2_5us = 8
        timeDiv_1us = 9
        
class vDivs(Enum):
        v_100mDiv = 0
        v_200mDiv = 1
        v_500mDiv = 2
        v_1Div = 3
        v_2Div = 4
        v_5Div = 5
        
class cpl(Enum):
        GND = 0
        DC = 1
        AC = 2

class commands(Enum):
        setupChange = '<'
        requestData = '$'
        requestSetup = chr(0xAA)
        acknowledge = chr(0xAC)
        
class channel():
        def __init__(self):
                self.enabled = 0x00
                self.vertical = 0x00
                self.coupling = cpl.DC
                self.voltsDiv = vDivs.v_1Div

class DSO():
        def __init__(self):
                 self.quad = 0x00
                 self.dual1 = 0x00
                 self.dual2 = 0x00
                 self.triggerValue = 2048
                 self.trggerSource = 0x01
                 self.triggerEdge = 0x01
                 self.horizontal = timeDivs.timeDiv_50us
                 self.ch1 = channel()
                 self.ch2 = channel()
                 self.ch3 = channel()
                 self.ch4 = channel()
    
def loop():
        global nextCommand
        Command = nextCommand
        data = []
        if(Command == 0x24) and (x > 0):
#                print "loop"
                form.sock.send(chr(0x24))
                if(x == 1): 
                        try:
                                y = form.sock.recv(280)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.setData(dat)
                                c2.clear()
                                c3.clear()
                                c4.clear()
                        
                elif(x == 2):
                        try:
                                y = form.sock.recv(280)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.clear()
                                c2.setData(dat)
                                c3.clear()
                                c4.clear()
                        
                elif(x == 3):
                        try:
                                y = form.sock.recv(280*2)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.setData(dat[:280])
                                c2.setData(dat[280:])
                                c3.clear()
                                c4.clear()
                        
                elif(x == 4):
                        try:
                                y = form.sock.recv(280)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.clear()
                                c2.clear()
                                c3.setData(dat)
                                c4.clear()
                        
                elif(x == 5):
                        try:
                                y = form.sock.recv(280*2)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.setData(dat[:280])
                                c2.clear()
                                c3.setData(dat[280:])
                                c4.clear()
                        
                elif(x == 6):
                        try:
                                y = form.sock.recv(280*2)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.clear()
                                c2.setData(dat[:280])
                                c3.setData(dat[280:])
                                c4.clear()
                        
                elif(x == 7):
                        try:
                                y = form.sock.recv(280*3)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.setData(dat[:280])
                                c2.setData(dat[280:560])
                                c3.setData(dat[560:])
                                c4.clear()
                        
                elif(x == 8):
                        try:
                                y = form.sock.recv(280)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.clear()
                                c2.clear()
                                c3.clear()
                                c4.setData(dat)
                        
                elif(x == 9):
                        try:
                                y = form.sock.recv(280*2)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.setData(dat[280:])
                                c2.clear()
                                c3.clear()
                                c4.setData(dat[:280])
                        
                elif(x == 10):
                        try:
                                y = form.sock.recv(280*2)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.clear()
                                c2.setData(dat[280:])
                                c3.clear()
                                c4.setData(dat[:280])
                        
                elif(x == 11):
                        try:
                                y = form.sock.recv(280*2)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.clear()
                                c2.setData(dat[:280])
                                c3.setData(dat[280:])
                                c4.clear()
                        
                elif(x == 12):
                        try:
                                y = form.sock.recv(280*2)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.clear()
                                c2.clear()
                                c3.setData(dat[:280])
                                c4.setData(dat[280:])
                        
                elif(x == 13):
                        try:
                                y = form.sock.recv(280*3)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.setData(dat[:280])
                                c2.clear()
                                c3.setData(dat[280:560])
                                c4.setData(dat[560:])
                        
                elif(x == 14):
                        try:
                                y = form.sock.recv(280*3)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.clear()
                                c2.setData(dat[:280])
                                c3.setData(dat[280:560])
                                c4.setData(dat[560:])
                        
                elif(x == 15):
                        try:
                                y = form.sock.recv(280*4)
                        except:
                                print("data not received")
                        else:
                                for d in y:
                                        data.append(ord(d))
                                dat = np.asarray(data)
                                c1.setData(dat[:280])
                                c2.setData(dat[280:560])
                                c3.setData(dat[560:840])
                                c4.setData(dat[840:])
        
        elif(Command == 0x3C):
                form.sock.send(chr(0x3C))
                try:
                        ack = form.sock.recv(1)
                except:
                        print("data not received")

                        nextCommand = 0x3C
                else:
                        if(ack == chr(0xAC)):
                            form.sendSetup()
                        else:
                            print("ACK not received")
                        nextCommand = 0x24
                
                                
        
 
app = QtGui.QApplication(sys.argv)
form = DSOApp()
timer = QtCore.QTimer()
timer.timeout.connect(loop)

p = form.graphicsView
p.showGrid(x = True, y = True)
#p.showAxis(p.axis, show = False)
p.setWindowTitle('DSO')
p.setXRange(0, 280)
p.setYRange(0, 216)
c1 = pg.PlotCurveItem(pen = 'g')
c2 = pg.PlotCurveItem(pen = 'b')
c3 = pg.PlotCurveItem(pen = 'r')
c4 = pg.PlotCurveItem(pen = '#ffa500')
#c1.paint()
c1.clear()
c2.clear()
c3.clear()
c4.clear()
p.addItem(c1)
p.addItem(c2)
p.addItem(c3)
p.addItem(c4)



def main():
    form.show()
    app.exec_()
    
def Exit():
        timer.stop()
        form.sock.close()
        app.exit()
        
def updateSetup():
        global nextCommand
        nextCommand = 0x3C
        
if __name__ == '__main__':
    main()