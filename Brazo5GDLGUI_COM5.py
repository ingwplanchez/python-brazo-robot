#Boa:Frame:Frame1

import wx
import cinematicaBrazo5GDL as B5GDL
import comRT
import serial
import time
#import Modulo

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3,
 wxID_FRAME1CHECKBOX1, wxID_FRAME1COMBOBOX1, wxID_FRAME1COMBOBOX2,
 wxID_FRAME1PANEL1, wxID_FRAME1RADIOBUTTON1, wxID_FRAME1RADIOBUTTON2,
 wxID_FRAME1SLIDER1, wxID_FRAME1SLIDER2, wxID_FRAME1SLIDER3,
 wxID_FRAME1SLIDER4, wxID_FRAME1SLIDER5, wxID_FRAME1SPINCTRL1,
 wxID_FRAME1SPINCTRL2, wxID_FRAME1SPINCTRL3, wxID_FRAME1SPINCTRL4,
 wxID_FRAME1SPINCTRL5, wxID_FRAME1STATICBOX1, wxID_FRAME1STATICBOX2,
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10, wxID_FRAME1STATICTEXT11,
 wxID_FRAME1STATICTEXT12, wxID_FRAME1STATICTEXT13, wxID_FRAME1STATICTEXT2,
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5,
 wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, wxID_FRAME1STATICTEXT8,
 wxID_FRAME1STATICTEXT9,
] = [wx.NewId() for _init_ctrls in range(35)]

