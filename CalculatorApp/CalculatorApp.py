import tkinter as tk
import cmath as cm
import pyautogui 
import pygame as pg
import time 
import math
field_text=""


def add_to_field( sth ):
    global field_text
    field_text = field_text + str(sth)
    field.delete("1.0","end")
    field.insert("1.0",field_text)
def calculate():
    global filed_text
    result = str(eval(field_text))
    field.delete("1.0","end")
    field.insert("1.0",result)
def clear():
    global field_text
    field_text=""
    field.delete("1.0","end")
    field.insert("1.0",field_text)

def ln():
    global field_text
    result = int(eval(field_text))
    clear()
    e = 2.71828182846
    naturalLogaritmh = math.log(result,e)
    add_to_field(naturalLogaritmh)
    
def log(m):
    a = math.log(m,base=2)
    add_to_field(a)
    
def pow2():
    global field_text
    result = int(eval(field_text))
    clear()
    power2 = 2 ** result
    add_to_field(power2)
    
def sqrt():
    global field_text
    result = int(eval(field_text))
    clear()
    squar = math.sqrt(result)
    add_to_field(squar)
    
def factorial():
    global field_text
    result = int(eval(field_text))
    clear()
    factorial = 1
    for i in  range(result):
         factorial = factorial * (i+1)
    add_to_field(factorial)


## The scientific Mode of the Calculator app
def ScientificMode():
    window.title("Scientific")

    btn_ln=tk.Button(window, text="ln", command=lambda:ln(),width=5,font=("Times New Roman",13))
    btn_ln.grid(row=7,column=4)

    btn_sin=tk.Button(window, text="sin", command=lambda:add_to_field("sin("),width=5,font=("Times New Roman",13))
    btn_sin.grid(row=8,column=1)

    btn_cos=tk.Button(window, text="cos", command=lambda:add_to_field("cos("),width=5,font=("Times New Roman",13))
    btn_cos.grid(row=8,column=2)

    btn_pow=tk.Button(window, text="pow(", command=lambda:add_to_field("pow("),width=5,font=("Times New Roman",13))
    btn_pow.grid(row=8,column=4)
    
    btn_log=tk.Button(window, text="log()", command=lambda:add_to_field("log"),width=5,font=("Times New Roman",13))
    btn_log.grid(row=8,column=3)

    btn_2topowerof=tk.Button(window, text="2()", command=lambda:pow2(),width=5,font=("Times New Roman",13))
    btn_2topowerof.grid(row=7,column=3)

    btn_squerRoot=tk.Button(window, text="sqrt", command=lambda:sqrt(),width=5,font=("Times New Roman",13))
    btn_squerRoot.grid(row=6,column=4)

    btn_factorial=tk.Button(window, text="!", command=lambda:factorial(),width=5,font=("Times New Roman",13))
    btn_factorial.grid(row=7,column=1)

    btn_pi=tk.Button(window, text="pi", command=lambda:add_to_field("3.14159265359"),width=5,font=("Times New Roman",13))
    btn_pi.grid(row=7,column=2)

    btn_1=tk.Button(window, text="1", command=lambda:add_to_field(1),width=5,font=("Times New Roman",13))
    btn_1.grid(row=4,column=1)

    btn_2=tk.Button(window, text="2", command=lambda:add_to_field(2),width=5,font=("Times New Roman",13))
    btn_2.grid(row=4,column=2)

    btn_3=tk.Button(window, text="3", command=lambda:add_to_field(3),width=5,font=("Times New Roman",13))
    btn_3.grid(row=4,column=3)

    btn_4=tk.Button(window, text="4", command=lambda:add_to_field(4),width=5,font=("Times New Roman",13))
    btn_4.grid(row=3,column=1)

    btn_5=tk.Button(window, text="5", command=lambda:add_to_field(5),width=5,font=("Times New Roman",13))
    btn_5.grid(row=3,column=2)

    btn_6=tk.Button(window, text="6", command=lambda:add_to_field(6),width=5,font=("Times New Roman",13))
    btn_6.grid(row=3,column=3)

    btn_7=tk.Button(window, text="7", command=lambda:add_to_field(7),width=5,font=("Times New Roman",13))
    btn_7.grid(row=2,column=1)

    btn_8=tk.Button(window, text="8", command=lambda:add_to_field(8),width=5,font=("Times New Roman",13))
    btn_8.grid(row=2,column=2)

    btn_9=tk.Button(window, text="9", command=lambda:add_to_field(9),width=5,font=("Times New Roman",13))
    btn_9.grid(row=2,column=3)

    btn_plus=tk.Button(window, text="+", command=lambda:add_to_field("+"),width=5,font=("Times New Roman",13))
    btn_plus.grid(row=2,column=4)

    btn_minus=tk.Button(window, text="-", command=lambda:add_to_field("-"),width=5,font=("Times New Roman",13))
    btn_minus.grid(row=3,column=4)

    btn_multiply=tk.Button(window, text="x", command=lambda:add_to_field("*"),width=5,font=("Times New Roman",13))
    btn_multiply.grid(row=4,column=4)

    btn_divison=tk.Button(window, text="/", command=lambda:add_to_field("/"),width=5,font=("Times New Roman",13))
    btn_divison.grid(row=5,column=4)

    btn_point=tk.Button(window, text=".", command=lambda:add_to_field("."),width=5,font=("Times New Roman",13))
    btn_point.grid(row=5,column=2)

    btn_openparantese1=tk.Button(window, text="(", command=lambda:add_to_field("("),width=5,font=("Times New Roman",13))
    btn_openparantese1.grid(row=5,column=3)

    btn_openparantese2=tk.Button(window, text=")", command=lambda:add_to_field(")"),width=5,font=("Times New Roman",13))
    btn_openparantese2.grid(row=5,column=4)

    btn_equal=tk.Button(window, text="=", command=lambda:calculate(),width=5,font=("Times New Roman",13))
    btn_equal.grid(row=6,column=1)

    btn_clear=tk.Button(window, text="clear", command=lambda:clear(),width=5,font=("Times New Roman",13))
    btn_clear.grid(row=6,column=3)

    btn_scientificMode=tk.Button(window, text="Stand", command=lambda:standardMode(),width=5,font=("Times New Roman",13))
    btn_scientificMode.grid(row=6,column=2)
    

