import json
import random
from datetime import datetime

class Generator():
	"""docstring for input_generator"""
	def __init__(self):
		self.cow_generator()



	"""
	Function to create a random start value/creation/arrival time for the cow.
	Writes the info to info.json
	"""
	def cow_generator(self):
		start_value = f"{str(random.randint(300, 900))} GBq"
		creation_time = self.random_time("00:30", "02:30")
		arrival_time = self.random_time("04:00", "07:00")

		data = {"cow_info": {"start_value": start_value, "creation_time": creation_time, "arrival_time": arrival_time}}

		with open("info.json", "w") as f:
			json.dump(data, f, indent=4)


	"""
	Function to create a schedule of patients.
	Creates a json file for the schedule of the week.
	"""
	def patient_scheduler_generator(self):
		pass



	"""
	Function to return a random time between 2 given times.
	return: String
	"""
	def random_time(self, start, end):
		sh, sm = start.split(":")
		s = int(sh) * 60 + int(sm)

		eh, em = end.split(":")
		e = int(eh) * 60 + int(em)

		random_minute = random.randint(s, e)

		return '{:02d}:{:02d}'.format(*divmod(random_minute, 60))