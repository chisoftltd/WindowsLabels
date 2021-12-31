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
input = Entry(width=10)
input.pack()

window.mainloop()
