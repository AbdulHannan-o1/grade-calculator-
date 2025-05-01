# using tkinker to create a GUI for the program
import tkinter as tk
from tkinter import Button, Text, messagebox
def calculate():

    numbers = int(marksEntry.get()) # here marksEntry is the entry widget where user will enter the marks
    total_marks =int(totalMarks.get()) # here totalMarks is the entry widget where user will enter the total marks
    percentage = round(numbers / total_marks * 100 ,2)  #here round is used to round the percentage to 2 decimal places

    # print (f"Your percentage is {percentage} %")

    if percentage >= 90 and percentage <= 100:
        result=(" A+")
    elif percentage >= 80:
        result=(" A")
    elif percentage >= 70:
        result=(" B+")
    elif percentage >= 60:
        result=(" B")
    elif percentage >= 50:
        result=(" C+")
    elif percentage >= 40:
        result=(" C")
    elif percentage <= 30:
        result=("better luck next time")
    else:
        result=("Invalid percentage")

    # show result in the GUI
    result_label.config(text=f"Your percentage is {percentage} %\n your grade is {result}")

# main application(GUI)
app = tk.Tk()
app.title("Grade Calculator")
app.geometry("200x200")

tk.Label(app, text="Enter your obtained marks:").pack()
marksEntry = tk.Entry(app)
marksEntry.pack()

tk.Label(app, text="Enter your total marks:").pack()
totalMarks = tk.Entry(app)
totalMarks.pack()

# creating button to run the program 
calculate_btn = tk.Button(app, text= "Clalculate" , command=calculate)
calculate_btn.pack(pady= 10)

result_label = tk.Label(app, text="" , fg="blue")
result_label.pack()

# starting the application
app.mainloop()
