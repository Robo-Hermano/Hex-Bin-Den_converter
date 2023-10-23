import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import random
#introductions
#red = "\033[31m"
#blue = "\033[34m"
#green = "\033[32m"
introtext = "Welcome to codenames! This game of four teaches people to find the connections between words while making sure the fun remains.\nTwo teams of two duke it out. One player must use the colour board to help the other place the blue cards on words their own.\nIf you are the first player, you must say a word not in the grid and state how many words it relates to, using the colour board of the word grid.\nIf you are the second player, you must use this to pick cards that are blue (for team one) or red (for team two).\nWords that are blue give team one a point, red gives team two a point, and both changes turn if other side chooses them.\nGreen words do nothing, and the one black word makes the picking side lose.\nEnjoy this game, and glhf!"
#create boards, make this more varied afterwards
def create_board():
    board = [[],[],[],[],[]]
    lst = [
'Poison','Unicorn','Opera','Princess','Wall',
'Atlantis','Maple','Night','Bed','Smuggler',
'Temple','Thief','Dance','Plot','Mail',
'Berry','Trunk','Africa','State','Carrot',
'Eagle','Ketchup','Novel','Racket','America',
"apple", "banana", "dog", "elephant",
"fire", "guitar", "house", "island", "jazz",
"kangaroo", "lamp", "mountain", "notebook", "ocean",
"penguin", "quasar", "rainbow", "saxophone", "tiger",
"umbrella", "violin", "waterfall", "xylophone", "yoga",
"zeppelin", "astronomy", "butterfly", "chocolate", "diamond"
]
    for i in range(5):
        for j in range(5):
            a = random.randint(0,len(lst)-1)
            board[i].append(lst[a])
            lst.remove(lst[a])
    return board
board = create_board()
#for colour linking to real board, crucial for the game
def create_couleur():
    couleur = [[],[],[],[],[]]
    lst = []
    for i in range(8):
        lst.append("green")
        lst.append("blue")
        lst.append("red")
    lst.append("black")
    for i in range(5):
        for j in range(5):
            a = random.randint(0,len(lst)-1)
            couleur[i].append(lst[a])
            lst.remove(lst[a])
    return couleur
