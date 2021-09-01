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
def open_mass_conversion():
    win.withdraw()
    os.system('unit_conversion2.py')

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
            if a == 'km':
                if b == 'mile':
                    result = (c/1.6093)
                elif b == 'inch':
                    result = (c*39370)
                elif b == 'foot':
                    result = (c*3281)
                elif b == 'metre':
                    result = (c*1000)
                elif b == 'yard':
                    result = (c*1094)
                elif b == 'cm':
                    result = (c*100000)
            elif a == 'mile':
                if b == 'km':
                    result = (c*1.6093)
                elif b == 'inch':
                    result = (c*63360)
                elif b == 'foot':
                    result = (c*5280)
                elif b == 'metre':
                    result = (c*1609)
                elif b == 'yard':
                    result = (c*1760)
                elif b == 'cm':
                    result = (c*160934)
            elif a == 'inch':
                if b == 'mile':
                    result = (c/63360)
                elif b == 'km':
                    result = (c/39370)
                elif b == 'foot':
                    result = (c/12)
                elif b == 'metre':
                    result = (c/39.37)
                elif b == 'yard':
                    result = (c/36)
                elif b == 'cm':
                    result = (c*2.54)
            elif a == 'foot':
                if b == 'mile':
                    result = (c/5280)
                elif b == 'km':
                    result = (c/3281)
                elif b == 'inch':
                    result = (c*12)
                elif b == 'metre':
                    result = (c/3.281)
                elif b == 'yard':
                    result = (c/3)
                elif b == 'cm':
                    result = (c/30.48)
            elif a == 'cm':
                if b == 'mile':
                    result = (c/160934)
                elif b == 'km':
                    result = (c/100000)
                elif b == 'inch':
                    result = (c/2.54)
                elif b == 'metre':
                    result = (c/100)
                elif b == 'yard':
                    result = (c/91.44)
                elif b == 'foot':
                    result = (c/30.48)
            elif a == 'metre':
                if b == 'mile':
                    result = (c/1609)
                elif b == 'km':
                    result = (c/1000)
                elif b == 'inch':
                    result = (c*39.37)
                elif b == 'cm':
                    result = (c*100)
                elif b == 'yard':
                    result = (c*1.094)
                elif b == 'foot':
                    result = (c*3.281)
            elif a == 'yard':
                if b == 'mile':
                    result = (c/1760)
                elif b == 'km':
                    result = (c/1094)
                elif b == 'inch':
                    result = (c*36)
                elif b == 'metre':
                    result = (c/1.094)
                elif b == 'cm':
                    result = (c*91.44)
                elif b == 'foot':
                    result = (c*3)
            if 0 < result < 1:
                output_label.config(text = f"{c} {a} = {result:e} {b}", bg = bg_color)
            elif 0 < math.modf(result)[0] < 1:
                output_label.config(text = f"{c} {a} = {result:.4f} {b}", bg = bg_color)
            else:
                output_label.config(text = f"{c} {a} = {result} {b}", bg = bg_color)
        else:
            output_label.config(text = "Both units are same", bg = bg_color)
    

desc_label = Label(win, text = "Here You can convert any length unit and find its conversion",
                   font = ('verdana',18,'italic'), wraplength = 550,
                   bg = bg_color, fg = 'slategray4')
desc_label.pack(pady = 20)

unit_frame = Frame(win, bg = bg_color)
unit_frame.pack()

unit1_label = Label(unit_frame, text = "Select unit 1 :", font = ('Courier',20),
                    bg = bg_color, fg = 'red3')
unit1_label.grid(row = 0, column = 0, padx = 10, pady = 10)

unit1_option = Combobox(unit_frame, state = 'readonly', textvariable = unit1,
                        values = ['mile','inch','foot','kilometre','centimetre','metre','yard'],
                        font = entry_font, width = 11)
unit1_option.grid(row = 0, column = 1, padx = 20, pady = 10)

unit2_label = Label(unit_frame, text = "Select unit 2 :", font = ('Courier',20),
                    bg = bg_color, fg = 'red3')
unit2_label.grid(row = 1, column = 0, pady = 10)

unit2_option = Combobox(unit_frame, state = 'readonly', textvariable = unit2,
                        values = ['kilometre','inch','foot','centimetre','metre','mile','yard'],
                        font = entry_font, width = 11)
unit2_option.grid(row = 1, column = 1, pady = 10)

entry_frame = Frame(win, bg = bg_color)
entry_frame.pack()

entry_label = Label(entry_frame, text = "Enter a value :", font = ('Consolas',20),
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

sub_menu.add_cascade(label = 'Length Unit Conversion', state = DISABLED)
sub_menu.add_cascade(label = 'Mass Unit Conversion', command = open_mass_conversion)
sub_menu.add_cascade(label = 'Time Unit Conversion', command = open_time_conversion)
sub_menu.add_separator()
sub_menu.add_cascade(label = 'Quit', command = win.destroy)

win.mainloop()
