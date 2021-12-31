from tkinter import *
import time

window = Tk()
window.title("Mikael First GUI Program")
window.minsize(width=500, height=300)

# label
my_label = Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

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
button.place(x=200, y=55)


# Button
def new_button_clicked():
    my_label.config(text="Benjamin Chinwe")
    window.title("Benjamin Chinwe GUI Program")


new_button = Button(text="Benjamin Chinwe", command=new_button_clicked)
new_button.place(x=450, y=0)

# Entry
input = Entry(width=50)
input.insert(END, string="Some text to begin with.")
print(input.get())
input.grid(column=550, row=150)

window.mainloop()
