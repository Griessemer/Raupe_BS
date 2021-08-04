#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Aug 2021

@author: Griessemer (Bernd Spitznagel)

Aufgabe des Programms:
    Siehe Uebung W.2.5 Raupe Allzeitappetit aus ´Programmieren Trainieren´
    Beschreibung in Readme_Explain.pdf

"""

from tkinter import *
master = Tk()

def circle(canvas,x,y, r, line_col, col, w = 2):
   id = canvas.create_oval(x-r, y-r, x+r, y+r, outline = line_col, fill = col, width = w)
   return id
def punkt_koords(start_koords, vers_x, vers_y):
    return [start_koords[0] + vers_x, start_koords[1] + vers_y]
def aktion_01():
    p1 = punkt_koords([150,100], 0, 0)
    p2 = punkt_koords(p1, 70, 70)
    p3 = punkt_koords(p2, 90, 15)
    p4 = punkt_koords(p3, 90, -18)
    p5 = punkt_koords(p4, 90, 15)
    p6 = punkt_koords(p5, 90, -15)

    rad = 60

    circle(w, p1[0], p1[1], rad,  "black", "lightgreen")
    circle(w, p2[0], p2[1], rad, "black", "lightgreen")
    circle(w, p3[0], p3[1], rad, "black", "lightgreen")
    circle(w, p4[0], p4[1], rad, "black", "lightgreen")
    circle(w, p5[0], p5[1], rad, "black", "lightgreen")
    circle(w, p6[0], p6[1], rad, "black", "lightgreen")

    aug1 = punkt_koords([100, 80], 0 , 0)
    aug2 = punkt_koords(aug1, 32, 0)

    circle(w, aug1[0], aug1[1], 23, "black", "white", 3.5)
    circle(w, aug2[0], aug2[1], 23.75, "black", "white", 1.35)
    circle(w, aug1[0], aug1[1], 23, "white", "white", 0.5)
    circle(w, aug1[0]+8, aug1[1], 10, "black", "black", 1.5)
    circle(w, aug2[0]-8, aug2[1], 10, "black", "black", 1.5)

def aktion_02():
    w.delete("all")


if __name__ == '__main__':
    B1 = Button(master, text="Raupe zeichnen",
                bg="green2", fg="green", font=("Times", 30), command=aktion_01)
    B1.grid(row=0, column=0, padx=10, pady=15)
    B2 = Button(master, text="Raupe loeschen",
                bg="tomato", fg="red4", font=("Times", 30), command=aktion_02)
    B2.grid(row=0, column=1, padx=10, pady=15)
    B3 = Button(master, text="QUIT",
                bg="red", fg="black", font=("Times", 30), command=master.destroy)
    B3.grid(row=2, column=0, columnspan=2, padx=15, pady=15)
    canvas_width = 800
    canvas_height = 400
    w = Canvas(master,
               width=canvas_width,
               height=canvas_height)
    w.grid(row=1, column=0, columnspan=2)

    mainloop()
