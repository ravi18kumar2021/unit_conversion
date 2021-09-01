from tkinter import *
from tkinter.ttk import Combobox
import math
import os

win = Tk()
win.title('Unit Converter')
win.geometry('600x600+200+100')
win.config(bg = 'bisque')

# variables
unit1 = StringVar()
unit2 = StringVar()
label_font = ('helvetica',20,'italic')
entry_font = ('times new roman',18,'bold')
bg_color = 'bisque'

# function
def open_length_conversion():
    win.withdraw()
    os.system('unit_conversion1.py')

def open_mass_conversion():
    win.withdraw()
    os.system('unit_conversion2.py')
    
def show():
    global result
    a = unit1.get()
    b = unit2.get()
    c = entry_box.get()
    if a == '' or b == '' or c == '':
        output_label.config(text = "You can't leave field blank", bg = bg_color)
    else:
        c = float(c)
        if a!=b:
            if a == 'nanosecond':
                if b == 'microsecond':
                    result = (c/1000)
                elif b == 'millisecond':
                    result = (c/1000000)
                elif b == 'second':
                    result = (c/1000000000)
                elif b == 'minute':
                    result = (c/60000000000)
                elif b == 'hour':
                    result = (c/3600000000000)
                elif b == 'day':
                    result = (c/86400000000000)
                elif b == 'week':
                    result = (c/604800000000000)
                elif b == 'month':
                    result = (c/2628000000000000)
                elif b == 'year':
                    result = (c/31540000000000000)
                elif b == 'decade':
                    result = (c/315400000000000000)
                elif b == 'century':
                    result = (c/3154000000000000000)
            elif a == 'microsecond':
                if b == 'nanosecond':
                    result = (c*1000)
                elif b == 'millisecond':
                    result = (c/1000)
                elif b == 'second':
                    result = (c/1000000)
                elif b == 'minute':
                    result = (c/60000000)
                elif b == 'hour':
                    result = (c/3600000000)
                elif b == 'day':
                    result = (c/86400000000)
                elif b == 'week':
                    result = (c/604800000000)
                elif b == 'month':
                    result = (c/2628000000000)
                elif b == 'year':
                    result = (c/31540000000000)
                elif b == 'decade':
                    result = (c/315400000000000)
                elif b == 'century':
                    result = (c/3154000000000000)
            elif a == 'millisecond':
                if b == 'microsecond':
                    result = (c*1000)
                elif b == 'nanosecond':
                    result = (c*1000000)
                elif b == 'second':
                    result = (c/1000)
                elif b == 'minute':
                    result = (c/60000)
                elif b == 'hour':
                    result = (c/3600000)
                elif b == 'day':
                    result = (c/86400000)
                elif b == 'week':
                    result = (c/604800000)
                elif b == 'month':
                    result = (c/2628000000)
                elif b == 'year':
                    result = (c/31540000000)
                elif b == 'decade':
                    result = (c/315400000000)
                elif b == 'century':
                    result = (c/3154000000000)
            elif a == 'second':
                if b == 'microsecond':
                    result = (c*1000000)
                elif b == 'millisecond':
                    result = (c*1000)
                elif b == 'nanosecond':
                    result = (c*1000000000)
                elif b == 'minute':
                    result = (c/60)
                elif b == 'hour':
                    result = (c/3600)
                elif b == 'day':
                    result = (c/86400)
                elif b == 'week':
                    result = (c/604800)
                elif b == 'month':
                    result = (c/2628000)
                elif b == 'year':
                    result = (c/31540000)
                elif b == 'decade':
                    result = (c/315400000)
                elif b == 'century':
                    result = (c/3154000000)
            elif a == 'minute':
                if b == 'microsecond':
                    result = (c*60000000)
                elif b == 'millisecond':
                    result = (c*60000)
                elif b == 'second':
                    result = (c*60)
                elif b == 'nanosecond':
                    result = (c*60000000000)
                elif b == 'hour':
                    result = (c/60)
                elif b == 'day':
                    result = (c/1440)
                elif b == 'week':
                    result = (c/10080)
                elif b == 'month':
                    result = (c/43800)
                elif b == 'year':
                    result = (c/525600)
                elif b == 'decade':
                    result = (c/5256000)
                elif b == 'century':
                    result = (c/52560000)
            elif a == 'hour':
                if b == 'microsecond':
                    result = (c*3600000000)
                elif b == 'millisecond':
                    result = (c*3600000)
                elif b == 'second':
                    result = (c/3600)
                elif b == 'minute':
                    result = (c*60)
                elif b == 'nanosecond':
                    result = (c*3600000000000)
                elif b == 'day':
                    result = (c/24)
                elif b == 'week':
                    result = (c/168)
                elif b == 'month':
                    result = (c/730)
                elif b == 'year':
                    result = (c/8760)
                elif b == 'decade':
                    result = (c/87600)
                elif b == 'century':
                    result = (c/876000)
            elif a == 'day':
                if b == 'microsecond':
                    result = (c*86400000000)
                elif b == 'millisecond':
                    result = (c*86400000)
                elif b == 'second':
                    result = (c*86400)
                elif b == 'minute':
                    result = (c*1440)
                elif b == 'hour':
                    result = (c*24)
                elif b == 'nanosecond':
                    result = (c*86400000000000)
                elif b == 'week':
                    result = (c/7)
                elif b == 'month':
                    result = (c/30.417)
                elif b == 'year':
                    result = (c/365)
                elif b == 'decade':
                    result = (c/3650)
                elif b == 'century':
                    result = (c/36500)
            elif a == 'week':
                if b == 'microsecond':
                    result = (c*604800000000)
                elif b == 'millisecond':
                    result = (c*604800000)
                elif b == 'second':
                    result = (c*604800)
                elif b == 'minute':
                    result = (c*10080)
                elif b == 'hour':
                    result = (c*168)
                elif b == 'nanosecond':
                    result = (c*604800000000000)
                elif b == 'day':
                    result = (c*7)
                elif b == 'month':
                    result = (c/7)
                elif b == 'year':
                    result = (c/52.143)
                elif b == 'decade':
                    result = (c/521)
                elif b == 'century':
                    result = (c/5214)
            elif a == 'month':
                if b == 'microsecond':
                    result = (c*2.205)
                elif b == 'millisecond':
                    result = (c*2628000000)
                elif b == 'second':
                    result = (c*2628000)
                elif b == 'minute':
                    result = (c*43800)
                elif b == 'hour':
                    result = (c*730)
                elif b == 'nanosecond':
                    result = (c*2628000000000000)
                elif b == 'week':
                    result = (c*7)
                elif b == 'day':
                    result = (c*30.417)
                elif b == 'year':
                    result = (c/12)
                elif b == 'decade':
                    result = (c/120)
                elif b == 'century':
                    result = (c/1200)
            elif a == 'year':
                if b == 'microsecond':
                    result = (c*31540000000000)
                elif b == 'millisecond':
                    result = (c*31540000000)
                elif b == 'second':
                    result = (c*31540000)
                elif b == 'minute':
                    result = (c*525600)
                elif b == 'hour':
                    result = (c*8760)
                elif b == 'nanosecond':
                    result = (c*31540000000000000)
                elif b == 'week':
                    result = (c*52.143)
                elif b == 'month':
                    result = (c*12)
                elif b == 'day':
                    result = (c*365)
                elif b == 'decade':
                    result = (c/10)
                elif b == 'century':
                    result = (c/100)
            elif a == 'decade':
                if b == 'microsecond':
                    result = (c*2.205)
                elif b == 'millisecond':
                    result = (c*315400000000)
                elif b == 'second':
                    result = (c*315400000)
                elif b == 'minute':
                    result = (c*5256000)
                elif b == 'hour':
                    result = (c*87600)
                elif b == 'nanosecond':
                    result = (c*315400000000000000)
                elif b == 'week':
                    result = (c*521)
                elif b == 'month':
                    result = (c*120)
                elif b == 'year':
                    result = (c*10)
                elif b == 'day':
                    result = (c*3650)
                elif b == 'century':
                    result = (c/10)
            elif a == 'century':
                if b == 'microsecond':
                    result = (c*2.205)
                elif b == 'millisecond':
                    result = (c*3154000000000)
                elif b == 'second':
                    result = (c*3154000000)
                elif b == 'minute':
                    result = (c*52560000)
                elif b == 'hour':
                    result = (c*876000)
                elif b == 'nanosecond':
                    result = (c*3154000000000000000)
                elif b == 'week':
                    result = (c*5214)
                elif b == 'month':
                    result = (c*1200)
                elif b == 'year':
                    result = (c*100)
                elif b == 'decade':
                    result = (c*10)
                elif b == 'day':
                    result = (c*36500)
            if 0 < result < 1:
                output_label.config(text = f"{c} {a} = {result:e} {b}", bg = bg_color)
            elif 0 < math.modf(result)[0] < 1:
                output_label.config(text = f"{c} {a} = {result:.4f} {b}", bg = bg_color)
            else:
                output_label.config(text = f"{c} {a} = {result} {b}", bg = bg_color)
        else:
            output_label.config(text = "Both units are same", bg = bg_color)
    

