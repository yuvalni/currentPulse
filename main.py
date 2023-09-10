from UI.main_window_ui import Ui_MainWindow
import pyqtgraph as pg
from PySide6 import QtWidgets
from PySide6.QtCore import QTimer,QPropertyAnimation
import sys
from time import sleep

#from keithley.keithley import Keithley2600
from keithley.Mockup import Keithley2600
import pyqtgraph as pg
import numpy as np

pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.set_constraints()

        self.actionconnect.triggered.connect(self.init_keithley)
        self.actionDisconect.triggered.connect(self.disconnect_keithley)
        self.PB_pulse.clicked.connect(self.apply_pulse_and_measure)

        self.PB_measureRes.clicked.connect(self.measure_resistance)

        self.set_updateTimer()
        self.set_cooldownTimer()

        self.keithley = None
        self.init_keithley()
        self.pulseLine = self.currentPlot.plot( pen=pg.mkPen(color='k',width=2),labels={'bottom:':"time [ms]",'left': 'current [mA]'})
    
        self.resistanceLine = self.resistancePlot.plot(pen=None,symbol='o',symbolBrush=0.2)
        
        self.currents = np.empty(0)
        self.resistance = np.empty(0)

        self.pulseMax = 0

        self.measureTimer = QTimer()
        self.measureTimer.setSingleShot(True)
        self.measureTimer.timeout.connect(self.measure_resistance)

        self.inCooldown = False
        
        self.SB_NPLC.setValue(0.001)
        self.SB_pulseMax.setValue(1)
        self.SB_pulseMin.setValue(0.001)
        self.SB_tbm.setValue(20E-3)
        self.SB_voltag_comp.setValue(5)
        
        self.SB_measAVG.setValue(5)
        

    def set_constraints(self):
        self.pulseCurrentMax_cons = [0,110/1000]  #constraints in Amps!
        self.pulseCurrentMin_cons = [0,0.1/1000] #constraints in Amps!
        self.voltagecompliance_cons = [0,100]
        self.nplc_cons = [0,10]
        self.measCurr_cons = [0,0.1/1000] #0.1mA  #constraints in Amps!
        self.AVGnum_cons = [0,20]


    def set_updateTimer(self):
        self.updateTimer = QTimer()
        self.updateTimer.setInterval(10)
        self.updateTimer.timeout.connect(self.add_progressbar)

    def add_progressbar(self):
        self.PB_cooldwon.setValue(self.cooldownTimer.remainingTime()/10000*100)
        

    def set_cooldownTimer(self):
        self.cooldownTimer = QTimer()
        self.cooldownTimer.setSingleShot(True)
        self.cooldownTimer.setInterval(10*1000)#10seconds cooldown
        self.cooldownTimer.timeout.connect(self.PB_cooldwon.reset)
        self.cooldownTimer.timeout.connect(self.updateTimer.stop)
        self.cooldownTimer.timeout.connect(self.cooldown_stopped)

    def cooldown_stopped(self):
        self.inCooldown = False
        

    def print_to_status(self,string,timeout=800):
        self.statusbar.showMessage(string,timeout)
        

    def init_keithley(self):
        #self.keithley = MockUp()
        self.keithley = Keithley2600()
        if self.keithley.connect():
            self.print_to_status("Keithley connected.")
            self.print_to_status(self.keithley.query('*IDN?'),timeout=0)
            self.KeithleyConnected.setChecked(True)
        
        return True
    
    def connect_keithley(self):
        if self.keithley.connect():
            self.print_to_status("Keithley connected.")
            self.KeithleyConnected.setChecked(True)
            self.print_to_status(self.keithley.query('*IDN?'))
    def disconnect_keithley(self):
        self.keithley.disconnect()
        self.print_to_status("keithley disconnected.")
        self.KeithleyConnected.setChecked(False)
        return True


    def check_pulse_constraints(self):
        self.pulseMax = float(self.SB_pulseMax.value())/1000 #the value is now in Amps
        self.pulseMin = float(self.SB_pulseMin.value())/1000 #the value is now in Amps
        self.nplc = float(self.SB_NPLC.value())
        self.tbm = float(self.SB_tbm.value())
        self.V_comp = float(self.SB_voltag_comp.value())
    
        if self.pulseMax > max(self.pulseCurrentMax_cons) or self.pulseMax < min(self.pulseCurrentMax_cons):
            return False
        if self.pulseMin > max(self.pulseCurrentMin_cons) or self.pulseMin < min(self.pulseCurrentMin_cons):
            return False
        if self.nplc > max(self.nplc_cons) or self.nplc < min(self.nplc_cons):
            return False
        if self.V_comp > max(self.voltagecompliance_cons) or self.V_comp < min(self.voltagecompliance_cons):
            return False
        
        
        return True


    def check_measure_constraints(self):
        self.meas_curr = float(self.SP_measCurrent.value())/1000 #the value is now in Amps
        self.AVGnum = float(self.SB_measAVG.value())

        if self.AVGnum > max(self.AVGnum_cons) or self.AVGnum < min(self.AVGnum_cons):
            return False
        if self.meas_curr > max(self.measCurr_cons) or self.meas_curr < min(self.measCurr_cons):
            return False
        return True

    def apply_pulse_and_measure(self):
        ##check constraints
        if self.inCooldown:
            ret = QtWidgets.QMessageBox.question(self,"In cool down mode","Are you sure you want another pulse?")
            if ret == QtWidgets.QMessageBox.No: #or ret == QtWidgets.QMessageBox.No:
                self.print_to_status("Pulse aborted")
                return False
        if not self.check_pulse_constraints():
            self.statusbar.showMessage("Bad pulse Parameter",timeout=0)
            return False

        self.statusbar.showMessage("Applying pulse.",timeout=0)
        t,I = self.keithley.pulse_script(self.pulseMax,self.pulseMin,self.nplc,self.tbm,self.V_comp)
        self.inCooldown = True

        self.pulseLine.setData(t,I)

        #self.measure_resistance()
        self.measureTimer.setInterval(self.SB_waitBFmeas.value())  
        self.measureTimer.start() ## this will call the measurement function after a delay
        
        
        self.cooldownTimer.start()
        self.updateTimer.start()

        return True


    def measure_resistance(self):
        if not self.check_measure_constraints():
            self.statusbar.showMessage("Bad measurement Parameter",timeout=0)
            return False
        Res = self.keithley.measure_script(self.meas_curr,self.AVGnum)
        self.currents = np.append(self.currents,self.pulseMax)
        self.resistance = np.append(self.resistance,Res)
        
        self.resistanceLine.setData(self.currents,self.resistance)

        self.print_to_status("Resistance measured.")
        return True

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()