from tkinter import *
from tkinter import ttk
import backend

# Function for selecting rows in listbox


def get_selected_row(event):  # event is an special parameter for func in bind method

        global selected_tuple
        # pointing at index of row in listbox, [0] means frist element in tuple
        index = list1.curselection()[0]
        # from the list1 get the tuple saved in index

        selected_tuple = list1.get(index)

        e1.delete(0, END)  # clearing widget
        # filing entry one with title which is second element of tuple
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    return (selected_tuple)
# function for view button


def view_command():
    list1.delete(0, END)  # deleting everytime we execute again button
    for row in backend.view():  # iterating throufh view method
        # listbox has special insert method(END,row) row will be added at the end
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)  # clearing list
    # variables with StringVar with get method will display text we want.
    for row in backend.search(titleText.get(), authorText.get(), yearText.get(), ISBNtext.get()):
        list1.insert(END, row)


def insert_command():
    backend.insert(titleText.get(), authorText.get(),
                   yearText.get(), ISBNtext.get())  # inserting all arguments
    list1.delete(0, END)
    list1.insert(END, (titleText.get(), authorText.get(),  # shows already added title
                       yearText.get(), ISBNtext.get()))


def delete_command():
    backend.delete(selected_tuple[0])  # 0 is an number Id of element


def update_command():
    backend.update(selected_tuple[0], titleText.get(), authorText.get(),
                   yearText.get(), ISBNtext.get())  # adding 5 variables from backend update func


window = Tk()

window.wm_title("Bookstore")
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

list1 = Listbox(window, height=10, width=40)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = ttk.Scrollbar(window)  # stworzenie scrollbara

sb1.grid(column=2, row=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)  # przypisanie go do listboxa
sb1.configure(command=list1.yview)  # przypisanie go zeby byl w osi y listboxa

# Bind is an methos (firstargument, function)
list1.bind('<<ListboxSelect>>', get_selected_row)


b1 = ttk.Button(window, text="View all", width=12,
                style="Toggle.TButton", command=view_command)
b1.grid(row=2, column=3)

b2 = ttk.Button(window, text="Search entry", width=12,
                style="Toggle.TButton", command=search_command)
b2.grid(row=3, column=3)

b3 = ttk.Button(window, text="Add entry", width=12,
                style="Toggle.TButton", command=insert_command)
b3.grid(row=4, column=3)


b4 = ttk.Button(window, text="Update", width=12,
                style="Toggle.TButton", command=update_command)
b4.grid(row=5, column=3)

b5 = ttk.Button(window, text="Delete", width=12,
                style="Toggle.TButton", command=delete_command)
b5.grid(row=6, column=3)

b6 = ttk.Button(window, text="Close", width=12,
                style="Toggle.TButton", command=window.destroy)
b6.grid(row=7, column=3)

print(list1)

window.mainloop()
