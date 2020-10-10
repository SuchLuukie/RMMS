import json
import math
import datetime

class Calculator():
	"""docstring for calculating radioactivity"""
	def __init__(self):
		self.info = self.loadJSON("info.json")

		self.tc99m_decay_const = 0.1151 #hour
		self.mo99_decay_const = 0.252 #day

	"""
	Function to see how much mo-99 is currently in the cow in GBq
	Parameter: datetime
	return: int
	"""
	def get_current_mo99(self, time):
		start_values = self.loadJSON("info.json")
		time_elapsed = self.elapsed_time(datetime.datetime.strptime(start_values["cow_info"]["creation_time"], "%Y/%m/%d, %H:%M:%S"), time) / 60 / 24
		#Now in days

		if time_elapsed < 0:
			return "error"

		start_value = start_values["cow_info"]["start_value"].split(" ")
		start_value = int(start_value[0])

		return int(start_value * math.exp(-self.mo99_decay_const * time_elapsed))

	"""
	Function to see how much tc-99m is avaliable in MBq.
	Parameter: datetime
	return: array of 7 elements of strings
	"""
	def get_daily_tc99(self):
		time = datetime.datetime(2020, 10, 5, 8, 0, 0)
		mo99 = self.get_current_mo99(time)

		array = []
		for i in range(7):
			array.append(round(self.get_current_mo99(time) * 0.9 * 1000))
			time += datetime.timedelta(days=1)

		return array

	"""
	Function to see how much Tc-99m is still in the patient. in MBq
	Parameter: patient name, datetime
	return: str
	"""
	def patient_tc99(self, name, time):
		registery = self.loadJSON("patients.json")
		name = name.title()

		for day in registery:
			for patient in registery[day]["schedule"]:
				if name == patient["name"]:
					time_elapsed = self.elapsed_time(datetime.datetime.strptime(patient["injection_time"], "%Y/%m/%d, %H:%M:%S"), time) / 60

					if time_elapsed < 0:
						return "error"

					start_value = patient["injection_size"].split(" ")
					start_value = int(start_value[0])
					
					return "{} {}".format(str(int(start_value * math.exp(-self.tc99m_decay_const * time_elapsed))), "MBq")

		return "Patient not found."


	"""
	Function to check if there is a enough tc-99m to treat every patient on the schedule.
	"""
	def check_if_enough_tc99(self):
		registery = self.loadJSON("patients.json")
		daily_tc99m = self.get_daily_tc99() #In MBq
		time = datetime.datetime.strptime(self.info["cow_info"]["creation_time"], "%Y/%m/%d, %H:%M:%S")

		cancel = []
		index = 0
		for day in registery:
			daily_capacity = daily_tc99m[index]
			for patient in registery[day]["schedule"]:
				appointment_time = datetime.datetime.strptime(patient["injection_time"], "%Y/%m/%d, %H:%M:%S")
				time_elapsed = self.elapsed_time(time, appointment_time) / 60
				time = appointment_time

				daily_capacity = int(daily_capacity * math.exp(-self.tc99m_decay_const * time_elapsed))

				injection_size = patient["injection_size"].split(" ")
				injection_size = int(injection_size[0])

				daily_capacity -= injection_size

				if daily_capacity < 1:
					cancel.append(patient["name"])

			index += 1
		return cancel

	"""
	Function to see how much mo-99 can be shipped to a animal hospital for their use at the end of the last appointment.
	"""
	def remaining_mo99(self):
		schedule = self.loadJSON("patients.json")
		last_appointment = datetime.datetime.strptime(schedule["sunday"]["schedule"][2]["injection_time"], "%Y/%m/%d, %H:%M:%S")
		
		return self.get_current_mo99(last_appointment)


	"""
	Function to get elapsed time between 2 times.
	parameter: string 2x
	return int (in minutes)
	"""
	def elapsed_time(self, start, end):
		duration = end - start 
		duration = duration.total_seconds() / 60

		return round(duration)


	def loadJSON(self, filename):
		with open(filename, "r") as json_file:
			return json.load(json_file)

	def writeJSON(self, filename, data):
		with open(filename, 'w') as f:
			json.dump(data, f, indent=4)
	