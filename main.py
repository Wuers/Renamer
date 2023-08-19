
#22.07.2023
import customtkinter as ctk
from tkinter import filedialog as fd
from tkinter import ttk
import sys
import pandas as pd
import dataframe_functions

file_names_list = []

#button functions
def add_button_func():
    #1 selecting files
    global file_list
    file_list = fd.askopenfilenames(
        initialdir='E:/0_Wuer/5 Projekty/Python/P2_Renamer/TEST FILES'
        )
    
    global file_names_list
    def finding_names_from_list(file_list):
        new_list = []
        for file in file_list:
            name_start_index = (file.rfind('/'))+1
            name = file[name_start_index:]
            new_list.append(name)
        return new_list
    
    file_names_list=finding_names_from_list(file_list)

    #2 couting files
    selected_files_numb = len(file_list)
    #3 displaying number of files
    counter_label.configure(text = f'({selected_files_numb}) files are selected')

def  refresh():
    print (f'refreshing - file list is: {file_names_list}')
    for i in range(10):
        number=i+1
        file_name = 'nazwa pliku'
        format = '.pdf'
        date = '10.10.2023'
        data = [number, file_name, format, date]
        table1.insert(parent ='', index = 'end', values = data)

#GENERAL
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

#LAYOUT BELLOW
#window
window =ctk.CTk()
window.title('Renamer by Wuers')
window.geometry('600x400')

#label - selection
title_label = ctk.CTkLabel(window,height=20,width=100,
                           padx=10, pady=20,
                           text="Select Files and Rules:")
title_label.pack()

#FRAME 1 - Adding files and live counter
frame_1 = ctk.CTkFrame (window,
                        width=200,
                        height = 50)
frame_1.pack(pady=10)
#button - add_button for files
file_add_button = ctk.CTkButton(master = frame_1,
                                text='Add files',
                                command=add_button_func
                                )
file_add_button.pack()


#testing new button with methods in another file
#file_add_button2 = ctk.CTkButton(master = frame_1,
#                                text='Add files2',
#                                command=dataframe_functions.add_button_func2
#                                )
#file_add_button2.pack()

#Label - button updated label -live Counter
counter_label = ctk.CTkLabel(
    master = frame_1,
    text = 'Files not selected'
)
counter_label.pack()

#refresh table button 
refresh_button = ctk.CTkButton(master=frame_1, 
                               text ='refresh_button',
                               command = refresh)
refresh_button.pack()
#preview of selected files table
table1 = ttk.Treeview(window, columns =('number', 'file_name','format', 'date' ),show = 'headings')
table1.heading('number', text = 'Number')
table1.heading('file_name', text = 'File name')
table1.heading('format', text = 'Format')
table1.heading('date', text = 'Date')

for i in range(10):
    number=i+1
    file_name = 'nazwa pliku'
    format = '.pdf'
    date = '10.10.2023'
    data = [number, file_name, format, date]
    table1.insert(parent ='', index = 'end', values = data)

table1.pack()

#FRAME 2 - Adding rules and rules list (preview??)
frame_2 = ctk.CTkFrame (window,
                        width=200,
                        height = 50)
frame_2.pack(pady=10)
#add_button for rules
rule_add_button = ctk.CTkButton(master = frame_2,
                                text='Add rules'
                                )
rule_add_button.pack()

#frame 3 - Preview of changes - table with files and aplied rules in e.g red 

#frame 4 - Rename execute button
#frame 5 - excel import export buttons

#dataframe_functions.wuer_func()
#RUN
window.mainloop()