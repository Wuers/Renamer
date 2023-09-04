
#22.07.2023
import customtkinter as ctk
from tkinter import filedialog as fd

from tkinter import ttk
import sys
# import pandas as pd
import dataframe_functions

file_names_list = []

#button functions
def add_button_func():
    #1 selecting files
    global file_paths_list
    file_paths_list = fd.askopenfilenames(
        initialdir='E:/0_Wuer/5 Projekty/Python/P2_Renamer/TEST FILES'
        )
    
    global name_format_list
    def nested_files_list(file_path_list):
        #returns nested list of [[file1,fomart1][...]]
        #global format_index
        fetched_list = []
        for file in file_path_list:
            name_start_index = (file.rfind('/'))+1
            separator_index = (file.rfind('.'))
            format_start_index = separator_index +1
            name = file[name_start_index:separator_index]
            format = file [format_start_index:]
            pair = [name, format]
            fetched_list.append(pair)
        # adding information to preview table:    
        for file in fetched_list:
            number=(fetched_list.index(file))+1
            file_index = fetched_list.index(file)
            file_name = fetched_list[file_index][0]
            format = fetched_list[file_index][1]
            date = '10.10.2023'
            data = [number, file_name, format, date]
            table1.insert(parent ='', index = 'end', values = data)
        return fetched_list
                       
    
    #2 couting files
    selected_files_numb = len(file_paths_list)
    #3 displaying number of files
    counter_label.configure(text = f'({selected_files_numb}) files are selected')
    name_format_list=nested_files_list(file_paths_list)

    return name_format_list

def preview_func():
    global letters_numb
    letters_numb= letters_number_input.get()
    #print (f'Returned value is: {letters_numb}')
    #updating label:
    
    choosen_function_name = optionmenu_1.get()
    letters_label.configure(text =f'{letters_numb} would be {choosen_function_name}')
    return (letters_numb)

#GENERAL

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

#LAYOUT BELLOW
#window
window =ctk.CTk()
window.title('Renamer by Wuers')
window.geometry('600x600')

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

#Empty review table:
table1 = ttk.Treeview(window, columns =('number', 'file_name','format', 'date' ),show = 'headings')
table1.heading('number', text = 'Number')
table1.heading('file_name', text = 'File name')
table1.heading('format', text = 'Format')
table1.heading('date', text = 'Date')
table1.pack()


#FRAME 2 - Adding rules and rules list (preview??)
frame_2 = ctk.CTkFrame (window,
                        width=500,
                        height =550)
frame_2.pack(pady=10)
#add_button for rules
#rule_add_button = ctk.CTkButton(master = frame_2,
#                                text='Add rules')
#rule_add_button.pack()

#options - delete, add numbering find and change
#1)delete
optionmenu_1=ctk.CTkOptionMenu(master=frame_2,
                                values=['Delete', 'Add','Add numbering','Find and change'],
                                #command= 
                                )
optionmenu_1.set('Choose option')
optionmenu_1.pack()

letters_label= ctk.CTkLabel(frame_2, text = '')
letters_label.pack()

letter_var = ctk.IntVar()
letters_number_input = ctk.CTkEntry(master = frame_2)

letters_number_input.pack()

preview_button = ctk.CTkButton(master = frame_2, text = 'Preview', command = preview_func)
preview_button.pack()


#frame 3 - Preview of changes - table with files and aplied rules in e.g red 

#frame 4 - Rename execute button
#frame 5 - excel import export buttons
#RUN
window.mainloop()