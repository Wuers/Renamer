import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('functionalities_test')
window.geometry('600x400')

#button
def button_func():
    print ('a basic button')
    print (radio_var.get())

button_string = tk.StringVar(value = 'A button with string var')
button = ttk.Button(window, text ='A simple button', command = button_func,
                    textvariable = button_string)
button.pack()

#check buttons
check_var = tk.IntVar(value = 5)
check1 = ttk.Checkbutton(window, text = 'checkbox 1',
                        command = lambda:print(check_var.get()),
                        variable = check_var,
                        onvalue = 10,
                        offvalue = 5)
check1.pack()

check_var2 = tk.IntVar(value = 6)
check2 = ttk.Checkbutton(window, text = 'checkbox 2',
                         command = lambda: print ('test')
                         #variable = check_var2,
                         )
check2.pack()
#radio buttons
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(window, text = 'Radiobutton 1',
                        value = 'radio 1', 
                        variable = radio_var,
                        command = lambda:print(radio_var.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, text = 'Radiobutton 2',
                        value = 2,
                        variable= radio_var,
                        command = lambda: print(radio_var.get()\))
radio2.pack()

#example:
#create another checkbutton and 2 radiobuttons
#radio button:
    #values for buttons are A and B
    #ticking either print the values of the ckeckbutton
    #ticking the radio button unchecks the checkbutton
#check button:
    #ticking the checkbutton print the value of the radio button value
    #use tkinter var for Booleans!

    
#run
window.mainloop()