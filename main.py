from tkinter import *
import time

window = Tk()
window.title("Mikael First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "Emmanuel Chinwe"
my_label.config(text="Emmanuel Chinwe")


# Button

def button_clicked():
    my_label.config(text="Benjamin Chinwe")
    window.title("Benjamin Chinwe GUI Program")
    time.sleep(5)
    print(f"{input.get()}")
    my_label.config(text=input.get())


button = Button(text="Shepherd Chinwe", command=button_clicked)
button.pack()

# Entry
input = Entry(width=50)
input.insert(END, string="Some text to begin with.")
print(input.get())
input.pack()

# Text
text = Text(height=5, width=30)
# Put cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

window.mainloop()
