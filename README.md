# RMMS
Radioactive Medicine Management System
RMMS Is an simulated nuclear medicine management system.


#Libraries Used:
Datetime, for keeping track of time across components.
Tkinter, used for the user interface.
JSON, Datastructure.
Matplotlib/numpy, used for graphs.


#How it works.
It generates random inputs for the program to use.

Then it checks if the given amount of radioactive material is sufficient to treat all the patients.
if it's not sufficient, then it displays the patients to cancel their appointments.

There are 2 search windows.
The first is to view the amount of radioactive material (Mo-99) at any time. (Input is Datetime.)
The second is to view the amount of radioactive material (Tc-99m) in the patient at any point after their appointment. (Input patient name and Datetime.)
