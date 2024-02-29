from tkinter import *
from math import *
from tkinter.messagebox import *

convert_constant = 1
inverse_convert_constant = 1


def fsin(arg):
    return sin(arg * convert_constant)


def fcos(arg):
    return cos(arg * convert_constant)


def ftan(arg):
    return tan(arg * convert_constant)


def arcsin(arg):
    return inverse_convert_constant * (asin(arg))


def arccos(arg):
    return inverse_convert_constant * (acos(arg))


def arctan(arg):
    return inverse_convert_constant * (atan(arg))


btn_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': '#566666',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': "flat",
    'activebackground': "#666666"
}

# some function:


def clear():
    ex=txt_display.get()
    ex=ex[0:len(ex)-1]
    txt_display.delete(0,END)
    txt_display.insert(0,ex)


def all_clear():
    b.expression=""
    b.text_input.set('')
    txt_display.delete(0, END)


def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text = b["text"]
    print(text)

    if text == 'x':
        txt_display.insert(END, "*")
        return

    if text== '=':
        try:
            ex=txt_display.get()
            anser=eval(ex)
            txt_display.delete(0,END)
            txt_display.insert(0,anser)
        except Exception as e:
            print("error...",e)
            showerror("Error",e)

        return

    txt_display.insert(END, text)




class Calculator:
    def __init__(self,master):
        self.expression = ""
        self.recall= ""
        self.sum_up= ""
        self.text_input = StringVar()
        self.master = master

        self.middleFrame = Frame(window, relief='flat', bg='#666666')

        # Scientific Calculator Button
        self.btn_left_brack = Button(self.middleFrame, **btn_params, text='(', command=lambda: self.btn_click('('))
        self.btn_left_brack.grid(row=0, column=0)

        self.btn_right_brack = Button(self.middleFrame, **btn_params, text=')', command=lambda: self.btn_click(')'))
        self.btn_right_brack.grid(row=0, column=1)

        self.btn_exp = Button(self.middleFrame, **btn_params, text='exp', command=lambda: self.btn_click('exp('))
        self.btn_exp.grid(row=0, column=2)

        self.btn_pi = Button(self.middleFrame, **btn_params, text='π', command=lambda: self.btn_click('pi'))
        self.btn_pi.grid(row=0, column=3)

        self.btn_Deg = Button(self.middleFrame, **btn_params, activeforeground='orange', text='Deg',
                              command=self.convert_deg)
        self.btn_Deg.grid(row=1, column=0)

        self.btn_Rad = Button(self.middleFrame, **btn_params, foreground='orange', activeforeground='orange', text='Rad',
                              command=self.convert_rad)
        self.btn_Rad.grid(row=1, column=1)

        self.btn_cube = Button(self.middleFrame, **btn_params, text=u'x\u00B3')
        self.btn_cube.grid(row=1, column=2)

        self.btn_abs = Button(self.middleFrame, **btn_params, text='abs')
        self.btn_abs.grid(row=1, column=3)

        self.btn_sin = Button(self.middleFrame, **btn_params, text='sin', command=lambda: self.btn_click('fsin('))
        self.btn_sin.grid(row=2, column=0)

        self.btn_cos = Button(self.middleFrame, **btn_params, text='cos', command=lambda: self.btn_click('fcos('))
        self.btn_cos.grid(row=2, column=1)

        self.btn_tan = Button(self.middleFrame, **btn_params, text='tan', command=lambda: self.btn_click('ftan('))
        self.btn_tan.grid(row=2, column=2)

        self.btn_log = Button(self.middleFrame, **btn_params, text='log', command=lambda: self.btn_click('log('))
        self.btn_log.grid(row=2, column=3)

        self.btn_sin_inverse = Button(self.middleFrame, **btn_params, text=u'sin\u207B\u00B9')
        self.btn_sin_inverse.grid(row=3, column=0)

        self.btn_cos_inverse = Button(self.middleFrame, **btn_params, text=u'cos\u207B\u00B9')
        self.btn_cos_inverse.grid(row=3, column=1)

        self.btn_tan_inverse = Button(self.middleFrame, **btn_params, text=u'tan\u207B\u00B9')
        self.btn_tan_inverse.grid(row=3, column=2)

        self.btn_ln = Button(self.middleFrame, **btn_params, text='ln')
        self.btn_ln.grid(row=3, column=3)

        self.btn_factorial = Button(self.middleFrame, **btn_params, text='n!')
        self.btn_factorial.grid(row=0, column=4)

        self.btn_square = Button(self.middleFrame, **btn_params, text=u"x\u00B2")
        self.btn_square.grid(row=1, column=4)

        self.btn_power = Button(self.middleFrame, **btn_params, text="x^y")
        self.btn_power.grid(row=2, column=4)

        self.btn_ans = Button(self.middleFrame, **btn_params, text="ans")
        self.btn_ans.grid(row=3, column=4)

    def convert_deg(self):
        global convert_constant
        global inverse_convert_constant
        covert_constant = pi / 180
        inverse_convert_constant = 180 / pi
        self.btn_Rad['foreground'] = 'white'
        self.btn_Deg['foreground'] = 'orange'

    def convert_rad(self):
        global convert_constant
        global inverse_convert_constant
        covert_constant = 1
        inverse_convert_constant = 1
        self.btn_Rad['foreground'] = 'orange'
        self.btn_Deg['foreground'] = 'white'

    def btn_click(self, expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)

        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)




