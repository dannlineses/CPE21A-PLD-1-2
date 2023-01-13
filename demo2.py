from tkinter import *
window = Tk()
window.geometry("300x200+10+20")

window.title("My first python GUI")

lbl = Label(window, text= "Mt first UI Python Program", fg = "red", font =("Verdana,16"))
lbl.place(x = 60, y = 70)

btn = Button(window,text = "Submit", bg="Blue")
btn.place(x=80, y=100)


txtfld = Entry(window,text="This is an entry widget", bd = 5)
txtfld.place(x = 70, y=90)

def sel():
	selection = "You selected" + str(var.get())
	label.config(text = selection)

var = IntVar()
r1 = Radiobutton(window,text="Male", variants = var, value = 1, command = sel)
r1.pack(anchor = W)

r2 = Radiobutton(window,text="Female", variants = var, value = 2, command = sel)
r2.pack(anchor = E)


label = Label(window)
label.pack()
window.mainloop()