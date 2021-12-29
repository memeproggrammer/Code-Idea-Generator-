from tkinter import*
import random
root = Tk()
root.title("Idea Generator")
root.geometry("1000x1000")
typeofprograms = ("Game", "Tool")
typeofprogram = random.choice(typeofprograms)
if typeofprogram == ("Game"):
    plots = (" Post-Apocylpse", " Multi-Universe Buisenes", " Chess But all the pieces are Jeff Bezos")
    plot = random.choice(plots)
    total = (typeofprogram) + (plot)
    idea = Label(root, text=total, font="Courier").pack()
root.mainloop()