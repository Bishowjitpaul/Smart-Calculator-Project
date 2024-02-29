import tkinter
from tkinter import *
from math import *
from tkinter.messagebox import *
convert_constant = 1
inverse_convert_constant = 1

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
    txt_display.delete(0,END)

def click_btn_function(event):
    print("btn clicked")
    b = event.widget
    text = b["text"]
    print(text)

    if text == 'x':
        txt_display.insert(END, "*")
        return

    '''if text== '=':
        try:
            ex=txt_display.get()
            anser=eval(ex)
            txt_display.delete(0,END)
            txt_display.insert(0,anser)
        except Exception as e:
            print("error...",e)
            showerror("Error",e)


        return'''

    txt_display.insert(END, text)

# creating a window
window = Tk()
window.iconbitmap(r'cal.ico')

window.title(' Scientific Calculator')
window.geometry("360x470")


top_frame = Frame(window, width=650, height=20, bd=4, relief='flat', bg='#666666')
top_frame.pack(side=TOP)

txt_display = Entry(top_frame, font=('arial, 26'), relief='flat',
                    bg='#455555', fg='pink', width=60, bd=10, justify='center')
txt_display.pack(side=TOP, pady=10, padx=10, fill=X)

buttonFrame1 = Frame(window, relief='flat', bg='#666666')
buttonFrame1.pack(side=RIGHT)



# adding button

btn_clear = Button(buttonFrame1, **btn_params, text='C', command=all_clear)
btn_clear.grid(row=0, column=0)

btn_del = Button(buttonFrame1, **btn_params, text='del', command=clear)
btn_del.grid(row=0, column=1)

btn_change_sign = Button(buttonFrame1, **btn_params, text='+/-')
btn_change_sign.grid(row=0, column=2)

btn_div = Button(buttonFrame1, **btn_params, text='/')
btn_div.grid(row=0, column=3)

btn_sqrt = Button(buttonFrame1, **btn_params, text='sqrt')
btn_sqrt.grid(row=0, column=4)

temp = 1
for i in range(1,4):
    for j in range(2,5):
        btn = Button(buttonFrame1, text=str(temp), **btn_params)
        btn.grid(row=i, column=j)
        btn.configure(activeforeground='#6d4d4d', bg='#4d4d4d')
        temp = temp + 1
        btn.bind("<Button-1>", click_btn_function)

btn_0 = Button(buttonFrame1, **btn_params, text='0', command=lambda: self.btn_click('0'))
btn_0.configure(activeforeground='#6d4d4d', bg='#4d4d4d', width=7)
btn_0.grid(row=4, column=2, columnspan=2)

btn_equal = Button(buttonFrame1, **btn_params, text='=', )
btn_equal.configure(activeforeground='#ff9980', bg='#ff9980')
btn_equal.grid(row=4, column=4)

btn_decimal = Button(buttonFrame1, **btn_params, text=".")
btn_decimal.grid(row=4, column=1)

btn_comma = Button(buttonFrame1, **btn_params, text=",")
btn_comma.grid(row=4, column=0)

btn_mult = Button(buttonFrame1, **btn_params, text='x')
btn_mult.grid(row=1, column=1)

btn_memory_clear = Button(buttonFrame1, **btn_params, text='MC')
btn_memory_clear.grid(row=1, column=0)

btn_sub = Button(buttonFrame1, **btn_params, text='-')
btn_sub.grid(row=2, column=1)

btn_memory_recall = Button(buttonFrame1, **btn_params, text='MR')
btn_memory_recall.grid(row=2, column=0)

btn_add = Button(buttonFrame1, **btn_params, text='+')
btn_add.grid(row=3, column=1)

btn_memory_add = Button(buttonFrame1, **btn_params, text='M+', command=lambda: self.memory_add)
btn_memory_add.grid(row=3, column=0)

#binding all btns


