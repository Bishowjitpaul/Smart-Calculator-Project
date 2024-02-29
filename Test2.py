import tkinter as tk
from math import *
from tkinter.messagebox import *


convert_constant= 1
inverse_convert_constant= 1

btn_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg':'#566666',
    'font': ('arial',18),
    'width': 2,
    'height': 2,
    'relief': "flat",
    'activebackground': "#666666"
}

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


class Calculator:
    def __init__(self,master):
        self.expression = ""
        self.recall= ""
        self.sum_up= ""
        self.text_input = tk.StringVar()
        self.master = master



        top_frame=tk.Frame(master,width=650, height=20, bd=4, relief= 'flat',bg='#666666')
        top_frame.pack(side=tk.TOP)

        bottom_frame = tk.Frame(master, width=650, height=470, bd=4, relief='flat', bg='#666666')
        bottom_frame.pack(side=tk.BOTTOM)

        my_item = tk.Label(top_frame, text='Scientific Calculator',
                           font=('arial', 14, 'bold'), fg='black', width=26, bg='#816666')
        my_item.pack()

#justify means entry er middle , ba right ba left j dike thke likha suru hobe

        txt_display = tk.Entry(top_frame, font=('arial, 26'), relief='flat',
                               bg='#455555', fg='pink', textvariable= self.text_input, width = 60, bd=10, justify= 'center')
        txt_display.pack()

#button_system
#row 0
        self.btn_left_brack= tk.Button(bottom_frame,**btn_params, text='(',command=lambda:self.btn_click('('))
        self.btn_left_brack.grid(row=0,column=0)

        self.btn_right_brack = tk.Button(bottom_frame, **btn_params, text=')', command=lambda: self.btn_click(')'))
        self.btn_right_brack.grid(row=0, column=1)

        self.btn_exp = tk.Button(bottom_frame, **btn_params, text='exp', command=lambda: self.btn_click('exp('))
        self.btn_exp.grid(row=0, column=2)

        self.btn_pi = tk.Button(bottom_frame, **btn_params, text='π', command=lambda: self.btn_click('pi'))
        self.btn_pi.grid(row=0, column=3)

        self.btn_clear = tk.Button(bottom_frame, **btn_params, text='C', command=self.btn_clear_all)
        self.btn_clear.grid(row=0, column=4)

        self.btn_del = tk.Button(bottom_frame, **btn_params, text='del', command=self.btn_clear1)
        self.btn_del.grid(row=0, column=5)

        self.btn_change_sign= tk.Button(bottom_frame, **btn_params, text='+/-', command=lambda: self.change_signs)
        self.btn_change_sign.grid(row=0, column=6)

        self.btn_div = tk.Button(bottom_frame, **btn_params, text='/', command=lambda: self.btn_click('/'))
        self.btn_div.grid(row=0, column=7)

        self.btn_sqrt = tk.Button(bottom_frame, **btn_params, text='sqrt', command=lambda: self.btn_click('sqrt('))
        self.btn_sqrt.grid(row=0, column=8)

#row1
        self.btn_Deg = tk.Button(bottom_frame, **btn_params, activeforeground='orange', text='Deg',
                               command=self.convert_deg)
        self.btn_Deg.grid(row=1, column=0)

        self.btn_Rad = tk.Button(bottom_frame, **btn_params, foreground='orange', activeforeground='orange', text='Rad',
                               command=self.convert_rad)
        self.btn_Rad.grid(row=1, column=1)

        self.btn_cube = tk.Button(bottom_frame, **btn_params, text=u'x\u00B3', command=lambda:self.btn_click('**3'))
        self.btn_cube.grid(row=1, column=2)

        self.btn_abs = tk.Button(bottom_frame, **btn_params, text='abs', command=lambda: self.btn_click('abs'+'('))
        self.btn_abs.grid(row=1, column=3)

        self.btn_7 = tk.Button(bottom_frame, **btn_params, text='7', command=lambda: self.btn_click('7'))
        self.btn_7.configure(activeforeground='#6d4d4d',bg= '#4d4d4d')
        self.btn_7.grid(row=1, column=4)

        self.btn_8 = tk.Button(bottom_frame, **btn_params, text='8', command=lambda: self.btn_click('8'))
        self.btn_8.configure(activeforeground='#6d4d4d', bg='#4d4d4d')
        self.btn_8.grid(row=1, column=5)

        self.btn_9 = tk.Button(bottom_frame, **btn_params, text='9', command=lambda: self.btn_click('9'))
        self.btn_9.configure(activeforeground='#6d4d4d', bg='#4d4d4d')
        self.btn_9.grid(row=1, column=6)

        self.btn_mult = tk.Button(bottom_frame, **btn_params, text='x', command=lambda: self.btn_click('*'))
        self.btn_mult.grid(row=1, column=7)

        self.btn_memory_clear = tk.Button(bottom_frame, **btn_params, text='MC', command=lambda: self.memory_clear)
        self.btn_memory_clear.grid(row=1, column=8)

