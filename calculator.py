# from tkinter import *

# root = Tk()
# root.title("Simple Calculater")
# e = Entry(root, width=35, borderwidth=5)
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# def button_click(number):
#     current = e.get()
#     e.delete(0,END)
#     e.insert(0, str(current) + str(number))
# def button_clear():
#     e.delete(0,END)
# def button_add():
#     first_number = e.get()
#     global f_num
#     f_num = int(first_number)
#     e.delete(0,END)
# def button_equal():
#     second_number = e.get()
#     e.delete(0, END)
#     e.insert(0, f_num + int(second_number))


# button_1 = Button(root, text="1", padx=40, pady=20, command=lambda : button_click(1))
# button_2 = Button(root, text="2", padx=40, pady=20, command=lambda : button_click(2))
# button_3 = Button(root, text="3", padx=40, pady=20, command=lambda : button_click(3))
# button_4 = Button(root, text="4", padx=40, pady=20, command=lambda : button_click(4))
# button_5 = Button(root, text="5", padx=40, pady=20, command=lambda : button_click(5))
# button_6 = Button(root, text="6", padx=40, pady=20, command=lambda : button_click(6))
# button_7 = Button(root, text="7", padx=40, pady=20, command=lambda : button_click(7))
# button_8 = Button(root, text="8", padx=40, pady=20, command=lambda : button_click(8))
# button_9 = Button(root, text="9", padx=40, pady=20, command=lambda : button_click(9))
# button_0 = Button(root, text="0", padx=40, pady=20, command=lambda : button_click(0))
# button_add = Button(root, text="+", padx=39,pady=20, command=button_add)
# button_equal = Button(root, text="=", padx=91,pady=20, command=button_equal)
# button_clear = Button(root, text="=", padx=79,pady=20, command=button_clear)  

# button_1.grid(row=3, column=0)
# button_2.grid(row=3, column=1)
# button_3.grid(row=3, column=2)

# button_4.grid(row=2, column=0)
# button_5.grid(row=2, column=1)
# button_6.grid(row=2, column=2)

# button_7.grid(row=1, column=0)
# button_8.grid(row=1, column=1)
# button_9.grid(row=1, column=2)

# button_0.grid(row=4, column=0)
# button_clear.grid(row=4, column=1, columnspan=2)
# button_add.grid(row=5, column=0)
# button_equal.grid(row=5, column=1, columnspan=2)

# root.mainloop()



import tkinter
from tkinter import *

root=Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure (bg="#17161b")

equation =""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)
    
def clear ():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate ():
    global equation
    result =""
    if equation !="":
        try:
            result = eval(equation)
        except:
            result ="error"
            equation = ""
    label_result.config(text=result)
    

label_result= Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",command=lambda: clear()). place (x=10,y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("/")). place (x=150,y=100)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("%")). place (x=290,y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("*")). place (x=430,y=100)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("7")). place (x=10,y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("8")). place (x=150,y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("9")). place (x=290,y=200)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("-")) .place(x=430,y=200)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("4")) .place(x=10,y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("5")). place (x=150,y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("6")). place (x=290,y=300)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("+")). place (x=430,y=300)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("1")). place (x=10,y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("2")). place (x=150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("3")) .place(x=290, y=400)
Button(root, text="e", width=11, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show("e")). place (x=10,y=500)

Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",command=lambda: show(".")). place (x=290,y=500)
Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037",command=lambda: calculate()) .place(x=430,y=400)

root.mainloop()