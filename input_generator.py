import json
import random
import datetime

class Generator():
	"""docstring for input_generator"""
	def __init__(self):
		self.cow_generator()
		self.empty_schedule()

		self.patient_scheduler_generator()



	"""
	Function to create a random start value/creation/arrival time for the cow.
	Writes the info to info.json
	"""
	def cow_generator(self):
		start_value = f"{str(random.randint(300, 900))} GBq"
		creation_time = self.random_time("00:30", "02:30").split(":")
		arrival_time = self.random_time("04:00", "07:00").split(":")
		date = datetime.datetime(2020, 10, 5).date()


		creation_time = datetime.datetime.combine(date, datetime.time(int(creation_time[0]), int(creation_time[1])))
		arrival_time = datetime.datetime.combine(date, datetime.time(int(arrival_time[0]), int(arrival_time[1])))

		data = {"cow_info": {"start_value": start_value, "creation_time": creation_time.strftime("%Y/%m/%d, %H:%M:%S"), "arrival_time": arrival_time.strftime("%Y/%m/%d, %H:%M:%S")}}

		with open("info.json", "w") as f:
			json.dump(data, f, indent=4)



	"""
	Function to create a schedule of patients.
	Creates a json file for the schedule of the week.
	"""
	def patient_scheduler_generator(self):
		with open("patients.json", "r") as json_file:
			schedule = json.load(json_file)
		schedule = schedule["schedule"]


		date = datetime.datetime(2020, 10, 4).date()
		for day in schedule:
			date += datetime.timedelta(1)
			time = "08:00"

			for patient in range(schedule[day]["max_patients"]):
				injection_time = "{}:00".format(self.random_time(time, self.add_time(time, 30))).split(":")
				injection_time = datetime.datetime.combine(date, datetime.time(int(injection_time[0]), int(injection_time[1])))

				appointment_time = "{}:00".format(time).split(":")
				appointment_time = datetime.datetime.combine(date, datetime.time(int(appointment_time[0]), int(appointment_time[1])))

				patient_dict = {
					"name": self.random_name(),
					"appointment_time": appointment_time.strftime("%Y/%m/%d, %H:%M:%S"),
					"injection_time": injection_time.strftime("%Y/%m/%d, %H:%M:%S"),
					"injection_size": self.random_injection_size()
				}
				schedule[day]["schedule"].append(patient_dict)

				time = self.random_time(self.add_time(time, 40), self.add_time(time, 50))



		with open("patients.json", "w") as f:
			json.dump(schedule, f, indent=4)



	"""
	Function to create a random injection size for a patient.
	Parameters: 300-740 MBq
	return: string
	"""
	def random_injection_size(self):
		size = random.randint(300, 740)
		return "{} MBq".format(size)


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


	"""
	Function to add a certain amount of time to a military time in minutes.
	Parameter: string, string
	return: string
	"""
	def add_time(self, time, minutes):
		th, tm = time.split(":")
		t = int(th) * 60 + int(tm) + minutes

		return '{:02d}:{:02d}'.format(*divmod(t, 60))


	"""
	Function to create an empty schedule for the patient scheduler
	"""
	def empty_schedule(self):
		with open("empty_schedule.json", "r") as json_file:
			empty = json.load(json_file)

		with open("patients.json", "w") as f:
			json.dump(empty, f, indent=4)


	"""
	Function to get a random full name
	return: string
	"""
	def random_name(self):
		with open("names/first_names.json", "r") as json_file:
			first = json.load(json_file)

		with open("names/last_names.json", "r") as json_file:
			last = json.load(json_file)

		return "{} {}".format(random.choice(first), random.choice(last).lower().capitalize())