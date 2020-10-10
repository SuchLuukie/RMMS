# Import libraries.
from tkinter import *
import matplotlib

# Import files.
from input_generator import Generator
from radioactivity_calculator import Calculator
from interface import Interface
from create_graph import create_graphs

generator = Generator() #Generates all starting parameters of the simulation.
calculator = Calculator()
graphs = create_graphs(calculator)

root = Tk()
interface = Interface(root, calculator, graphs)
root.mainloop()