#row3
        self.btn_sin = tk.Button(bottom_frame, **btn_params, text='sin', command= lambda:self.btn_click('fsin('))
        self.btn_sin.grid(row=2, column=0)

        self.btn_cos = tk.Button(bottom_frame, **btn_params, text='cos', command=lambda: self.btn_click('fcos('))
        self.btn_cos.grid(row=2, column=1)

        self.btn_tan = tk.Button(bottom_frame, **btn_params, text='tan', command=lambda: self.btn_click('ftan('))
        self.btn_tan.grid(row=2, column=2)

        self.btn_log = tk.Button(bottom_frame, **btn_params, text='log', command=lambda: self.btn_click('log('))
        self.btn_log.grid(row=2, column=3)

        self.btn_4 = tk.Button(bottom_frame, **btn_params, text='4', command=lambda: self.btn_click('4'))
        self.btn_4.configure(activeforeground='#6d4d4d', bg='#4d4d4d')
        self.btn_4.grid(row=2, column=4)

        self.btn_5 = tk.Button(bottom_frame, **btn_params, text='5', command=lambda: self.btn_click('5'))
        self.btn_5.configure(activeforeground='#6d4d4d', bg='#4d4d4d')
        self.btn_5.grid(row=2, column=5)

        self.btn_6 = tk.Button(bottom_frame, **btn_params, text='6', command=lambda: self.btn_click('6'))
        self.btn_6.configure(activeforeground='#6d4d4d', bg='#4d4d4d')
        self.btn_6.grid(row=2, column=6)

        self.btn_sub= tk.Button(bottom_frame, **btn_params, text='-', command=lambda: self.btn_click('-'))
        self.btn_sub.grid(row=2, column=7)

        self.btn_memory_recall= tk.Button(bottom_frame, **btn_params, text='MR', command=lambda: self.memory_recall())
        self.btn_memory_recall.grid(row=2, column=8)

#row3
        self.btn_sin_inverse = tk.Button(bottom_frame, **btn_params, text=u'sin\u207B\u00B9', command=lambda: self.btn_click('arcsin('))
        self.btn_sin_inverse.grid(row=3, column=0)

        self.btn_cos_inverse = tk.Button(bottom_frame, **btn_params, text=u'cos\u207B\u00B9', command=lambda: self.btn_click('arccos('))
        self.btn_cos_inverse.grid(row=3, column=1)

        self.btn_tan_inverse = tk.Button(bottom_frame, **btn_params, text=u'tan\u207B\u00B9', command=lambda: self.btn_click('arctan('))
        self.btn_tan_inverse.grid(row=3, column=2)

        self.btn_ln = tk.Button(bottom_frame, **btn_params, text='ln', command=lambda: self.btn_click('loge('))
        self.btn_ln.grid(row=3, column=3)

        self.btn_1 = tk.Button(bottom_frame, **btn_params, text='1', command=lambda: self.btn_click('1'))
        self.btn_1.configure(activeforeground='#6d4d4d', bg='#4d4d4d')
        self.btn_1.grid(row=3, column=4)

        self.btn_2 = tk.Button(bottom_frame, **btn_params, text='2', command=lambda: self.btn_click('2'))
        self.btn_2.configure(activeforeground='#6d4d4d', bg='#4d4d4d')
        self.btn_2.grid(row=3, column=5)

        self.btn_3 = tk.Button(bottom_frame, **btn_params, text='3', command=lambda: self.btn_click('3'))
        self.btn_3.configure(activeforeground='#6d4d4d', bg='#4d4d4d')
        self.btn_3.grid(row=3, column=6)

        self.btn_add = tk.Button(bottom_frame, **btn_params, text='+', command=lambda: self.btn_click('+'))
        self.btn_add.grid(row=3, column=7)

        self.btn_memory_add = tk.Button(bottom_frame, **btn_params, text='M+', command=lambda: self.memory_add)
        self.btn_memory_add.grid(row=3, column=8)