couleur = create_couleur()
class Codenames:
    #easier to run functions one by one starting with __init__
    def __init__(self):
        #create the template to play the game on
        self.master = Tk()
        self.master.geometry("500x500")
        self.master.state("zoomed")
        self.master.title("Codenames")
        self.intros = Label(self.master, text=introtext+"\nNow firstly input player names per single text box; adjacent names will be in same teams\nand first and third will use the colour board and the others will choose words",font=("Calibri",20))
        self.intros.pack()
        #to register names, make the game more authentic
        self.nam1 = Text(self.master, height = 1)
        self.nam2 = Text(self.master, height = 1)
        self.nam3 = Text(self.master, height = 1)
        self.nam4 = Text(self.master, height = 1)
        self.nam1.pack()
        self.nam2.pack()
        self.nam3.pack()
        self.nam4.pack()
        self.slam = Button(self.master, text = "click here to save names and procede",command=self.next)
        self.slam.pack()
    def next(self):
        self.slam.forget()
        self.nom1 = self.nam1.get("1.0", "end-1c")
        self.nam1.forget()
        self.nom2 = self.nam2.get("1.0", "end-1c")
        self.nam2.forget()
        self.nom3 = self.nam3.get("1.0", "end-1c")
        self.nam3.forget()
        self.nom4 = self.nam4.get("1.0", "end-1c")
        self.nam4.forget()
        self.revel = Button(self.master,text="colour board reveal, only "+self.nom1+" and "+self.nom3+" should see!",command=self.show_couleur)
        self.revel.pack()
    def show_couleur(self):
        #for a player in each team to save, using their phone maybe?
        self.revel.config(state=DISABLED)
        self.fram = Frame(self.master)
        for i in range(5):
            self.fram.columnconfigure(i,weight=0)
        for i in range(5):
            for j in range(5):
                zum = Button(self.fram,text=couleur[i][j])
                zum.grid(row=i,column=j,sticky=W+E)
        self.fram.pack(expand=True)
        self.forgor = Button(self.master,text="click here once both players have a way to remember it; first to 8 points or not choose the black card wins!",command=self.start)
        self.forgor.pack()
    def start(self):
        #this stuff isn't needed anymore
        self.intros.forget()
        self.revel.forget()
        self.forgor.forget()
        self.fram.forget()
        #for turns of teams
        self.turn = 2
        self.number = 0
        self.checker = Label(self.master,text=self.nom2+"'s turn. What number did "+self.nom1+" say? Enter on textbox (only change this number when the turn changes)",font=("Calibri",20))
        self.checker.pack()
        self.totot = Text(self.master,height=1)
        self.totot.pack()
        #the five by five word grid
        self.grid = Frame(self.master)
        for i in range(5):
            self.grid.columnconfigure(i,weight=0)
        self.zum1 = Button(self.grid,text=board[0][0],command=lambda:self.button_click(self.zum1,0,0))
        self.zum1.grid(row=0,column=0,sticky=W+E)
        self.zum2 = Button(self.grid,text=board[0][1],command=lambda:self.button_click(self.zum2,0,1))
        self.zum2.grid(row=0,column=1,sticky=W+E)
        self.zum3 = Button(self.grid,text=board[0][2],command=lambda:self.button_click(self.zum3,0,2))
        self.zum3.grid(row=0,column=2,sticky=W+E)
        self.zum4 = Button(self.grid,text=board[0][3],command=lambda:self.button_click(self.zum4,0,3))
        self.zum4.grid(row=0,column=3,sticky=W+E)
        self.zum5 = Button(self.grid,text=board[0][4],command=lambda:self.button_click(self.zum5,0,4))
        self.zum5.grid(row=0,column=4,sticky=W+E)
        self.zum6 = Button(self.grid,text=board[1][0],command=lambda:self.button_click(self.zum6,1,0))
        self.zum6.grid(row=1,column=0,sticky=W+E)
        self.zum7 = Button(self.grid,text=board[1][1],command=lambda:self.button_click(self.zum7,1,1))
        self.zum7.grid(row=1,column=1,sticky=W+E)
        self.zum8 = Button(self.grid,text=board[1][2],command=lambda:self.button_click(self.zum8,1,2))
        self.zum8.grid(row=1,column=2,sticky=W+E)
        self.zum9 = Button(self.grid,text=board[1][3],command=lambda:self.button_click(self.zum9,1,3))
        self.zum9.grid(row=1,column=3,sticky=W+E)
        self.zum10 = Button(self.grid,text=board[1][4],command=lambda:self.button_click(self.zum10,1,4))
        self.zum10.grid(row=1,column=4,sticky=W+E)
        self.zum11 = Button(self.grid,text=board[2][0],command=lambda:self.button_click(self.zum11,2,0))
        self.zum11.grid(row=2,column=0,sticky=W+E)
        self.zum12 = Button(self.grid,text=board[2][1],command=lambda:self.button_click(self.zum12,2,1))
        self.zum12.grid(row=2,column=1,sticky=W+E)
        self.zum13 = Button(self.grid,text=board[2][2],command=lambda:self.button_click(self.zum13,2,2))
        self.zum13.grid(row=2,column=2,sticky=W+E)
        self.zum14 = Button(self.grid,text=board[2][3],command=lambda:self.button_click(self.zum14,2,3))
        self.zum14.grid(row=2,column=3,sticky=W+E)
        self.zum15 = Button(self.grid,text=board[2][4],command=lambda:self.button_click(self.zum15,2,4))
        self.zum15.grid(row=2,column=4,sticky=W+E)
        self.zum16 = Button(self.grid,text=board[3][0],command=lambda:self.button_click(self.zum16,3,0))
        self.zum16.grid(row=3,column=0,sticky=W+E)
        self.zum17 = Button(self.grid,text=board[3][1],command=lambda:self.button_click(self.zum17,3,1))
        self.zum17.grid(row=3,column=1,sticky=W+E)
        self.zum18 = Button(self.grid,text=board[3][2],command=lambda:self.button_click(self.zum18,3,2))
        self.zum18.grid(row=3,column=2,sticky=W+E)
        self.zum19 = Button(self.grid,text=board[3][3],command=lambda:self.button_click(self.zum19,3,3))
        self.zum19.grid(row=3,column=3,sticky=W+E)
        self.zum20 = Button(self.grid,text=board[3][4],command=lambda:self.button_click(self.zum20,3,4))
        self.zum20.grid(row=3,column=4,sticky=W+E)
        self.zum21 = Button(self.grid,text=board[4][0],command=lambda:self.button_click(self.zum21,4,0))
        self.zum21.grid(row=4,column=0,sticky=W+E)
        self.zum22 = Button(self.grid,text=board[4][1],command=lambda:self.button_click(self.zum22,4,1))
        self.zum22.grid(row=4,column=1,sticky=W+E)
        self.zum23 = Button(self.grid,text=board[4][2],command=lambda:self.button_click(self.zum23,4,2))
        self.zum23.grid(row=4,column=2,sticky=W+E)
        self.zum24 = Button(self.grid,text=board[4][3],command=lambda:self.button_click(self.zum24,4,3))
        self.zum24.grid(row=4,column=3,sticky=W+E)
        self.zum25 = Button(self.grid,text=board[4][4],command=lambda:self.button_click(self.zum25,4,4))
        self.zum25.grid(row=4,column=4,sticky=W+E)
        self.grid.pack(expand=True)
        self.p1, self.p2, self.checky = 0,0,0
        self.one = Label(self.master,text=self.nom1+" and "+self.nom2+"'s points: "+str(self.p1),font=("Calibri",20))
        self.one.pack()
        self.two = Label(self.master,text=self.nom3+" and "+self.nom4+"'s points: "+str(self.p2),font=("Calibri",20))
        self.two.pack()
        self.three = Label(self.master,text="for stating what colour each cards is",font=("Calibri",20))
        self.three.pack()
    def button_click(self, button, row, col):
        #to change points when players choose a word
        self.bruv = self.totot.get("1.0","end-1c")
        self.number += 1
        if couleur[row][col] == "blue":
            self.p1 += 1
            self.one.config(text=self.nom1+" and "+self.nom2+"'s points: "+str(self.p1),font=("Calibri",20))
            self.three.config(text="blue card, "+self.nom1+" and "+self.nom2+" gets a point",font=("Calibri",20))
            if self.turn == 5:
                self.turn = 2
                self.number = 0
                self.checker.config(text=self.nom2+"'s turn. What number did "+self.nom1+" say?",font=("Calibri",20))
            elif int(self.bruv) == self.number:
                self.turn = 5
                self.number = 0
                self.checker.config(text=self.nom4+"'s turn. What number did "+self.nom3+" say?",font=("Calibri",20))
        elif couleur[row][col] == "red":
            self.p2 += 1
            self.two.config(text=self.nom3+" and "+self.nom4+"'s points: "+str(self.p2))
            self.three.config(text="red card, "+self.nom3+" and "+self.nom4+" gets a point")
            if self.turn == 2:
                self.turn = 5
                self.number = 0
                self.checker.config(text=self.nom4+"'s turn. What number did "+self.nom3+" say?")
            elif int(self.bruv)==self.number:
                self.turn = 2
                self.number = 0
                self.checker.config(text=self.nom2+"'s turn. What number did "+self.nom1+" say?")
        elif couleur[row][col] == "black":
            self.checker.forget()
            self.grid.forget()
            self.one.forget()
            self.two.forget()
            self.three.forget()
            self.totot.forget()
            if self.turn == 5:
                self.e = Label(self.master,text="Black card, "+self.nom1+" and "+self.nom2+" have won!",font=("Calibri",20))
                self.e.pack(expand=True)
            else:
                self.e = Label(self.master,text="Black card, "+self.nom3+" and "+self.nom4+" have won!",font=("Calibri",20))
                self.e.pack(expand=True)
        else:
            self.three.config(text="green card, nothing happens")
            if int(self.bruv) == self.number:
                self.turn = 10/self.turn
                self.number = 0
                if self.turn == 2:
                    self.checker.config(text=self.nom2+"'s turn. What number did "+self.nom1+" say?",font=("Calibri",20))
                else:
                    self.checker.config(text=self.nom4+"'s turn. What number did "+self.nom3+" say?",font=("Calibri",20))
        button.config(state=DISABLED)
        self.check_win()
        #to check if a team wins
    def check_win(self):
        if self.p1 == 8:
            self.show_winner(self.nom1,self.nom2)
        elif self.p2 == 8:
            self.show_winner(self.nom3,self.nom4)
    def show_winner(self, player, playor):
        #and now, celebration for one and devastation for the other
        self.checker.forget()
        self.totot.forget()
        self.grid.forget()
        self.one.forget()
        self.two.forget()
        self.three.forget()
        win_label = Label(self.master, text=player+" and "+playor+" have reached 8 points and won!",font=("Calibri",20))
        win_label.pack(expand=True)
#time to finally run the class
Codenames().master.mainloop()
