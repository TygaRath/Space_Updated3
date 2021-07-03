import tkinter
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *


screen = tk.Tk()
screen.title("High Scores")
screen.configure(background="grey")
screen.iconbitmap("icon.ico")
screen.geometry("600x600")

mycur = mysql.connector.connect(
    host="localhost",
    user="root",
    password="toor",)
cur = mycur.cursor()

cur.execute("CREATE DATABASE game_data_7")
cur.execute("USE game_data_7")
cur.execute("CREATE TABLE Scores (UserName VARCHAR(50), Score INTEGER(5), Date date)")

s1 = "INSERT INTO Scores(UserName, Score, Date) VALUES(%s, %s, %s)"
f = open('texting')
data = f.readlines()
for line in data:
    word=line.split()
    if word == []:
        continue
    a=word[0]
    b=word[1]
    c=word[2]
    d1=(a,b,c)
    cur.execute(s1, d1)
    mycur.commit()
f.close()

def update(rows):
    for i in rows:
        trv.insert("", 'end', values=i)

def clear():
    cur.execute("SELECT NULL FROM Scores")
    rows=cur.fetchall()
    update(rows)


wrapper1 =LabelFrame(screen, text="Leaderboard")
wrapper2 = LabelFrame(screen, text="Clear")
wrapper1.pack(fill='both', expand='yes', padx=20, pady=10)

trv = ttk.Treeview(wrapper1, columns=(1,2,3), show='headings', height='6')
trv.pack()

trv.heading(1, text="UserName")
trv.heading(2, text="Scores")
trv.heading(3, text="Date")

cur.execute("SELECT * FROM Scores ORDER BY Score DESC")
rows=cur.fetchall()
update(rows)

cbtn=Button(screen, text="Clear", command=clear)
cbtn.place(x=300, y=400)

def delet():
    import os
    os.remove('texting')
    cur.execute("DROP TABLE Scores")
    quit()

b = tkinter.Button(screen, text="Delete Leaderboard", font=('cambria', 15), fg="black", bg="white", command=clear)
b.place(x=234, y=344)

screen.mainloop()
