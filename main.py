from tkinter import *

gui = Tk()

l = Label( gui, text = "Entrez votre age" )
l.pack( side = LEFT )

e = Entry( gui, bd = 5 )
e.pack( side = RIGHT )

gui.mainloop()
