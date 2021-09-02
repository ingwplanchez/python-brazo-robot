# -*- coding: cp1252 -*-
from math import sin,cos
from cmath import pi

class BrazoRobotico:
    def __init__(self, theta=[]):
##    def __init__(self, theta=[], d=[], a=[], alpha=[]):
        self.theta = theta[:]
        
##        self.d =  d[:]
##        self.a = a[:]
##        self.alpha = alpha[:]
##        
##    def calcularCD(self):
##        #cinematica directa de la posicion
##        aux = pi/180
##        self.p = []
##        self.p.append(self.a[0]*cos(self.theta[0]*aux) + self.a[1]*cos((self.theta[0]+self.theta[1])*aux))
##        self.p.append(self.a[0]*sin(self.theta[0]*aux) + self.a[1]*sin((self.theta[0]+self.theta[1])*aux))
##
##    def reiniciar(self):
##        for i in range(len(self.theta)):
##            self.theta[i] = 0.0
##        self.calcularCD()
