from tkinter import *
#James Dumitru
#Math
def addition():
    entry_3.insert(0, int(entry_1.get()) + int(entry_2.get()))
def subtraction():
    entry_3.insert(0, int(entry_1.get()) - int(entry_2.get()))
def multiply():
    entry_3.insert(0, int(entry_1.get()) * int(entry_2.get()))
def divide():
    entry_3.insert(0, int(entry_1.get()) / int(entry_2.get()))

#Window_box
window = Tk()
window.configure(background='orange')
window.title("Lab 9")
label_1 = Label(window, text="Calculator", height=3, width=10, background='orange')
label_1.pack()
label_num1=Label(window,text="1st Number", background='orange')
label_num1.pack(side=TOP)
listbox_0=Listbox(window,height=40,width=40)
listbox_0.pack()
label_num2=Label(window,text="2nd Number", background='orange')
label_num2.pack(side=TOP)
frame_1 = Frame(window)
frame_1.pack()

frame_2 = Frame(window)
frame_2.pack()

#Buttons from add, subtract, multiply and divide
button_1 = Button(frame_1, text="Add", fg="blue", command=addition)
button_1.pack(side=LEFT)
button_2 = Button(frame_1, text="Subtract", fg="blue", command=subtraction)
button_2.pack(side=RIGHT)
button_3 = Button(frame_2, text="Multiply", fg="blue", command=multiply)
button_3.pack(side=LEFT)
button_4 = Button(frame_2, text="Divide", fg="blue", command=divide)
button_4.pack(side=RIGHT)
entry_1 = Entry(listbox_0, bd=2) # 1st Text box option
entry_1.pack(side=TOP)
entry_2 = Entry(listbox_0, bd=2) # 2nd Text box option
entry_2.pack(side=TOP)
entry_3 = Listbox(window,height=10,width=20)
entry_3.pack(side=TOP)
window.mainloop()