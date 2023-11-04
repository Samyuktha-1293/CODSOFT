from tkinter import *

sym=n1=n2=NONE

def num(n1):
    prev=show['text']
    new=prev + str(n1)
    show.config(text=new)


  
def clearscreen():
    show.config(text='')

def operator(op):
    global n1,sym
    n1=int(show['text'])
    sym=op
    show.config(text='')

def output():
    global n1,sym,n2
    n2=int(show['text'])
    if sym=='+':
        show.config(text=(n1+n2))
    elif sym=='-':
        show.config(text=(n1-n2))
    elif sym=='*':
        show.config(text=(n1*n2))
    else:
        if n2==0:
            show.config(text='INVALID SYNTAX')
        else:
            show.config(text=(n1/n2))

scr=Tk()
scr.title("Calculator")
scr.geometry("328x480")
scr.configure(bg='peachpuff')

show=Label(scr,font=('verdana',25),text='',bg='peachpuff',fg='black')
show.grid(row=0,column=0,columnspan=10,sticky='w',pady=(55,30))

button1=Button(scr,font=('verdana',14),text='1',bg='plum',fg='black',width=6,height=3,command=lambda:num(1))
button1.grid(row=1,column=0)

button2=Button(scr,font=('verdana',14),text='2',bg='plum',fg='black',width=6,height=3,command=lambda:num(2))
button2.grid(row=1,column=1)

button3=Button(scr,font=('verdana',14),text='3',bg='plum',fg='black',width=6,height=3,command=lambda:num(3))
button3.grid(row=1,column=2)

b_mul=Button(scr,font=('verdana',14),text='*',bg='blueviolet',fg='black',width=6,height=3,command=lambda:operator('*'))
b_mul.grid(row=3,column=3)

button4=Button(scr,font=('verdana',14),text='4',bg='plum',fg='black',width=6,height=3,command=lambda:num(4))
button4.grid(row=2,column=0)

button5=Button(scr,font=('verdana',14),text='5',bg='plum',fg='black',width=6,height=3,command=lambda:num(5))
button5.grid(row=2,column=1)

button6=Button(scr,font=('verdana',14),text='6',bg='plum',fg='black',width=6,height=3,command=lambda:num(6))
button6.grid(row=2,column=2)

b_substraction=Button(scr,font=('verdana',14),text='-',bg='blueviolet',fg='black',width=6,height=3,command=lambda:operator('-'))
b_substraction.grid(row=2,column=3)

button7=Button(scr,font=('verdana',14),text='7',bg='plum',fg='black',width=6,height=3,command=lambda:num(7))
button7.grid(row=3,column=0)

button8=Button(scr,font=('verdana',14),text='8',bg='plum',fg='black',width=6,height=3,command=lambda:num(8))
button8.grid(row=3,column=1)

button9=Button(scr,font=('verdana',14),text='9',bg='plum',fg='black',width=6,height=3,command=lambda:num(9))
button9.grid(row=3,column=2)

b_addition=Button(scr,font=('verdana',14),text='+',bg='blueviolet',fg='black',width=6,height=3,command=lambda:operator('+'))
b_addition.grid(row=1,column=3)

button0=Button(scr,font=('verdana',14),text='0',bg='plum',fg='black',width=6,height=3,command=lambda:num(0))
button0.grid(row=4,column=1)

b_clear=Button(scr,font=('verdana',14),text='AC',bg='magenta',fg='black',width=6,height=3,command=lambda:clearscreen())
b_clear.grid(row=4,column=0)

b_equal=Button(scr,font=('verdana',14),text='=',bg='blueviolet',fg='black',width=6,height=3,command=lambda:output())
b_equal.grid(row=4,column=2)

b_division=Button(scr,font=('verdana',14),text='/',bg='blueviolet',fg='black',width=6,height=3,command=lambda:operator('/'))
b_division.grid(row=4,column=3)

scr.mainloop()