btn_0.bind("<Button-1>", click_btn_function)
btn_div.bind("<Button-1>", click_btn_function)
btn_equal.bind("<Button-1>", click_btn_function)
btn_decimal.bind("<Button-1>", click_btn_function)
btn_comma.bind("<Button-1>", click_btn_function)
btn_mult.bind("<Button-1>", click_btn_function)
btn_add.bind("<Button-1>", click_btn_function)
btn_sub.bind("<Button-1>", click_btn_function)

####################################################

def iExit():
    iExit=tkinter.messagebox.askyesno("Scientific Calculator","confirm if you want to exit")
    if iExit>0:
        window.destroy()
        return

def Scientific():
    window.geometry("650x490+50+50")
    window.resizable(False, False)

def Standard():
    window.geometry("360x470")
    window.resizable(False, False)

menubar= Menu(window)
filemenu=Menu(menubar, tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label="Standard",command=Standard)
filemenu.add_command(label="Scientific",command=Scientific)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=iExit)

window.config(menu=menubar)





window.mainloop()
middleFrame= Frame(window, relief='flat', bg='#666666')

btn_left_brack = Button(middleFrame, **btn_params, text='(', command=lambda:b.btn_click('('))
btn_left_brack.grid(row=0, column=0)

btn_right_brack = Button(middleFrame, **btn_params, text=')', command=lambda: b.btn_click(')'))
btn_right_brack.grid(row=0, column=1)

btn_exp = Button(middleFrame, **btn_params, text='exp', command=lambda: self.btn_click('exp('))
btn_exp.grid(row=0, column=2)

btn_pi = Button(middleFrame, **btn_params, text='π', command=lambda: b.btn_click('pi'))
btn_pi.grid(row=0, column=3)

btn_Deg = Button(middleFrame, **btn_params, activeforeground='orange', text='Deg', command=convert_deg)

btn_Deg.grid(row=1, column=0)

btn_Rad = Button(middleFrame, **btn_params, foreground='orange', activeforeground='orange', text='Rad',command=convert_rad)
btn_Rad.grid(row=1, column=1)

btn_cube = Button(middleFrame, **btn_params, text=u'x\u00B3')
btn_cube.grid(row=1, column=2)

btn_abs = Button(middleFrame, **btn_params, text='abs')
btn_abs.grid(row=1, column=3)

btn_sin = Button(middleFrame, **btn_params, text='sin', command=lambda:b.btn_click('fsin('))
btn_sin.grid(row=2, column=0)

btn_cos = Button(middleFrame, **btn_params, text='cos', command=lambda: b.btn_click('fcos('))
btn_cos.grid(row=2, column=1)

btn_tan = Button(middleFrame, **btn_params, text='tan', command=lambda: self.btn_click('ftan('))
btn_tan.grid(row=2, column=2)

btn_log = Button(middleFrame, **btn_params, text='log', command=lambda: self.btn_click('log('))
btn_log.grid(row=2, column=3)

btn_sin_inverse = Button(middleFrame, **btn_params, text=u'sin\u207B\u00B9')
btn_sin_inverse.grid(row=3, column=0)

btn_cos_inverse = Button(middleFrame, **btn_params, text=u'cos\u207B\u00B9')
btn_cos_inverse.grid(row=3, column=1)

btn_tan_inverse = Button(middleFrame, **btn_params, text=u'tan\u207B\u00B9')
btn_tan_inverse.grid(row=3, column=2)

btn_ln = Button(middleFrame, **btn_params, text='ln')
btn_ln.grid(row=3, column=3)

btn_factorial = Button(middleFrame, **btn_params, text='n!')
btn_factorial.grid(row=0, column=4)

btn_square = Button(middleFrame, **btn_params, text=u"x\u00B2")
btn_square.grid(row=1, column=4)

btn_power = Button(middleFrame, **btn_params, text="x^y")
btn_power.grid(row=2, column=4)

btn_ans = Button(middleFrame, **btn_params, text="ans")
btn_ans.grid(row=3, column=4)