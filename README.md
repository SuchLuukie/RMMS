# RMMS
Radioactive Medicine Management System
This project is a simulation of a radioactive material management system.
It factors in decay rates/half lifes. Simulated appointments with patients and injection sizes.

# The Project
When I received the assignment from this I had no clue about anything from the topic.
The goal for the project was to simulate the decay rates of radioactive material and to be able to know at any point how much there was.
Along with some small features about patient injections and such.

# Libraries Used:
 * Datetime, for keeping track of time across components.
 * Tkinter, used for the user interface.
 * JSON, Datastructure.
 * Matplotlib/numpy, used for graphs.


# How it works.
It generates random inputs for the program to use.

Then it checks if the given amount of radioactive material is sufficient to treat all the patients.
if it's not sufficient, then it displays the patients to cancel their appointments.

There are 2 search windows.
The first is to view the amount of radioactive material (Mo-99) at any time. (Input is Datetime.)
The second is to view the amount of radioactive material (Tc-99m) in the patient at any point after their appointment. (Input patient name and Datetime.)

# Interface
Graph
![Graph](https://github.com/SuchLuukie/RMMS/blob/master/Showcase/graph.PNG?raw=true)

GUI
![GUI](https://github.com/SuchLuukie/RMMS/blob/master/Showcase/GUI.PNG?raw=true)