def standardMode():
    window.title("Standard")
    btn_ln.destroy()
    
    btn_1=tk.Button(window, text="1", command=lambda:add_to_field(1),width=5,font=("Times New Roman",13))
    btn_1.grid(row=4,column=1)

    btn_2=tk.Button(window, text="2", command=lambda:add_to_field(2),width=5,font=("Times New Roman",13))
    btn_2.grid(row=4,column=2)

    btn_3=tk.Button(window, text="3", command=lambda:add_to_field(3),width=5,font=("Times New Roman",13))
    btn_3.grid(row=4,column=3)

    btn_4=tk.Button(window, text="4", command=lambda:add_to_field(4),width=5,font=("Times New Roman",13))
    btn_4.grid(row=3,column=1)

    btn_5=tk.Button(window, text="5", command=lambda:add_to_field(5),width=5,font=("Times New Roman",13))
    btn_5.grid(row=3,column=2)

    btn_6=tk.Button(window, text="6", command=lambda:add_to_field(6),width=5,font=("Times New Roman",13))
    btn_6.grid(row=3,column=3)

    btn_7=tk.Button(window, text="7", command=lambda:add_to_field(7),width=5,font=("Times New Roman",13))
    btn_7.grid(row=2,column=1)

    btn_8=tk.Button(window, text="8", command=lambda:add_to_field(8),width=5,font=("Times New Roman",13))
    btn_8.grid(row=2,column=2)

    btn_9=tk.Button(window, text="9", command=lambda:add_to_field(9),width=5,font=("Times New Roman",13))
    btn_9.grid(row=2,column=3)

    btn_0=tk.Button(window, text="0", command=lambda:add_to_field(0),width=5,font=("Times New Roman",13))
    btn_0.grid(row=5,column=1)

    btn_plus=tk.Button(window, text="+", command=lambda:add_to_field("+"),width=5,font=("Times New Roman",13))
    btn_plus.grid(row=2,column=4)

    btn_minus=tk.Button(window, text="-", command=lambda:add_to_field("-"),width=5,font=("Times New Roman",13))
    btn_minus.grid(row=3,column=4)

    btn_multiply=tk.Button(window, text="x", command=lambda:add_to_field("*"),width=5,font=("Times New Roman",13))
    btn_multiply.grid(row=4,column=4)

    btn_divison=tk.Button(window, text="/", command=lambda:add_to_field("/"),width=5,font=("Times New Roman",13))
    btn_divison.grid(row=5,column=4)

    btn_point=tk.Button(window, text=".", command=lambda:add_to_field("."),width=5,font=("Times New Roman",13))
    btn_point.grid(row=5,column=2)

    btn_openparantese1=tk.Button(window, text="(", command=lambda:add_to_field("("),width=5,font=("Times New Roman",13))
    btn_openparantese1.grid(row=5,column=3)

    btn_openparantese2=tk.Button(window, text=")", command=lambda:add_to_field(")"),width=5,font=("Times New Roman",13))
    btn_openparantese2.grid(row=5,column=4)

    btn_equal=tk.Button(window, text="=", command=lambda:calculate(),width=5,font=("Times New Roman",13))
    btn_equal.grid(row=6,column=1)

    btn_clear=tk.Button(window, text="clear", command=lambda:clear(),width=5,font=("Times New Roman",13))
    btn_clear.grid(row=6,column=3)

    btn_scientificMode=tk.Button(window, text="Scient", command=lambda:ScientificMode(),width=5,font=("Times New Roman",13))
    btn_scientificMode.grid(row=6,column=2)
    


