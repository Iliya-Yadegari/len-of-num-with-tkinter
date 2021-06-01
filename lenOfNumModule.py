from tkinter import *

def num_len(num_e,w):
    num_len = len(num_e)

    res_label = Label(w,text = f'The amount of digits in your number is {num_len}').grid(row = 2,column = 0,padx = 10,pady = 10)