#row4
        self.btn_factorial = tk.Button(bottom_frame, **btn_params, text='n!', command=lambda: self.btn_click('factorial('))
        self.btn_factorial.grid(row=4, column=0)

        self.btn_square = tk.Button(bottom_frame, **btn_params, text=u"x\u00B2", command=lambda: self.btn_click('**2'))
        self.btn_square.grid(row=4, column=1)

        self.btn_power = tk.Button(bottom_frame, **btn_params, text="x^y", command=lambda: self.btn_click('**'))
        self.btn_power.grid(row=4, column=2)

        self.btn_ans = tk.Button(bottom_frame, **btn_params, text="ans", command=self.answer)
        self.btn_ans.grid(row=4, column=3)

        self.btn_0 = tk.Button(bottom_frame, **btn_params, text='0', command=lambda: self.btn_click('0'))
        self.btn_0.configure(activeforeground='#6d4d4d', bg='#4d4d4d', width=7,)
        self.btn_0.grid(row=4, column=4, columnspan=2)

        self.btn_equal = tk.Button(bottom_frame, **btn_params, text='=', command= self.btn_equal)
        self.btn_equal.configure(activeforeground='#ff9980', bg='#ff9980')
        self.btn_equal.grid(row=4, column=6)

        self.btn_decimal = tk.Button(bottom_frame, **btn_params, text=".", command=lambda: self.btn_click('.'))
        self.btn_decimal.grid(row=4, column=7)

        self.btn_comma = tk.Button(bottom_frame, **btn_params, text=",", command=lambda: self.btn_click(','))
        self.btn_comma.grid(row=4, column=8)

    #Functions
    def btn_click(self,expression_val):
        if len(self.expression) >= 23:
            self.expression = self.expression
            self.text_input.set(self.expression)

        else:
            self.expression = self.expression + str(expression_val)
            self.text_input.set(self.expression)

    def btn_clear1(self):
        self.expression = self.expression[:-1]
        self.text_input.set(self.expression)

    def change_signs(self):
        self.expression=self.expression + '-'
        self.text_input.set(self.expression)

    def memory_clear(self):
        self.recall = ""

    def memory_add(self):
        self.recall = self.recall + '+' + self.expression

    def answer(self):
        self.answer = self.sum_up
        self.expression = self.expression + self.answer
        self.text_input.set(self.expression)

    def memory_recall(self):
        if self.expression == "":
            self.text_input.set('0' + self.expression + self.recall)
        else:
            self.text_input.set(self.expression + self.recall)

    def convert_deg(self):
        global convert_constant
        global inverse_convert_constant
        covert_constant = pi / 180
        inverse_convert_constant = 180/pi
        self.btn_Rad['foreground'] = 'white'
        self.btn_Deg['foreground'] = 'orange'

    def convert_rad(self):
        global convert_constant
        global inverse_convert_constant
        covert_constant = 1
        inverse_convert_constant = 1
        self.btn_Rad['foreground'] = 'orange'
        self.btn_Deg['foreground'] = 'white'

    def btn_clear_all(self):
        self.expression = ''
        self.text_input.set('')

    def btn_equal(self):
        try:
            self.sum_up = str(eval(self.expression))
            self.text_input.set(self.sum_up)
            self.expression = self.sum_up
        except Exception as e:
            showerror("Error", e)


#creating a window
root = tk.Tk()
root.iconbitmap(r'cal.ico')
b = Calculator(root)
root.title(' Scientific Calculator')
root.geometry("650x490+50+50")
root.resizable(False, False)
root.mainloop()
