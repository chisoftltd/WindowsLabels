import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# label
my_label = tkinter.Label(text="This is a label", font=("Arial", 24, "bold"))
my_label.pack(expand=True)




window.mainloop()


def foo(a, b=4, c=6):
    print(a, b, c)


foo(4, 9)