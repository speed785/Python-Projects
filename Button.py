from tkinter import *

window = Tk()
window.title("Button")
btnCalculate = Button(window,
        text="Calculate", bg="light blue")
btnCalculate.grid(padx=75, pady=15)
window.mainloop()



def changeColor():
    if btnCalculate["fg"] == "blue":  # if caption is blue
        btnCalculate["fg"] = "red"   # change color to red
    else:
        btnCalculate["fg"] = "blue"   # change color to blue

window = Tk()
window.title("Button")
btnCalculate = Button(window, text="Calculate",
                fg="blue", command=changeColor)
btnCalculate.grid(padx=100, pady=15)
window.mainloop()