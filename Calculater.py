from tkinter import *
window=Tk()
window.title(" Calculater")
window.geometry("400x400")
window.config(bg="Lightyellow")

val=""
data=StringVar()
def btn_click(number):
    global val
    val = val+ str(number)
    data.set(val)


def btn_clear():
    global val
    val=""
    data.set(val)


def btn_equal():
    global val
    val = str(eval(val))
    data.set(val)


text=Entry(window,font=('Arial',20,'bold'),bd=20,justify='right',bg='lightblue',textvariable=data)
text.grid(row=0,columnspan=4)
btn=Button(window,text="9",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click(9))
btn.grid(row=1,column=0)
btn=Button(window,text="8",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click(8))
btn.grid(row=1,column=1)
btn=Button(window,text="7",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click(7))
btn.grid(row=1,column=2)
btn=Button(window,text="+",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click('+'))
btn.grid(row=1,column=3)


btn=Button(window,text="6",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click(6))
btn.grid(row=2,column=0)
btn=Button(window,text="5",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click(5))
btn.grid(row=2,column=1)
btn=Button(window,text="4",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click(4))
btn.grid(row=2,column=2)
btn=Button(window,text="*",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click('*'))
btn.grid(row=2,column=3)


btn=Button(window,text="3",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click(3))
btn.grid(row=3,column=0)
btn=Button(window,text="2",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click(2))
btn.grid(row=3,column=1)
btn=Button(window,text="1",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click(1))
btn.grid(row=3,column=2)
btn=Button(window,text="-",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click('-'))
btn.grid(row=3,column=3)

btn=Button(window,text="CE",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_clear())
btn.grid(row=4,column=0)
btn=Button(window,text="0",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click(0))
btn.grid(row=4,column=1)
btn=Button(window,text="/",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_click('/'))
btn.grid(row=4,column=2)
btn=Button(window,text="=",font=('Arial',20,'bold'),bd=10,width=3,command=lambda :btn_equal())
btn.grid(row=4,column=3)

window.mainloop()