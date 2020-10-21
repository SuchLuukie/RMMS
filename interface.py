from tkinter import *
from tkinter.messagebox import showerror

import datetime

class Interface():
	"""docstring for Interface"""
	def __init__(self, master, calculator, graphs):
		self.master = master
		self.calculator = calculator
		self.graphs = graphs

		self.create_widgets()
		

	def create_widgets(self):
		self.master.geometry("700x400")


		self.patient_input_name = Entry(self.master)
		self.patient_input_time = Entry(self.master)
		self.patient_input_button = Button(self.master, text="Submit", command=self.patient)
		self.patient_label = Label(self.master, text="Patient Remaining Radioactive Material")
		self.patient_output = Text(self.master)

		self.patient_input_name.insert(END, "Name")
		self.patient_input_time.insert(END, "yyyy/mm/dd, hh:mm:ss")

		self.patient_input_name.place(x=50, y=50)
		self.patient_input_time.place(x=50, y=70)
		self.patient_input_button.place(x=80, y=90)
		self.patient_label.place(x=10, y=30)
		self.patient_output.place(x=50, y=130, width=120, height=20)

		#----------------------------------------------------------------------------------------------------------

		self.graph_button = Button(self.master, text="Graph", command=self.graphs.mo99_graph)
		self.graph_button.place(x=500, y=50)

		#----------------------------------------------------------------------------------------------------------

		self.radioactive_material_time = Entry(self.master)
		self.radioactive_material_button = Button(self.master, text="Retrieve", command=self.radioactive_material)
		self.radioactive_material_label = Label(self.master, text="Retrieve Radioactive Material in Cow")
		self.radioactive_material_output = Text(self.master)

		self.radioactive_material_time.insert(END, "yyyy/mm/dd, hh:mm:ss")

		self.radioactive_material_time.place(x=300, y=50)
		self.radioactive_material_button.place(x=330, y=70)
		self.radioactive_material_label.place(x=270, y=30)
		self.radioactive_material_output.place(x=300, y=100, width=120, height=20)


		array = self.calculator.check_if_enough_tc99()
		string = "Appointments to cancel: \n"
		for item in array:
			string += item
			string += "\n"

		self.cancel_output = Label(self.master, text=string)

		self.cancel_output.place(x=50, y=200)


	def patient(self):
		time = self.patient_input_time.get()
		name = self.patient_input_name.get()

		try:
			time = datetime.datetime.strptime(time, "%Y/%m/%d, %H:%M:%S")

		except:
			showerror(title=None, message="Wrong date format, use: yyyy/m/d, h:m:s")
			return

		value = self.calculator.patient_tc99(name, time)

		if value == "Patient not found.":
			showerror(title=None, message="The given time is before the injection time of the patient.")
			return

		self.patient_output.delete(1.0, "end")
		self.patient_output.insert(1.0, value)



	def radioactive_material(self):
		time = self.radioactive_material_time.get()

		try:
			time = datetime.datetime.strptime(time, "%Y/%m/%d, %H:%M:%S")

		except:
			showerror(title=None, message="Wrong date format, use: yyyy/m/d, h:m:s")
			return

		value = self.calculator.get_current_mo99(time)

		if value == "error":
			showerror(title=None, message="The given time is before the cow's creation time.")
			return

		self.radioactive_material_output.delete(1.0, "end")
		self.radioactive_material_output.insert(1.0, str(value) + " GBq")
			