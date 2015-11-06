from gi.repository import Gtk


class MainGui:
	"GTK/Glade User interface. This is a pyGTK window"
	def __init__(self):
		self.gladefile = "calculadoraElena.glade" 
        	self.glade = Gtk.Builder()
       		self.glade.add_from_file(self.gladefile)
        	self.glade.get_object("windowCalculadora").show_all()
		signals = { "on_buttonCERO_clicked" : self.on_button0_clicked,
		"on_button1_clicked" : self.on_button1_clicked,
		"on_button2_clicked" : self.on_button2_clicked,
		"on_button3_clicked" : self.on_button3_clicked,
		"on_button4_clicked" : self.on_button4_clicked,
		"on_button5_clicked" : self.on_button5_clicked,
		"on_button6_clicked" : self.on_button6_clicked,
		"on_button7_clicked" : self.on_button7_clicked,
		"on_button8_clicked" : self.on_button8_clicked,
		"on_button9_clicked" : self.on_button9_clicked,
		"on_buttonCOMA_clicked" : self.on_buttonCOMA_clicked,
		"on_buttonSUMA_clicked" : self.on_buttonSUMA_clicked,
		"on_buttonRESTA_clicked" : self.on_buttonRESTA_clicked,
		"on_buttonMULTIP_clicked" : self.on_buttonMULTIP_clicked,
		"on_buttonDIVISION_clicked" : self.on_buttonDIVISION_clicked,
		"on_buttonIGUAL_clicked" : self.on_buttonIGUAL_clicked,
		"on_buttonBorradoTOTAL_clicked" : self.on_buttonBorradoTOTAL_clicked,
		"on_buttonBorradoPARCIAL_clicked" : self.on_buttonBorradoPARCIAL_clicked,
		"gtk_main_quit" : Gtk.main_quit }
        	self.glade.connect_signals(signals)
		self.entryVisor = self.glade.get_object("entryVisor")
		self.operacion1 = ""
		self.operador = ""
		self.operacion2 = ""
	def on_button0_clicked(self, widget):
		num = ""
		if self.entryVisor.get_text() != '':
			num = self.entryVisor.get_text()
		num += str(0)
		self.entryVisor.set_text(num)
	def on_button1_clicked(self, widget):
		num = ""
		if self.entryVisor.get_text() != '':
			num = self.entryVisor.get_text()
		num += str(1)
		self.entryVisor.set_text(num)
	def on_button2_clicked(self, widget):
		num = ""
		if self.entryVisor.get_text() != '':
			num = self.entryVisor.get_text()
		num += str(2)
		self.entryVisor.set_text(num)
	def on_button3_clicked(self, widget):
		num = ""
		if self.entryVisor.get_text() != '':
			num = self.entryVisor.get_text()
		num += str(3)
		self.entryVisor.set_text(num)
	def on_button4_clicked(self, widget):
		num = ""
		if self.entryVisor.get_text() != '':
			num = self.entryVisor.get_text()
		num += str(4)
		self.entryVisor.set_text(num)
	def on_button5_clicked(self, widget):
		num = ""
		if self.entryVisor.get_text() != '':
			num = self.entryVisor.get_text()
		num += str(5)
		self.entryVisor.set_text(num)
	def on_button6_clicked(self, widget):
		num = ""
		if self.entryVisor.get_text() != '':
			num = self.entryVisor.get_text()
		num += str(6)
		self.entryVisor.set_text(num)
	def on_button7_clicked(self, widget):
		num = ""
		if self.entryVisor.get_text() != '':
			num = self.entryVisor.get_text()
		num += str(7)
		self.entryVisor.set_text(num)
	def on_button8_clicked(self, widget):
		num = ""
		if self.entryVisor.get_text() != '':
			num = self.entryVisor.get_text()
		num += str(8)
		self.entryVisor.set_text(num)
	def on_button9_clicked(self, widget):
		num = ""
		if self.entryVisor.get_text() != '':
			num = self.entryVisor.get_text()
		num += str(9)
		self.entryVisor.set_text(num)
	def on_buttonCOMA_clicked(self, widget):
		num = ""
		if self.entryVisor.get_text() != '':
			num = self.entryVisor.get_text()
			num += str(".")
		else:
			num += str("0.")
		self.entryVisor.set_text(num)
	def on_buttonRESTA_clicked(self, widget):
		self.operacion1 = self.entryVisor.get_text()
		self.operador = "-"
		self.entryVisor.set_text("")
	def on_buttonSUMA_clicked(self, widget):
		self.operacion1 = self.entryVisor.get_text()
		self.operador = "+"
		self.entryVisor.set_text("")
	def on_buttonDIVISION_clicked(self, widget):
		self.operacion1 = self.entryVisor.get_text()
		self.operador = "/"
		self.entryVisor.set_text("")
	def on_buttonMULTIP_clicked(self, widget):
		self.operacion1 = self.entryVisor.get_text()
		self.operador = "*"
		self.entryVisor.set_text("")
	def on_buttonIGUAL_clicked(self, widget):
		calculo = 0
		self.operacion2 = self.entryVisor.get_text()
		if self.operador == "-":
			calculo = float(self.operacion1) - float(self.operacion2)
		if self.operador == "+":
			calculo = float(self.operacion1) + float(self.operacion2)
		if self.operador == "/":
			try:
				calculo = float(self.operacion1) / float(self.operacion2)
			except:
				print("error, La division por cero no esta definida")
		if self.operador == "*":
			calculo = float(self.operacion1) * float(self.operacion2)
		self.entryVisor.set_text(str(calculo))
	def on_buttonBorradoTOTAL_clicked(self,widget):
		self.entryVisor.set_text("")
		self.operacion1 = ""
		self.operacion2 = ""
		self.operador = ""
	def on_buttonBorradoPARCIAL_clicked(self,widget):
		aux = self.entryVisor.get_text()
		longitud = len(aux)
		self.entryVisor.set_text(aux[0:longitud-1])
if __name__== "__main__":
	MainGui()
	Gtk.main()