desc_label = Label(win, text = "Here You can convert any Time unit and find its conversion",
                   font = ('verdana',18,'italic'), wraplength = 550,
                   bg = bg_color, fg = 'slategray4')
desc_label.pack(pady = 20)

unit_frame = Frame(win, bg = bg_color)
unit_frame.pack()

unit1_label = Label(unit_frame, text = "Select unit 1 :", font = label_font,
                    bg = bg_color, fg = 'red3')
unit1_label.grid(row = 0, column = 0, padx = 10, pady = 10)

unit1_option = Combobox(unit_frame, state = 'readonly', textvariable = unit1,
                        values = ['nanosecond','microsecond','millisecond','second','minute','hour','day','week','month','year','decade','century'],
                        font = entry_font, width = 11)
unit1_option.grid(row = 0, column = 1, padx = 20, pady = 10)

unit2_label = Label(unit_frame, text = "Select unit 2 :", font = label_font,
                    bg = bg_color, fg = 'red3')
unit2_label.grid(row = 1, column = 0, pady = 10)

unit2_option = Combobox(unit_frame, state = 'readonly', textvariable = unit2,
                        values = ['nanosecond','microsecond','millisecond','second','minute','hour','day','week','month','year','decade','century'],
                        font = entry_font, width = 11)
unit2_option.grid(row = 1, column = 1, pady = 10)

entry_frame = Frame(win, bg = bg_color)
entry_frame.pack()

entry_label = Label(entry_frame, text = "Enter a value :", font = label_font,
                    bg = bg_color)
entry_label.grid(row = 0, column = 0, pady = 20)

entry_box = Entry(entry_frame, font = entry_font, width = 8, justify = 'center')
entry_box.grid(row = 0, column = 1, padx = 20)

btn = Button(win, text = "Convert", command = show, font = ('Arial Rounded MT Bold',20))
btn.pack(pady = 15, ipadx = 20)

output_label = Label(win, font = label_font)
output_label.pack(pady = 10)

# menu bar
menu_option = Menu(win)
win.config(menu = menu_option)

# sub menu
sub_menu = Menu(menu_option, tearoff = 0)
menu_option.add_cascade(label = 'Select Conversion', menu = sub_menu)
sub_menu.add_cascade(label = 'Length Unit Conversion', command = open_length_conversion)
sub_menu.add_cascade(label = 'Mass Unit Conversion', command = open_mass_conversion)
sub_menu.add_cascade(label = 'Time Unit Conversion', state = DISABLED)
sub_menu.add_separator()
sub_menu.add_cascade(label = 'Quit', command = win.destroy)

win.mainloop()
