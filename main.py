from tkinter import *


def bmi():
        bmi = float(weight_entry.get()) / (float(Height_entry.get()) * float(Height_entry.get()))
        label_text.set(bmi)

        if bmi < 18:
            return "your underweight "
        elif bmi >= 18 and 25:
            return "normal"
        elif bmi >= 25 < 30:
            return "overweight"
        else:
            return "Obese"


def clear():
    weight_entry.delete(0, END)
    Height_entry.delete(0, END)
    age_entry.delete(0, END)

def exit():
    return root.destroy()

root = Tk()
label_text = StringVar()
clicked = StringVar()

root.geometry("800x600")

frame_1 = Frame(root, width=100, highlightbackground='black', highlightthickness=2)
frame_1.grid(row=0, column=0, padx=20, pady=20, ipadx=20, ipady=20)
weight_label = Label(frame_1, text="Weight:")
height_label = Label(frame_1, text="height:")
kilograms_label = Label(frame_1, text="kilograms")
cm_label = Label(frame_1, text="CM")
gender_label = Label(frame_1, text="Gender:")
age_label = Label(frame_1, text="Age")
drop = OptionMenu(frame_1, clicked, "Male", "Female")

weight_entry = Entry(frame_1)
Height_entry = Entry(frame_1)
age_entry = Entry(frame_1)

weight_label.grid(row=3, column=0)
weight_entry.grid(row=3, column=2)
kilograms_label.grid(row=3, column=3)
height_label.grid(row=5, column=0)
Height_entry.grid(row=5, column=2)
cm_label.grid(row=5, column=3)
gender_label.grid(row=6, column=0)
drop.grid(row=6, column=2)
age_label.grid(row=6, column=4)
age_entry.grid(row=6, column=5)

calculate_button = Button(root, text="calculate your ideal Body Mass Index", width=50, command=bmi)
calculate_button.grid(row=7, column=0, sticky=W+E+N+S)
add = Label(root, text="", textvariable=label_text).grid(row=8, column=1, sticky=W)

BMI_label = Label(root, text="BMI:")
BMI_label.grid(row=8, column=0)
Ideal_label = Label(root, text="ideal :")
Ideal_label.grid(row=8, column=2)

clear = Button(root, text="clear", command=clear)
clear.grid(row=10, column=0)

exit_button = Button(root, text="exit program", command=exit)
exit_button.grid(row=10, column=2)

mainloop()