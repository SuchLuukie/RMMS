# libraries
import matplotlib.pyplot as plt
import numpy as np
import datetime

class create_graphs():
	"""docstring for Graphs"""
	def __init__(self, calculator):
		self.calculator = calculator


	def mo99_graph(self):
		info = self.calculator.loadJSON("info.json")
		time = datetime.datetime.strptime(info["cow_info"]["creation_time"], "%Y/%m/%d, %H:%M:%S")

		x, y = [], []
		for i in range(0, 144):
			value = self.calculator.get_current_mo99(time)
			time = time + datetime.timedelta(hours=1)

			x.append(i)
			y.append(value)

		plt.plot(x, y)
		plt.ylabel("Mo-99 (GBq)")
		plt.xlabel("Time (Hours)")
		plt.show()