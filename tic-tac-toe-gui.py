#Tic-Tac-Toe Gui
#Coded by James Dumitru
#Notes
#So far: 
# Works: Game is playable, output messages works for winners, x and o option works. currently meant for 2 players right now.
# Needs: reset option to clear board for new game after game is done, needs player 1 mode as an option.       
# Thank you for this semester, I struggled alot, but I've really begun to like python alot now and plan on making 
# working with gui's this summer! I've really loved my time in this class. Thank you again.

from tkinter import *
from tkinter import messagebox

#Shows Instructions and Player information
#Fits perfectly in root
root=Tk()
root.title("Tic-Tac-Toe GUI")
root.geometry("450x200")

lbl=Label(root,text="Select a Tile & Get 3 in a Row to Win!",height=3, width=30,font=('Roboto','15'))
lbl.grid(row=0,column=0)
lbl=Label(root,text="Player 1: X",font=('Roboto','15'))
lbl.grid(row=1,column=0)
lbl=Label(root,text="Player 2: O",font=('Roboto','15'))
lbl.grid(row=2,column=0)

turn = 1; #For first person turn. First Player is always X!


#each button equals the box thats choosen.
# |1|2|3|
# |4|5|6|
# |7|8|9|
def spot1():
    global turn
    if button1["text"]==" ":   #Gets the X or O of a button
        if turn==1:
            turn =2;
            button1["text"]="X"
        elif turn==2:
            turn=1;
            button1["text"]="O"
        check();
def spot2():
    global turn
    if button2["text"]==" ":
        if turn==1:
            turn =2;
            button2["text"]="X"
        elif turn==2:
            turn=1;
            button2["text"]="O"
        check();
def spot3():
    global turn
    if button3["text"]==" ":
        if turn==1:
            turn =2;
            button3["text"]="X"
        elif turn==2:
            turn=1;
            button3["text"]="O"
        check();
def spot4():
    global turn
    if button4["text"]==" ":
        if turn==1:
            turn =2;
            button4["text"]="X"
        elif turn==2:
            turn=1;
            button4["text"]="O"
        check();
def spot5():
    global turn
    if button5["text"]==" ":
        if turn==1:
            turn =2;
            button5["text"]="X"
        elif turn==2:
            turn=1;
            button5["text"]="O"
        check();
def spot6():
    global turn
    if button6["text"]==" ":
        if turn==1:
            turn =2;
            button6["text"]="X"
        elif turn==2:
            turn=1;
            button6["text"]="O"
        check();
def spot7():
    global turn
    if button7["text"]==" ":
        if turn==1:
            turn =2;
            button7["text"]="X"
        elif turn==2:
            turn=1;
            button7["text"]="O"
        check();
def spot8():
    global turn
    if button8["text"]==" ":
        if turn==1:
            turn =2;
            button8["text"]="X"
        elif turn==2:
            turn=1;
            button8["text"]="O"
        check();
def spot9():
    global turn
    if button9["text"]==" ":
        if turn==1:
            turn =2;
            button9["text"]="X"
        elif turn==2:
            turn=1;
            button9["text"]="O"
        check();
popup=1;

def check():
    global popup;
    b1 = button1["text"];
    b2 = button2["text"];
    b3 = button3["text"];
    b4 = button4["text"];
    b5 = button5["text"];
    b6 = button6["text"];
    b7 = button7["text"];
    b8 = button8["text"];
    b9 = button9["text"];
    popup=popup+1;
    #Calculations for 
    if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
        win(button1["text"])
    if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
        win(button4["text"]);
    if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
        win(button7["text"]);
    if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
        win(button1["text"]);
    if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
        win(button2["text"]);
    if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
        win(button3["text"]);
    if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
        win(button1["text"]);
    if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
        win(button7["text"]);
    if popup ==10:
        messagebox.showinfo("It's a Tie! Wan't to try again?")
        root.destroy()

def win(player):
    ans = "Game complete " + player + " wins ";
    messagebox.showinfo("Congratulations", ans)
    root.destroy()  #closes right away, just need to reset board.

#All the buttons for the tic-tac-toe 3x3 areas.
button1 = Button(root, text=" ", width=3, height=1, font=('Roboto','20'), command=spot1) #<--button when spot goes to reporting def.
button1.grid(column=1, row=1) #button placement
button2 = Button(root, text=" ", width=3, height=1, font=('Roboto','20'), command=spot2)
button2.grid(column=2, row=1)
button3 = Button(root, text=" ", width=3, height=1, font=('Roboto','20'), command=spot3)
button3.grid(column=3, row=1)
button4 = Button(root, text=" ", width=3, height=1, font=('Roboto','20'), command=spot4)
button4.grid(column=1, row=2)
button5 = Button(root, text=" ", width=3, height=1, font=('Roboto','20'), command=spot5)
button5.grid(column=2, row=2)
button6 = Button(root, text=" ", width=3, height=1, font=('Roboto','20'), command=spot6)
button6.grid(column=3, row=2)
button7 = Button(root, text=" ", width=3, height=1, font=('Roboto','20'), command=spot7)
button7.grid(column=1, row=3)
button8 = Button(root, text=" ", width=3, height=1, font=('Roboto','20'), command=spot8)
button8.grid(column=2, row=3)
button9 = Button(root, text=" ", width=3, height=1, font=('Roboto','20'), command=spot9)
button9.grid(column=3, row=3)

root.mainloop()
