from tkinter import *
import lenOfNumModule as lnm



window = Tk()

main_frm = Frame(window)

num_lbl = Label(main_frm,text = 'Enter a number ===>').grid(row = 0,column = 0,padx = 10,pady = 10)
num_ent = Entry(main_frm)
submit_btn = Button(main_frm,text = 'Submit',width = 20,height = 3,command = lambda: lnm.num_len(num_ent.get(),window)).grid(row = 1,column = 0,padx = 10,pady = 10)

main_frm.grid(row = 0,column = 0,padx = 10,pady = 10)
num_ent.grid(row = 0,column = 1,padx = 10,pady = 10)

window.mainloop()