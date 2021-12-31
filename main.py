from tkinter import *
import time

window = Tk()
window.title("Mikael First GUI Program")
window.minsize(width=800, height=400)
window.config(padx=20, pady=20)

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
button.grid(column=1, row=1)
button.config(padx=50, pady=30)


# Button
def new_button_clicked():
    my_label.config(text="Benjamin Chinwe")
    window.title("Benjamin Chinwe GUI Program")


new_button = Button(text="Benjamin Chinwe", command=new_button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=25)
input.insert(END, string="Some text to begin with.")
print(input.get())
input.grid(column=3, row=3)

window.mainloop()
