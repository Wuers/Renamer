import customtkinter as ctk
from tkinter import filedialog as fd
from tkinter import ttk
import sys
import os
import datetime

# import pandas as pd?

#import my functions from file:
#import dataframe_functions as dff

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
        #returns nested list of [[file1,format1,date1](...)]
        #global format_index
        fetched_list = []
        for file in file_path_list:
            name_start_index = (file.rfind('/'))+1
            separator_index = (file.rfind('.'))
            format_start_index = separator_index +1
            name = file[name_start_index:separator_index]
            format = file [format_start_index:]
            creation_time = os.path.getctime(file)
            creation_date = datetime.datetime.fromtimestamp(creation_time)
            formated_creation_date = creation_date.strftime("%Y-%m-%d %H:%M")
            pair = [name, format, formated_creation_date]
            fetched_list.append(pair)
        # adding information to preview table:    
        for file in fetched_list:
            number=(fetched_list.index(file))+1
            file_index = fetched_list.index(file)
            file_name = fetched_list[file_index][0]
            format = fetched_list[file_index][1]
            date = fetched_list[file_index][2]
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

def validate_insert_if_int(V):
    if V == "" or V.isdigit():
        return True
    else:
        return False

def get_delete_value():
    global delete_entry
    value = delete_entry.get()
    if value.isdigit():
        print (f"value is ok")
        return int(value)
    else:
        print ("Please insert only value, not string etc")
    return None

def option_callback(choice):
    if choice =="Delete":
        title_label2.configure(text="Wybrano opcję Delete")

        radio_frame = ctk.CTkFrame(master=frame_2, width=400)
        radio_frame.pack(pady=10)
        radio_var = ctk.StringVar(value="")

        radio_buttons_frame = ctk.CTkFrame(master=radio_frame)
        radio_buttons_frame.pack()

        radio_1 = ctk.CTkRadioButton(master=radio_buttons_frame, text="At beginning", variable=radio_var, value="beginning")
        #radio_1.pack(side="left", padx=(0, 5))
        radio_1.grid(row=0, column=0, pady=10)
        radio_2 = ctk.CTkRadioButton(master=radio_buttons_frame, text="From end", variable=radio_var, value="end")
        #radio_1.pack(side="left", padx=(5, 0))
        radio_2.grid(row=0, column=2, pady=10)
        #entry to insert number of characters thats going to be deleted:
        validate_cmd=radio_buttons_frame.register(validate_insert_if_int)

        global delete_entry
        delete_entry = ctk.CTkEntry(
            master=radio_buttons_frame,
            placeholder_text="insert number of character to be deleted",
            width=250,
            validate="key",
            validatecommand=(validate_cmd, '%V')
            )
        delete_entry.grid(row=1, column =1, pady=10)

        #button to send value:
        delete_process_button = ctk.CTkButton(
            master=radio_buttons_frame,
            text="Confirm",
            command=get_delete_value
        )
        delete_process_button.grid(row=2, column=2, pady=10)

    elif choice =="Add":
        title_label2.configure(text="Wybrano opcję Add")
    elif choice =="Add numbering":
        title_label2.configure(text="Wybrano opcję Add numbering")
    elif choice =="Find and change":
        title_label2.configure(text="Wybrano opcję Find and change")
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
table1.heading('date', text = 'Creation date')
table1.pack()


#FRAME 2 - Choosing operation setting
frame_2 = ctk.CTkFrame(master=window)
frame_2.pack(pady=20, padx=20, fill="both", expand=True)

#FRAME 3 - confirmation
frame_3 = ctk.CTkFrame(master=window)
frame_3.pack(pady=20, padx=20, fill="both", expand=True)

#options - delete, add numbering find and change
#1)delete
optionmenu_1=ctk.CTkOptionMenu(master=frame_2,
                                values=['Delete', 'Add','Add numbering','Find and change'],
                                command=option_callback)
optionmenu_1.set('Choose option')
optionmenu_1.pack()



title_label2 = ctk.CTkLabel(master=frame_2,height=20,width=100,
                           padx=10, pady=20,
                           text="Select Files and Rules:")
#title_label2.pack()

#letters_label= ctk.CTkLabel(frame_3, text = '')
#letters_label.pack()

#letters_number_input = ctk.CTkEntry(master = frame_3)
#letters_number_input.pack()

#preview_button = ctk.CTkButton(master = frame_3, text = 'Preview', command = preview_func)
#preview_button.pack()


#frame 3 - Preview of changes - table with files and aplied rules in e.g red 

#frame 4 - Rename execute button

#RUN
window.mainloop()