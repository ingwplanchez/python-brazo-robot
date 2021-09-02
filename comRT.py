# -*- coding: cp1252 -*-
#import numpy as np
import ctypes

class comRoboTalk:
    def __init__(self, nombreArchivo, direccionIP='127.0.0.1'):
        self.nombreArchivo = ctypes.c_char_p(nombreArchivo)
        self.direccionIP = ctypes.c_char_p(direccionIP)
        self.rt = ctypes.windll.RoboTalk
        self.estado = 'Iniciado'

    def conectar(self):
        indicador = self.rt.RT_Connect(self.nombreArchivo, self.direccionIP)
        if indicador==0:
            self.estado = 'Conectado'
        elif indicador==-2:
            self.estado = 'Falló conexión'

    def desconectar(self):
        indicador = self.rt.RT_Disconnect()
        if indicador==0:
            self.estado = 'Desconectado'
        elif indicador==-3:
            self.estado = 'Sin conexión'
        elif indicador==-2:
            self.estado = 'Falló desconexión'

    def sensar(self, Nombres):
        tamanoArreglo = len(Nombres)
        arregloChar = ctypes.c_char_p * tamanoArreglo
        arregloFloat = ctypes.c_float * tamanoArreglo
        nombresArt = arregloChar()
        valoresArt = arregloFloat()
        for i in range(tamanoArreglo):
            nombresArt[i] = Nombres[i]
        indicador = self.rt.RT_GetTagValues(nombresArt,valoresArt,tamanoArreglo)
        valores = []
        for i in range(tamanoArreglo):
            valores.append(valoresArt[i])
        if indicador==0:
            self.estado = 'Sin error'
        elif indicador==-3:
            self.estado = self.estado = 'Sin conexión'
        elif indicador==-5:
            self.estado = 'Falla en la lectura'
        elif indicador==-7:
            self.estado = 'Entrada inválida'
        return valores
                
    def accionar(self, Nombres, Valores):
        tamanoArreglo = len(Nombres)
        arregloChar = ctypes.c_char_p * tamanoArreglo
        arregloFloat = ctypes.c_float * tamanoArreglo
        nombresArt = arregloChar()
        valoresArt = arregloFloat()
        for i in range(tamanoArreglo):
            nombresArt[i] = Nombres[i]
            valoresArt[i] = Valores[i]
        indicador = self.rt.RT_SetTagValues(nombresArt,valoresArt,tamanoArreglo)
        if indicador==0:
            self.estado = 'Sin error'
        elif indicador==-3:
            self.estado = 'Sin conexión'
        elif indicador==-4:
            self.estado = 'Falla en la escritura'
        elif indicador==-7:
            self.estado = 'Entrada inválida'
        
        


