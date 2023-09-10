import random
from time import sleep




class Keithley2600():
    def __init__(self):
        pass
    
    def connect(self):
        return True
    def query(self,str):
        return "Hi im keithley, trust me."
    def disconnect(self):
        return True
    
    def pulse_script(self,pulseMax,pulseMin,nplc,tbm,V_comp):
        sleep(1000/1000)
        return ([0.0,0.001,0.0025,0.004],[0.0,pulseMax,pulseMax,0])
    
    def measure_script(self,I,AVGnum):
       return (25+random.random())
    
    