window=tk.Tk()
window.title("Calculator")
window.configure(width="300" , height="300")
window.configure(bg="White")
field = tk.Text(window,height="2",width="21",font=("Times New Roman",20))
field.grid(row="1" ,column="1", columnspan="6")

btn_ln=tk.Button(window, text="ln", command=lambda:add_to_field("ln"),width=5,font=("Times New Roman",13))
btn_log=tk.Button(window, text="log()", command=lambda:add_to_field("log"),width=5,font=("Times New Roman",13))
btn_2topowerof=tk.Button(window, text="2()", command=lambda:add_to_field("2("),width=5,font=("Times New Roman",13))
btn_squerRoot=tk.Button(window, text="sqrt", command=lambda:add_to_field("sqrt("),width=5,font=("Times New Roman",13))
btn_factorial=tk.Button(window, text="!", command=lambda:add_to_field("!"),width=5,font=("Times New Roman",13))
btn_pi=tk.Button(window, text="pi", command=lambda:add_to_field("3.14159265359"),width=5,font=("Times New Roman",13))
btn_1=tk.Button(window, text="1", command=lambda:add_to_field(1),width=5,font=("Times New Roman",13))
btn_2=tk.Button(window, text="2", command=lambda:add_to_field(2),width=5,font=("Times New Roman",13))
btn_3=tk.Button(window, text="3", command=lambda:add_to_field(3),width=5,font=("Times New Roman",13))
btn_4=tk.Button(window, text="4", command=lambda:add_to_field(4),width=5,font=("Times New Roman",13))
btn_5=tk.Button(window, text="5", command=lambda:add_to_field(5),width=5,font=("Times New Roman",13))
btn_6=tk.Button(window, text="6", command=lambda:add_to_field(6),width=5,font=("Times New Roman",13))
btn_7=tk.Button(window, text="7", command=lambda:add_to_field(7),width=5,font=("Times New Roman",13))
btn_8=tk.Button(window, text="8", command=lambda:add_to_field(8),width=5,font=("Times New Roman",13))
btn_9=tk.Button(window, text="9", command=lambda:add_to_field(9),width=5,font=("Times New Roman",13))
btn_0=tk.Button(window, text="0", command=lambda:add_to_field(0),width=5,font=("Times New Roman",13))
btn_plus=tk.Button(window, text="+", command=lambda:add_to_field("+"),width=5,font=("Times New Roman",13))
btn_minus=tk.Button(window, text="-", command=lambda:add_to_field("-"),width=5,font=("Times New Roman",13))
btn_multiply=tk.Button(window, text="x", command=lambda:add_to_field("*"),width=5,font=("Times New Roman",13))
btn_divison=tk.Button(window, text="/", command=lambda:add_to_field("/"),width=5,font=("Times New Roman",13))
btn_point=tk.Button(window, text=".", command=lambda:add_to_field("."),width=5,font=("Times New Roman",13))
btn_openparantese1=tk.Button(window, text="(", command=lambda:add_to_field("("),width=5,font=("Times New Roman",13))
btn_openparantese2=tk.Button(window, text=")", command=lambda:add_to_field(")"),width=5,font=("Times New Roman",13))
btn_equal=tk.Button(window, text="=", command=lambda:calculate(),width=5,font=("Times New Roman",13))
btn_clear=tk.Button(window, text="clear", command=lambda:clear(),width=5,font=("Times New Roman",13))
btn_scientificMode=tk.Button(window, text="Scient", command=lambda:ScientificMode(),width=5,font=("Times New Roman",8))


standardMode()
window.mainloop()