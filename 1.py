from tkinter import *
from tkinter import messagebox
import random
def no():
    messagebox.showinfo (' ', 'Я так и знал ')
    quit()
def motionMouse(event):
    btnn.place(x=random.randint(100, 500), y=random.randint(100, 300))
root  =  Tk()
root.geometry('400x600')
x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
y = (root.winfo_screenheight()  - root.winfo_reqwidth()) / 2
root.wm_geometry("+%d+%d" % (x,y))
root.title(' ')
root.resizable(width=False, height=False)
root['bg'] = 'white'
label = Label(root, text='Ты даун?', font='Arial 20 bold', bg='white').pack()
btnn = Button(root, text='Нет',font='Arial 20 bold')
btnn.place(x=170, y=100)
btnn.bind('<Enter>', motionMouse )
btnn = Button(root, text='Да', font='Arial 20 bold', command=no).place(x=350, y=100)
root.mainloop()