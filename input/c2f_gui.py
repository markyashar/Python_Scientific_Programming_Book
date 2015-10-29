#!/usr/bin/env python
from Tkinter import *  # This statement imports functionality from GUI toolkit Tkinter to construct widgets.
root = Tk()            # Need to 1st make a root widget that holds complete window w/all the other widgets.
                       # This root widget is of type Tk. 
C_entry = Entry(root, width=4)   # The 1st entry widget is then made and referred to by a variable C_entry.
                                 # This widget is an object of type Entry, provided by Tkinter module. When
                                 # creating a widget, must bind it to a parent widget, which is graphical
                                 # element in which this new widget is to be packed. Widgets in present program
                                 # have 'root' widget as parent widget. Here, 'Entry' widget has possibility for
                                 # setting width of text field, here 'width=4' means that text field is 4 characters
                                 # wide. 
C_entry.pack(side='left')        # Pack statement is important to remember -- w/out it, widget remains ivisible.
Cunit_label = Label(root, text='Celsius')
Cunit_label.pack(side='left')

def compute():
    C = float(C_entry.get())     # Inside 'compute' function we first fetch Celsius value from 'C_entry' widget, using
                                 # widget's 'get' function, then we transform this string (everything typed in by user
                                 # is interpreted as text & stored in strings) to a 'float' before we compute corresponding
                                 # Fahrenheit value.
    F = (9./5)*C + 32
    F_label.configure(text='%g' % F)    # Finally, can update ("configure") text in the 'Label' widget 'F_label' w/a new text,
                                        # namely computed degrees in Fahrenheit.

compute = Button(root, text=' is ', command=compute)   # In this part of program, computations are tied to event of
                                                       # clicking the button "is". Button widget naturally has a text,
                                                       # but more important, it binds button to function 'compute' through
                                                       # the 'command=compute' option. This means that when user clicks button
                                                       # "is", function 'compute' is called.  
compute.pack(side='left', padx=4)
F_label = Label(root, width=5)          # Finally, can update ("configure") text in the 'Label' widget 'F_label' w/a new text,                                                                                           # namely computed degrees in Fahrenheit.

F_label.pack(side='left')
Funit_label = Label(root, text='Fahrenheit')
Funit_label.pack(side='left')

root.mainloop()      # Program enters event loop here. This is an infinite loop that "listens" to use events, such as moving
                     # mouse, clicking mouse, typing characters on keyboard, etc. When an event is recorded, program starts 
                     # performing associated actions. In the present case, program waits for only one case: clicking the
                     # button "is". As soon as we click on button, 'compute' function is called and program stats doing
                     # mathematical work. GUI will appear on screen until we destroy window by clicking on X up in corner of
                     # window decoration   