class Frame1(wx.Frame):
    def _init_sizers(self):
        # generated method, don't edit
        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

        self.button3.SetSizer(self.boxSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(552, 114), size=wx.Size(455, 439),
              style=wx.MINIMIZE_BOX | wx.CAPTION | wx.CLOSE_BOX | wx.SYSTEM_MENU,
              title=u'BRAZO_5GDL')
        self.SetClientSize(wx.Size(439, 401))
        self.SetBackgroundColour(wx.Colour(192, 192, 192))
        self.Show(True)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(439, 401),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.panel1.SetForegroundColour(wx.Colour(0, 0, 0))
        self.panel1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'MOVIMIENTOS POR EJES', name='staticBox1',
              parent=self.panel1, pos=wx.Point(24, 16), size=wx.Size(224, 296),
              style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.staticBox1.SetForegroundColour(wx.Colour(0, 0, 0))
        self.staticBox1.SetBackgroundColour(wx.Colour(128, 128, 128))

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'SALIR',
              name='button3', parent=self.panel1, pos=wx.Point(304, 280),
              size=wx.Size(88, 23), style=0)
        self.button3.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.button3.SetForegroundColour(wx.Colour(0, 0, 0))
        self.button3.SetBackgroundStyle(wx.BG_STYLE_SYSTEM)
        self.button3.Bind(wx.EVT_BUTTON, self.SALIR, id=wxID_FRAME1BUTTON3)

        self.slider1 = wx.Slider(id=wxID_FRAME1SLIDER1, maxValue=360,
              minValue=0, name='slider1', parent=self.panel1, pos=wx.Point(48,
              56), size=wx.Size(104, 24), style=wx.SL_HORIZONTAL, value=0)
        self.slider1.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.slider1.Bind(wx.EVT_SCROLL, self.OnSlider1Scroll)

        self.slider2 = wx.Slider(id=wxID_FRAME1SLIDER2, maxValue=100,
              minValue=-15, name='slider2', parent=self.panel1, pos=wx.Point(48,
              104), size=wx.Size(104, 24), style=wx.SL_HORIZONTAL, value=45)
        self.slider2.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.slider2.Bind(wx.EVT_SCROLL, self.OnSlider2Scroll)

        self.slider3 = wx.Slider(id=wxID_FRAME1SLIDER3, maxValue=100,
              minValue=-130, name='slider3', parent=self.panel1,
              pos=wx.Point(48, 152), size=wx.Size(104, 24),
              style=wx.SL_HORIZONTAL, value=45)
        self.slider3.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.slider3.Bind(wx.EVT_SCROLL, self.OnSlider3Scroll)

        self.slider4 = wx.Slider(id=wxID_FRAME1SLIDER4, maxValue=130,
              minValue=-100, name='slider4', parent=self.panel1,
              pos=wx.Point(48, 200), size=wx.Size(104, 24),
              style=wx.SL_HORIZONTAL, value=45)
        self.slider4.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.slider4.Bind(wx.EVT_SCROLL, self.OnSlider4Scroll)

        self.slider5 = wx.Slider(id=wxID_FRAME1SLIDER5, maxValue=360,
              minValue=0, name='slider5', parent=self.panel1, pos=wx.Point(48,
              248), size=wx.Size(104, 24), style=wx.SL_HORIZONTAL, value=0)
        self.slider5.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.slider5.Bind(wx.EVT_SCROLL, self.OnSlider5Scroll)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1, label=u'-',
              name='staticText1', parent=self.panel1, pos=wx.Point(200, 56),
              size=wx.Size(24, 13), style=0)
        self.staticText1.SetForegroundColour(wx.Colour(0, 0, 0))
        self.staticText1.SetBackgroundColour(wx.Colour(128, 128, 128))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2, label=u'-',
              name='staticText2', parent=self.panel1, pos=wx.Point(200, 112),
              size=wx.Size(24, 13), style=0)
        self.staticText2.SetForegroundColour(wx.Colour(0, 0, 0))

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3, label=u'-',
              name='staticText3', parent=self.panel1, pos=wx.Point(200, 160),
              size=wx.Size(24, 13), style=0)
        self.staticText3.SetForegroundColour(wx.Colour(0, 0, 0))

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4, label=u'-',
              name='staticText4', parent=self.panel1, pos=wx.Point(200, 208),
              size=wx.Size(24, 16), style=0)
        self.staticText4.SetForegroundColour(wx.Colour(0, 0, 0))

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5, label=u'-',
              name='staticText5', parent=self.panel1, pos=wx.Point(200, 256),
              size=wx.Size(24, 13), style=0)
        self.staticText5.SetForegroundColour(wx.Colour(0, 0, 0))

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'EJE 1', name='staticText6', parent=self.panel1,
              pos=wx.Point(56, 40), size=wx.Size(28, 13), style=0)
        self.staticText6.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.staticText6.SetForegroundColour(wx.Colour(0, 0, 0))

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'EJE2', name='staticText7', parent=self.panel1,
              pos=wx.Point(56, 88), size=wx.Size(25, 13), style=0)
        self.staticText7.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.staticText7.SetForegroundColour(wx.Colour(0, 0, 0))

        self.staticText8 = wx.StaticText(id=wxID_FRAME1STATICTEXT8,
              label=u'EJE 3', name='staticText8', parent=self.panel1,
              pos=wx.Point(56, 136), size=wx.Size(28, 13), style=0)
        self.staticText8.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.staticText8.SetForegroundColour(wx.Colour(0, 0, 0))

        self.staticText9 = wx.StaticText(id=wxID_FRAME1STATICTEXT9,
              label=u'EJE 4', name='staticText9', parent=self.panel1,
              pos=wx.Point(56, 184), size=wx.Size(28, 13), style=0)
        self.staticText9.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.staticText9.SetForegroundColour(wx.Colour(0, 0, 0))

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'EJE 5', name='staticText10', parent=self.panel1,
              pos=wx.Point(56, 232), size=wx.Size(28, 13), style=0)
        self.staticText10.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))
        self.staticText10.SetForegroundColour(wx.Colour(0, 0, 0))

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label=u'VALORES', name='staticText11', parent=self.panel1,
              pos=wx.Point(184, 32), size=wx.Size(50, 13), style=0)
        self.staticText11.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))
        self.staticText11.SetForegroundColour(wx.Colour(0, 0, 0))

        self.radioButton1 = wx.RadioButton(id=wxID_FRAME1RADIOBUTTON1,
              label=u'CONECTAR', name='radioButton1', parent=self.panel1,
              pos=wx.Point(32, 328), size=wx.Size(81, 13), style=0)
        self.radioButton1.SetForegroundColour(wx.Colour(0, 0, 0))
        self.radioButton1.SetValue(True)
        self.radioButton1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))
        self.radioButton1.Bind(wx.EVT_RADIOBUTTON, self.CONECTAR,
              id=wxID_FRAME1RADIOBUTTON1)

        self.radioButton2 = wx.RadioButton(id=wxID_FRAME1RADIOBUTTON2,
              label=u'DESCONECTAR', name='radioButton2', parent=self.panel1,
              pos=wx.Point(32, 352), size=wx.Size(96, 13), style=0)
        self.radioButton2.SetForegroundColour(wx.Colour(0, 0, 0))
        self.radioButton2.SetValue(True)
        self.radioButton2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))
        self.radioButton2.Bind(wx.EVT_RADIOBUTTON, self.DESCONECTAR,
              id=wxID_FRAME1RADIOBUTTON2)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'INICIALIZAR',
              name='button1', parent=self.panel1, pos=wx.Point(56, 280),
              size=wx.Size(88, 23), style=0)
        self.button1.SetForegroundColour(wx.Colour(0, 0, 0))
        self.button1.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.button1.Bind(wx.EVT_BUTTON, self.REINICIAR, id=wxID_FRAME1BUTTON1)

        self.staticBox2 = wx.StaticBox(id=wxID_FRAME1STATICBOX2,
              label=u'VALORES INICIALES', name='staticBox2', parent=self.panel1,
              pos=wx.Point(272, 16), size=wx.Size(144, 296), style=0)
        self.staticBox2.SetForegroundColour(wx.Colour(0, 0, 0))
        self.staticBox2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))

        self.spinCtrl1 = wx.SpinCtrl(id=wxID_FRAME1SPINCTRL1, initial=0,
              max=100, min=0, name='spinCtrl1', parent=self.panel1,
              pos=wx.Point(288, 56), size=wx.Size(117, 21),
              style=wx.SP_ARROW_KEYS)

        self.spinCtrl2 = wx.SpinCtrl(id=wxID_FRAME1SPINCTRL2, initial=0,
              max=100, min=0, name='spinCtrl2', parent=self.panel1,
              pos=wx.Point(288, 104), size=wx.Size(117, 21),
              style=wx.SP_ARROW_KEYS)

        self.spinCtrl3 = wx.SpinCtrl(id=wxID_FRAME1SPINCTRL3, initial=0,
              max=100, min=0, name='spinCtrl3', parent=self.panel1,
              pos=wx.Point(288, 152), size=wx.Size(117, 21),
              style=wx.SP_ARROW_KEYS)

        self.spinCtrl4 = wx.SpinCtrl(id=wxID_FRAME1SPINCTRL4, initial=0,
              max=100, min=0, name='spinCtrl4', parent=self.panel1,
              pos=wx.Point(288, 200), size=wx.Size(117, 21),
              style=wx.SP_ARROW_KEYS)

        self.spinCtrl5 = wx.SpinCtrl(id=wxID_FRAME1SPINCTRL5, initial=0,
              max=100, min=0, name='spinCtrl5', parent=self.panel1,
              pos=wx.Point(288, 240), size=wx.Size(117, 21),
              style=wx.SP_ARROW_KEYS)

        self.checkBox1 = wx.CheckBox(id=wxID_FRAME1CHECKBOX1,
              label=u'COMUNICACI\xd2N', name='checkBox1', parent=self.panel1,
              pos=wx.Point(32, 376), size=wx.Size(104, 13), style=0)
        self.checkBox1.SetValue(False)
        self.checkBox1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.checkBox1.Show(True)
        self.checkBox1.Bind(wx.EVT_CHECKBOX, self.COMUNICACION,
              id=wxID_FRAME1CHECKBOX1)

        self.comboBox1 = wx.ComboBox(choices=[], id=wxID_FRAME1COMBOBOX1,
              name='comboBox1', parent=self.panel1, pos=wx.Point(280, 328),
              size=wx.Size(130, 21), style=0, value=u'COM1')
        self.comboBox1.SetLabel(u'COM1')

        self.comboBox2 = wx.ComboBox(choices=['110', '300', '1200', '2400',
              '4800', '9600', '19200' ], id=wxID_FRAME1COMBOBOX2,
              name='comboBox2', parent=self.panel1, pos=wx.Point(280, 368),
              size=wx.Size(130, 21), style=0, value=u'9600')
        self.comboBox2.SetLabel(u'9600')

        self.staticText12 = wx.StaticText(id=wxID_FRAME1STATICTEXT12,
              label=u'PUERTO', name='staticText12', parent=self.panel1,
              pos=wx.Point(216, 328), size=wx.Size(44, 13), style=0)

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label=u'BAUDIOS', name='staticText13', parent=self.panel1,
              pos=wx.Point(216, 368), size=wx.Size(51, 13), style=0)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'AUTOM\xc0TICO',
              name='button2', parent=self.panel1, pos=wx.Point(144, 280),
              size=wx.Size(88, 23), style=0)
        self.button2.SetBackgroundColour(wx.Colour(128, 128, 128))
        self.button2.Bind(wx.EVT_BUTTON, self.AUTOMATICO, id=wxID_FRAME1BUTTON2)

        self._init_sizers()

    def __init__(self, parent):

        # Archivo De Roboworks Brazo5GDL

        self.com = comRT.comRoboTalk('Brazo5GDL')

        # Vector Para el movimiento de los 5 Ejes (Objeto BR)
        #Inicializacion del objeto BR de la clase BrazoRobotico
        self.BR = B5GDL.BrazoRobotico(theta=[0.0,0.0,0.0,0.0,0.0])

        # VARIABLES PARA LA COMUNICACION
        self.n = 0 # Variable que almacenara la posicion de la seleccion
        self.scom = 0 # Variable q almacenara el nombre del puerto
        self.escanear = 0 # Variable que permite escanear los puertos solo una vez
        #self.enlace = self.checkBox1.GetValue()
        self._init_ctrls(parent)

    def SALIR(self, event): # Boton SALIR
        self.Close()
        event.Skip()

    def OnSlider1Scroll(self, event): # BASE (EJE 1)

        Capturar1 = event.GetEventObject()
        Asignar1 = Capturar1.GetValue()
        self.staticText1.SetLabel(str(Asignar1))

        self.BR.theta[0] = float(self.slider1.GetValue())

        self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        n = self.comboBox1.GetSelection()
        scom = self.comboBox1.GetString(n)
        n = self.comboBox2.GetSelection()
        baudb = self.comboBox2.GetString(n)
        self.s = serial.Serial(scom,int(baudb))
        Cadena = "1"
        self.s.write(Cadena)
        self.s.write('\r')
        self.s.close()

        event.Skip()

    def OnSlider2Scroll(self, event): # EJE 2

        Capturar2 = event.GetEventObject()
        Asignar2 = Capturar2.GetValue()
        self.staticText2.SetLabel(str(Asignar2))

        self.BR.theta[1] = float(self.slider2.GetValue())

        self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        n = self.comboBox1.GetSelection()
        scom = self.comboBox1.GetString(n)
        n = self.comboBox2.GetSelection()
        baudb = self.comboBox2.GetString(n)
        self.s = serial.Serial(scom,int(baudb))
        Cadena = "2"
        self.s.write(Cadena)
        self.s.write('\r')
        self.s.close()
        event.Skip()

    def OnSlider3Scroll(self, event): # EJE 3

        Capturar3 = event.GetEventObject()
        Asignar3 = Capturar3.GetValue()
        self.staticText3.SetLabel(str(Asignar3))

        self.BR.theta[2] = float(self.slider3.GetValue())

        self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        n = self.comboBox1.GetSelection()
        scom = self.comboBox1.GetString(n)
        n = self.comboBox2.GetSelection()
        baudb = self.comboBox2.GetString(n)
        self.s = serial.Serial(scom,int(baudb))
        Cadena = "3"
        self.s.write(Cadena)
        self.s.write('\r')
        self.s.close()

        event.Skip()

    def OnSlider4Scroll(self, event): # EJE 4

        Capturar4 = event.GetEventObject()
        Asignar4 = Capturar4.GetValue()
        self.staticText4.SetLabel(str(Asignar4))

        self.BR.theta[3] = float(self.slider4.GetValue())

        self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        n = self.comboBox1.GetSelection()
        scom = self.comboBox1.GetString(n)
        n = self.comboBox2.GetSelection()
        baudb = self.comboBox2.GetString(n)
        self.s = serial.Serial(scom,int(baudb))
        Cadena = "4"
        self.s.write(Cadena)
        self.s.write('\r')
        self.s.close()

        event.Skip()

    def OnSlider5Scroll(self, event): # EJE 5

        Capturar5 = event.GetEventObject()
        Asignar5 = Capturar5.GetValue()
        self.staticText5.SetLabel(str(Asignar5))

        self.BR.theta[4] = float(self.slider5.GetValue())

        self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        n = self.comboBox1.GetSelection()
        scom = self.comboBox1.GetString(n)
        n = self.comboBox2.GetSelection()
        baudb = self.comboBox2.GetString(n)
        self.s = serial.Serial(scom,int(baudb))
        Cadena = "5"
        self.s.write(Cadena)
        self.s.write('\r')
        self.s.close()

        event.Skip()

    def CONECTAR(self, event):

        self.com.conectar()

        n = self.comboBox1.GetSelection()
        scom = self.comboBox1.GetString(n)
        n = self.comboBox2.GetSelection()
        baudb = self.comboBox2.GetString(n)
        self.s = serial.Serial(scom,int(baudb))
        Cadena = "Roboworks Conectado"
        self.s.write(Cadena)
        self.s.write('\r')
        self.s.close()

        event.Skip()

    def DESCONECTAR(self, event):
        self.com.desconectar()

        n = self.comboBox1.GetSelection()
        scom = self.comboBox1.GetString(n)
        n = self.comboBox2.GetSelection()
        baudb = self.comboBox2.GetString(n)
        self.s = serial.Serial(scom,int(baudb))
        Cadena = "Roboworks Desconectado"
        self.s.write(Cadena)
        self.s.write('\r')
        self.s.close()

        event.Skip()

    def REINICIAR(self, event):

        # POSICION INICIAL DE LOS EJES EN ANGULOS
        self.BR.theta[0] = self.spinCtrl1.GetValue()
        self.BR.theta[1] = self.spinCtrl2.GetValue()
        self.BR.theta[2] = self.spinCtrl3.GetValue()
        self.BR.theta[3] = self.spinCtrl4.GetValue()
        self.BR.theta[4] = self.spinCtrl5.GetValue()

        # VALORES EN ANGULOS DE LAS ETIQUETAS QUE MUESTRAN LOS ANGULOS
        self.staticText1.SetLabel(str(self.BR.theta[0]))
        self.staticText2.SetLabel(str(self.BR.theta[1]))
        self.staticText3.SetLabel(str(self.BR.theta[2]))
        self.staticText4.SetLabel(str(self.BR.theta[3]))
        self.staticText5.SetLabel(str(self.BR.theta[4]))

        # INICIALIZACION DE LOS SLIDERS
        self.slider1.SetValue(self.BR.theta[0])
        self.slider2.SetValue(self.BR.theta[1])
        self.slider3.SetValue(self.BR.theta[2])
        self.slider4.SetValue(self.BR.theta[3])
        self.slider5.SetValue(self.BR.theta[4])

        self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        event.Skip()

    def COMUNICACION(self, event):
        if self.checkBox1.GetValue(): # Si el check esta en True
            if self.escanear == 0: # escanear si escanear = 0
                # ESCANEAR PUERTOS
                for j in range(15): # escanea en un rango de 0 a 15 los posibles puertos
                    try:
                        self.s = serial.Serial(j) # Cuando se abre el puerto (Existe)
                        self.comboBox1.Append(self.s.portstr) #Agrega el puerto al Combobox
                        self.s.close() # Cierra el puerto
                    except serial.SerialException:
                        pass
                self.comboBox1.SetValue(self.s.portstr) # deja el ultimo puerto visualizado
            self.escanear = 1
        event.Skip()

    def AUTOMATICO(self, event):
        #self.com.conectar()

        self.BR.theta[0] = 0
        self.BR.theta[1] = 45
        self.BR.theta[2] = 45
        self.BR.theta[3] = 45
        self.BR.theta[4] = 0

        self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)
        Eje1 = self.BR.theta[0]
        Eje2 = self.BR.theta[1]
        Eje3 = self.BR.theta[2]
        Eje4 = self.BR.theta[3]

	n = self.comboBox1.GetSelection()
        scom = self.comboBox1.GetString(n)
        n = self.comboBox2.GetSelection()
        baudb = self.comboBox2.GetString(n)
        self.s = serial.Serial(scom,int(baudb))
        Cadena = 'a' # Envio al pic la se?al para activar el modo automatico
        self.s.write(Cadena)
        self.s.write('\r')
        self.s.close()

        while Eje1 <= 90:

            Eje1 = Eje1 + 1
            self.BR.theta[0] = Eje1
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje2 <= 100:

            Eje2 = Eje2 + 1
            self.BR.theta[1] = Eje2
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje3 >= -130:

            Eje3 = Eje3 - 1
            self.BR.theta[2] = Eje3
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje4 <= 130:

            Eje4 = Eje4 + 1
            self.BR.theta[3] = Eje4
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje1 <= 270:

            Eje1 = Eje1 + 1
            self.BR.theta[0] = Eje1
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje4 >= 100:

            Eje4 = Eje4 - 1
            self.BR.theta[3] = Eje4
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje2 >= 90:

            Eje2 = Eje2 - 1
            self.BR.theta[1] = Eje2
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje4 >= 45:

            Eje4 = Eje4 - 1
            self.BR.theta[3] = Eje4
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje3 <= 45:

            Eje3 = Eje3 + 1
            self.BR.theta[2] = Eje3
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

            Eje2 = Eje2 - 1
            self.BR.theta[1] = Eje2
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje1 >= 180:

            Eje1 = Eje1 - 1
            self.BR.theta[0] = Eje1
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje2 <= 90:

            Eje2 = Eje2 + 1
            self.BR.theta[1] = Eje2
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje2 >= 45:

            Eje2 = Eje2 - 1
            self.BR.theta[1] = Eje2
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje1 >= 90:

            Eje1 = Eje1 - 1
            self.BR.theta[0] = Eje1
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje2 <= 90:

            Eje2 = Eje2 + 1
            self.BR.theta[1] = Eje2
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje2 >= 45:

            Eje2 = Eje2 - 1
            self.BR.theta[1] = Eje2
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        while Eje1 >= 0:

            Eje1 = Eje1 - 1
            self.BR.theta[0] = Eje1
            #time.sleep(0.1)
            self.com.accionar(['RotacionDBase','EJE1','EJE2','EJE3','EJE4',], self.BR.theta)

        event.Skip()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
