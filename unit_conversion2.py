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

def open_time_conversion():
    win.withdraw()
    os.system('unit_conversion3.py')

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
            if a == 'kilogram':
                if b == 'pound(lbs)':
                    result = (c*2.205)
                elif b == 'ounce(oz)':
                    result = (c*35.274)
                elif b == 'tonne':
                    result = (c/1000)
                elif b == 'gram':
                    result = (c*1000)
                elif b == 'stone':
                    result = (c/6.35)
                elif b == 'miligram':
                    result = (c*1000000)
            elif a == 'pound(lbs)':
                if b == 'kilogram':
                    result = (c/2.205)
                elif b == 'ounce(oz)':
                    result = (c*16)
                elif b == 'tonne':
                    result = (c/2205)
                elif b == 'gram':
                    result = (c*454)
                elif b == 'stone':
                    result = (c/14)
                elif b == 'miligram':
                    result = (c*453592)
            elif a == 'ounce(oz)':
                if b == 'pound(lbs)':
                    result = (c/16)
                elif b == 'kilogram':
                    result = (c/35.274)
                elif b == 'tonne':
                    result = (c/12)
                elif b == 'gram':
                    result = (c/28.35)
                elif b == 'stone':
                    result = (c/224)
                elif b == 'miligram':
                    result = (c*28350)
            elif a == 'tonne':
                if b == 'pound(lbs)':
                    result = (c*2205)
                elif b == 'kilogram':
                    result = (c*1000)
                elif b == 'ounce(oz)':
                    result = (c*35274)
                elif b == 'gram':
                    result = (c/1000000)
                elif b == 'stone':
                    result = (c*157)
                elif b == 'miligram':
                    result = (c*1000000000)
            elif a == 'miligram':
                if b == 'pound(lbs)':
                    result = (c/453592)
                elif b == 'kilogram':
                    result = (c/1000000)
                elif b == 'ounce(oz)':
                    result = (c/28350)
                elif b == 'gram':
                    result = (c/1000)
                elif b == 'stone':
                    result = (c/6350000)
                elif b == 'tonne':
                    result = (c/1000000000)
            elif a == 'gram':
                if b == 'pound(lbs)':
                    result = (c/454)
                elif b == 'kilogram':
                    result = (c/1000)
                elif b == 'ounce(oz)':
                    result = (c*28.35)
                elif b == 'miligram':
                    result = (c*1000)
                elif b == 'stone':
                    result = (c/6350)
                elif b == 'tonne':
                    result = (c/1000000)
            elif a == 'stone':
                if b == 'pound(lbs)':
                    result = (c*14)
                elif b == 'kilogram':
                    result = (c*6.35)
                elif b == 'ounce(oz)':
                    result = (c*224)
                elif b == 'gram':
                    result = (c*6350)
                elif b == 'miligram':
                    result = (c*6350000)
                elif b == 'tonne':
                    result = (c/157)
            if 0 < result < 1:
                output_label.config(text = f"{c} {a} = {result:e} {b}", bg = bg_color)
            elif 0 < math.modf(result)[0] < 1:
                output_label.config(text = f"{c} {a} = {result:.4f} {b}", bg = bg_color)
            else:
                output_label.config(text = f"{c} {a} = {result} {b}", bg = bg_color)
        else:
            output_label.config(text = "Both units are same", bg = bg_color)
    

desc_label = Label(win, text = "Here You can convert any Mass unit and find its conversion",
                   font = ('verdana',18,'italic'), wraplength = 550,
                   bg = bg_color, fg = 'slategray4')
desc_label.pack(pady = 20)

unit_frame = Frame(win, bg = bg_color)
unit_frame.pack()

unit1_label = Label(unit_frame, text = "Select unit 1 :", font = label_font,
                    bg = bg_color, fg = 'red3')
unit1_label.grid(row = 0, column = 0, padx = 10, pady = 10)

unit1_option = Combobox(unit_frame, state = 'readonly', textvariable = unit1,
                        values = ['kilogram','gram','miligram','pound(lbs)','ounce(oz)','stone','tonne'],
                        font = entry_font, width = 11)
unit1_option.grid(row = 0, column = 1, padx = 20, pady = 10)

unit2_label = Label(unit_frame, text = "Select unit 2 :", font = label_font,
                    bg = bg_color, fg = 'red3')
unit2_label.grid(row = 1, column = 0, pady = 10)

unit2_option = Combobox(unit_frame, state = 'readonly', textvariable = unit2,
                        values = ['kilogram','gram','miligram','pound(lbs)','ounce(oz)','stone','tonne'],
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
menu_option.add_cascade(label = 'Select Type', menu = sub_menu)

sub_menu.add_cascade(label = 'Length Unit Conversion', command = open_length_conversion)
sub_menu.add_cascade(label = 'Mass Unit Conversion', state = DISABLED)
sub_menu.add_cascade(label = 'Time Unit Conversion', command = open_time_conversion)
sub_menu.add_separator()
sub_menu.add_cascade(label = 'Quit', command = win.destroy)

win.mainloop()
