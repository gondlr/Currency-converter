from tkinter import *
from tkinter import ttk
from tkinter import messagebox
try:  # Excepts errors due lack of internet connection
    import converter_scrapper
    from converter_scrapper import name_currency, exchange_rate
except:
    pass

root = Tk()
root.title("Currency converter")
root.resizable(0,0)
frame = Frame()
frame.pack()

#--------------------------Logic------------------------------

def validate_numbers(inStr,acttyp):    #acttyp: Tipo de acción. inStr: Valor input
    if acttyp == '1':
        if not inStr.isdigit():
            return False
    return True          
        
def invert():
    choice1 = list1.get()
    choice2 = list2.get()
    list1.set(choice2)
    list2.set(choice1)

def calculate():
    try:
        currency_to_convert = list1.current()
        currency_converted_to = list2.current()
        value_to_convert = float(left_box.get())
        converted_value = ((exchange_rate[currency_converted_to]*value_to_convert))/exchange_rate[currency_to_convert]
        conversion_value.set(converted_value)
    except:
        messagebox.showinfo("","Must complete all fields")

conversion_value = DoubleVar()


#--------------------------Interface----------------------------
try:   # Excepts errors due lack of internet connection

    left_box = Entry(frame, validate='key')
    left_box['validatecommand'] = (left_box.register(validate_numbers),'%P','%d')
    left_box.grid(row=0,column=0, padx=10, pady=10,columnspan="4")
    left_box.config(justify="right", font=("Arial",20))

    right_box = LabelFrame(frame)
    right_box_content = Label(right_box, textvariable=conversion_value, width=20, justify="right", font=("Arial",20))
    right_box.grid(row=0,column=6, padx=10,pady=10, columnspan=4)
    right_box_content.pack()

    button_invert = Button(frame, text="↔", width=5, 
        height=1, font=("Arial",10), command= lambda: invert())
    button_invert.grid(row=0, column=5)

    list1 = ttk.Combobox(frame, values=(name_currency), state="readonly")
    list1.grid(row=1,column=1)

    list2 = ttk.Combobox(frame, values=name_currency, state="readonly")
    list2.grid(row=1,column=8)

    button_calculate = Button(frame, text="Calculate", width=10, height=1, font=("Arial",10),
        command= lambda: calculate())
    button_calculate.grid(row=1, column=5)



except:
    pass
root.mainloop()
