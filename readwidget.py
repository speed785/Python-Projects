from tkinter import *
###################################
#Button
window = Tk()
window.title("Button")
btnCalculate = Button(window,
        text="Calculate", bg="light blue")
btnCalculate.grid(padx=75, pady=15)

###################################
#Color changing Button
def changeColor():
    if btnCalculate["fg"] == "blue":  # if caption is blue
        btnCalculate["fg"] = "red"   # change color to red
    else:
        btnCalculate["fg"] = "blue"   # change color to blue


window.title("Button")
btnCalculate = Button(window, text="Calculate",
                fg="blue", command=changeColor)
btnCalculate.grid(padx=100, pady=15)


###################################
#Read
window.title("ReadOnly Entry Widet")
conOFentOutput = StringVar()    # contents of widget
entOutput = Entry(window, state="readonly", textvariable=conOFentOutput)
entOutput2 = Entry(window, textvariable=conOFentOutput)
entOutput.grid(padx=100, pady=15)
entOutput2.grid(padx=100, pady=30)
conOFentOutput.set("Hello World!")


###################################
#Listbox
window.title("Listbox")
lstName = Listbox(window, width=10, height=5)
lstName.grid(padx=100, pady=15)
window.mainloop()