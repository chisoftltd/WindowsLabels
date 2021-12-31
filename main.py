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
#Put cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()


window.mainloop()