# creating a calculator window
window = Tk()
window.iconbitmap(r'cal.ico')
window.title(' Scientific Calculator')
window.geometry("360x500")
b=Calculator(window)

#Entry Frame:
top_frame = Frame(window, width=650, height=20, bd=4, relief='flat', bg='#666666')
top_frame.pack(side=TOP)

#Normal Calcultor Frame
buttonFrame = Frame(window, relief='flat', bg='#666666')
buttonFrame.pack(side=RIGHT)

#Scientific Frame


#Entry Display
txt_display = Entry(top_frame, font=('arial, 26'), relief='flat',textvariable= b.text_input,
                    bg='#455555', fg='pink', width=60, bd=10, justify='center')
txt_display.pack(side=TOP, pady=10, padx=10, fill=X)



# adding normal calculator button

temp = 1
for i in range(1, 4):
    for j in range(0, 3):
        btn = Button(buttonFrame, text=str(temp), **btn_params)
        btn.grid(row=i, column=j)
        btn.configure(activeforeground='#6d4d4d', bg='#4d4d4d')
        temp = temp + 1
        btn.bind("<Button-1>", click_btn_function)

btn_clear = Button(buttonFrame, **btn_params, text='C',command=all_clear)
btn_clear.grid(row=0, column=0)

btn_del = Button(buttonFrame, **btn_params, text='del',command=clear)
btn_del.grid(row=0, column=1)

btn_change_sign = Button(buttonFrame, **btn_params, text='+/-')
btn_change_sign.grid(row=0, column=2)

btn_div = Button(buttonFrame, **btn_params, text='/')
btn_div.grid(row=0, column=3)

btn_sqrt = Button(buttonFrame, **btn_params, text='sqrt',command=lambda:click_btn_function)
btn_sqrt.grid(row=0, column=4)

btn_0 = Button(buttonFrame, **btn_params, text='0', command=lambda: click_btn_function)
btn_0.configure(activeforeground='#6d4d4d', bg='#4d4d4d', width=7)
btn_0.grid(row=4, column=0, columnspan=2)

btn_equal = Button(buttonFrame, **btn_params, text='=')
btn_equal.configure(activeforeground='#ff9980', bg='#ff9980')
btn_equal.grid(row=4, column=2)

btn_decimal = Button(buttonFrame, **btn_params, text=".")
btn_decimal.grid(row=4, column=3)

btn_comma = Button(buttonFrame, **btn_params, text=",")
btn_comma.grid(row=4, column=4)

btn_mult = Button(buttonFrame, **btn_params, text='x')
btn_mult.grid(row=1, column=3)

btn_memory_clear = Button(buttonFrame, **btn_params, text='MC')
btn_memory_clear.grid(row=1, column=4)

btn_sub = Button(buttonFrame, **btn_params, text='-')
btn_sub.grid(row=2, column=3)

btn_memory_recall = Button(buttonFrame, **btn_params, text='MR')
btn_memory_recall.grid(row=2, column=4)

btn_add = Button(buttonFrame, **btn_params, text='+')
btn_add.grid(row=3, column=3)

btn_memory_add = Button(buttonFrame, **btn_params, text='M+', command=lambda: self.memory_add)
btn_memory_add.grid(row=3, column=4)

#binding all btns
btn_0.bind("<Button-1>", click_btn_function)
btn_div.bind("<Button-1>", click_btn_function)
btn_equal.bind("<Button-1>", click_btn_function)
btn_decimal.bind("<Button-1>", click_btn_function)
btn_comma.bind("<Button-1>", click_btn_function)
btn_mult.bind("<Button-1>", click_btn_function)
btn_add.bind("<Button-1>", click_btn_function)
btn_sub.bind("<Button-1>", click_btn_function)

###################################################

#MODE ACTIVATE
normalcalc= True
def sc_click():
    global normalcalc
    if normalcalc:
        buttonFrame.pack_forget()
        b.middleFrame.pack(side=TOP)
        buttonFrame.pack(side=TOP)
        window.geometry("360x790")
        print("show sc")

        normalcalc=False
    else:
        print('show normal')
        b.middleFrame.pack_forget()
        window.geometry("360x480")
        normalcalc=True


#creating menubar
menubar = Menu(window)
mode = Menu(menubar, font=("arial",12), tearoff=0)
mode.add_checkbutton(label="Scientific Calculator", command=sc_click)
menubar.add_cascade(label="Mode", menu=mode)
window.config(menu=menubar)

#finish the code
window.mainloop()
