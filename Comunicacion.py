#Boa:Frame:Frame1

import wx
import serial

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1BUTTON3,
 wxID_FRAME1BUTTON4, wxID_FRAME1COMBOBOX1, wxID_FRAME1COMBOBOX2,
 wxID_FRAME1PANEL1, wxID_FRAME1STATICBOX1, wxID_FRAME1STATICTEXT1,
 wxID_FRAME1STATICTEXT2, wxID_FRAME1STATICTEXT3, wxID_FRAME1TEXTCTRL1,
] = [wx.NewId() for _init_ctrls in range(13)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(423, 253), size=wx.Size(383, 248),
              style=wx.MINIMIZE_BOX | wx.CAPTION | wx.CLOSE_BOX | wx.SYSTEM_MENU,
              title=u'SERIAL')
        self.SetClientSize(wx.Size(367, 210))
        self.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(367, 210),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'ENVIAR',
              name='button1', parent=self.panel1, pos=wx.Point(264, 40),
              size=wx.Size(64, 23), style=0)
        self.button1.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button1.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.button1.Bind(wx.EVT_BUTTON, self.ENVIAR, id=wxID_FRAME1BUTTON1)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel1, pos=wx.Point(120, 40), size=wx.Size(128, 21),
              style=0, value=u'')

        self.comboBox1 = wx.ComboBox(choices=[], id=wxID_FRAME1COMBOBOX1,
              name='comboBox1', parent=self.panel1, pos=wx.Point(120, 80),
              size=wx.Size(130, 21), style=0, value=u'')
        self.comboBox1.SetLabel(u'')

        self.comboBox2 = wx.ComboBox(choices=['110', '300', '1200', '2400',
              '4800', '9600', '19200'], id=wxID_FRAME1COMBOBOX2,
              name='comboBox2', parent=self.panel1, pos=wx.Point(120, 120),
              size=wx.Size(130, 21), style=0, value=u'9600')
        self.comboBox2.SetLabel(u'9600')

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label=u'COMUNICACION', name='staticBox1', parent=self.panel1,
              pos=wx.Point(16, 8), size=wx.Size(336, 184), style=0)
        self.staticBox1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.staticBox1.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticBox1.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'MENSAJE', name='staticText1', parent=self.panel1,
              pos=wx.Point(48, 40), size=wx.Size(50, 13), style=0)
        self.staticText1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.staticText1.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText1.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'PUERTO', name='staticText2', parent=self.panel1,
              pos=wx.Point(48, 80), size=wx.Size(44, 13), style=0)
        self.staticText2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.staticText2.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText2.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'BAUDIOS', name='staticText3', parent=self.panel1,
              pos=wx.Point(48, 120), size=wx.Size(51, 13), style=0)
        self.staticText3.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              u'Tahoma'))
        self.staticText3.SetForegroundColour(wx.Colour(255, 255, 255))
        self.staticText3.SetBackgroundColour(wx.Colour(0, 0, 0))

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label=u'SALIR',
              name='button2', parent=self.panel1, pos=wx.Point(192, 160),
              size=wx.Size(56, 23), style=0)
        self.button2.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.button2.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button2.Bind(wx.EVT_BUTTON, self.SALIR, id=wxID_FRAME1BUTTON2)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label=u'LIMPIAR',
              name='button3', parent=self.panel1, pos=wx.Point(120, 160),
              size=wx.Size(56, 23), style=0)
        self.button3.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.button3.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button3.Bind(wx.EVT_BUTTON, self.LIMPIAR, id=wxID_FRAME1BUTTON3)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label=u'ESCANEAR',
              name='button4', parent=self.panel1, pos=wx.Point(264, 80),
              size=wx.Size(64, 23), style=0)
        self.button4.SetForegroundColour(wx.Colour(255, 255, 255))
        self.button4.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.button4.Bind(wx.EVT_BUTTON, self.ESCANEAR, id=wxID_FRAME1BUTTON4)

    def __init__(self, parent):

        self.n = 0 # Variable que almacenara la posicion de la seleccion
        self.scom = 0 # Variable q almacenara el nombre del puerto

        self._init_ctrls(parent)

    def ENVIAR(self, event): #Boton ENVIAR

        # Obtiene la posicion de la seleccion en el comboBox1 (Puerto)
        n = self.comboBox1.GetSelection()

        # Obtine el string de la seleccion en la posicion indicada
        scom = self.comboBox1.GetString(n)

        # Obtiene la posicion de la Seleccion en el ComboBox2 (Baudios)
        n = self.comboBox2.GetSelection()
        baudb = self.comboBox2.GetString(n)

        # Configuracion del Puerto Serial con los baudios seleccionados
        self.s = serial.Serial(scom,int(baudb))

        # Se captura el texto introducido en Text1 y se almacena en
        # La variable
        Cadena = self.textCtrl1.GetValue()

        # Se envia el contenido de la variable cadena al Puerto
        self.s.write(Cadena)
        self.s.write('\r')
        self.s.close() #Se cierra el puerto
        event.Skip()

    def SALIR(self, event):
        self.Close()
        event.Skip()

    def LIMPIAR(self, event):
        self.textCtrl1.Clear()
        event.Skip()

    def ESCANEAR(self, event):  #Funcion Para escanear puertos disponibles
                                #Boton ESCANEAR
        for j in range(32): # escanea en un rango de 0 a 15 los posibles puertos
            try:
                self.s = serial.Serial(j) # Cuando se abre el puerto (Existe)
                self.comboBox1.Append(self.s.portstr) #Agrega el puerto al Combobox
                self.s.close() # Cierra el puerto
            except serial.SerialException:
                pass
        self.comboBox1.SetValue(self.s.portstr) # deja el ultimo puerto visualizado
        self.button4.Enable(False) # Deshabilita el Boton ESCANEAR
        event.Skip()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
