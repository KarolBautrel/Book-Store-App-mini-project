from tkinter import *
from tkinter import ttk
import backend

window = Tk()
card = ttk.Frame(window, style='Card.TFrame', padding=(5, 6, 7, 8))
window.call("source", "sun-valley.tcl")
window.call("set_theme", "dark")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

titleText = StringVar()
e1 = Entry(window, textvariable=titleText)
e1.grid(row=0, column=1)

authorText = StringVar()
e2 = Entry(window, textvariable=authorText)
e2.grid(row=0, column=3)

yearText = StringVar()
e3 = Entry(window, textvariable=yearText)
e3.grid(row=1, column=1)

ISBNtext = StringVar()
e4 = Entry(window, textvariable=ISBNtext)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=10, width=30)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = ttk.Scrollbar(window)  # stworzenie scrollbara

sb1.grid(column=2, row=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)  # przypisanie go do listboxa
sb1.configure(command=list1.yview)  # przypisanie go zeby byl w osi y listboxa

b1 = ttk.Button(window, text="View all", width=12, style="Toggle.TButton", command=pass)
b1.grid(row=2, column=3)

b2 = ttk.Button(window, text="Search entry", width=12, style="Toggle.TButton")
b2.grid(row=3, column=3)

b3 = ttk.Button(window, text="Add entry", width=12, style="Toggle.TButton")
b3.grid(row=4, column=3)

b4 = ttk.Button(window, text="Update", width=12, style="Toggle.TButton")
b4.grid(row=5, column=3)

b5 = ttk.Button(window, text="Delete", width=12, style="Toggle.TButton")
b5.grid(row=6, column=3)

b6 = ttk.Button(window, text="Close", width=12, style="Toggle.TButton")
b6.grid(row=7, column=3)


window.mainloop()
