import customtkinter as ctk
from tkinter import filedialog as fd
from tkinter import ttk
import sys
import os
import datetime


file_names_list = []
#button functions
def f_add_button():
    #1 selecting files, returns list of files directories
    global file_paths_list
    file_paths_list = fd.askopenfilenames(
        initialdir='E:/0_Wuer/5 Projekty/Python/P2_Renamer/TEST FILES'
        )
    #loop that removes all files from table:
    for item in table1.get_children():
        table1.delete(item)
        
    global name_format_list
    def f_nested_files_list(file_path_list):
        #returns nested list of [[name1,format1,date1,file1_path](...)]
        #global format_index
        global fetched_list
        fetched_list = []
        for file in file_path_list:
            name = os.path.basename(file)
            name_without_exntension = os.path.splitext(name)[0]
            format = os.path.splitext(name)[1][1:]
            creation_time = os.path.getctime(file)
            creation_date = datetime.datetime.fromtimestamp(creation_time)
            formated_creation_date = creation_date.strftime("%Y-%m-%d %H:%M")
            #item is a tuple - file information.
            item = [name_without_exntension, format, formated_creation_date, file]
            fetched_list.append(item)
        # adding information to preview table:    
      
        for index,file in enumerate(fetched_list, start=1):
            file_name, format, date, full_path = file
            data = [index, file_name, format, date]
            table1.insert(parent='', index='end', values=data)
        return fetched_list
                       
    
    #2 couting files
    selected_files_numb = len(file_paths_list)
    #3 displaying number of files
    counter_label.configure(text = f'({selected_files_numb}) files are selected')
    name_format_list=f_nested_files_list(file_paths_list)

    return name_format_list

def validate_insert_if_int(V):
    #function to validate if inserted character is int
    if V == "" or V.isdigit():
        return True
    else:
        return False

def get_delete_value():
    #function that return int value from delete_entry
    global delete_entry
    value = delete_entry.get()
    if value.isdigit():
        return int(value)
    else:
        print ("Please insert only value, not string etc")
        return None
    
def delete_preview(): 
    num_chars = get_delete_value()
    if num_chars is not None:
        global position
        position = radio_var.get()
        global fetched_list
        new_fetched_list, old_and_new_paths = delete_from_filenames(num_chars, position, fetched_list)
        for old, new in old_and_new_paths:
            print(f"OLD: {old}")
            print(f"NEW: {new}")
            print("-----")
        update_table(new_fetched_list)
    else:
        print ("num_chars is bugged. Current value:", num_chars)

def save_delete_preview():
    # call delete_from_filenames to get old and new file paths
    num_chars = get_delete_value()
    position = radio_var.get()
    global fetched_list
    
    modified_list, old_and_new_path = delete_from_filenames(num_chars, position, fetched_list)
    for old_path, new_path in old_and_new_path:
        try:
            os.rename(old_path, new_path)
        except OSError as e:
            print(f"Error renaming {old_path} to {new_path}: {e}")

    # update table with new names
    update_table(modified_list)
    
def option_callback(choice):
    #function that displays elements needed for the function that has been selected
    global func_frame

    clear_frame()

    if choice =="Delete":
        #label with info:
        title_label2.configure(text="Can delete given number of chars from begginng or from end of choosen file names")
        #creating frame for specific function:
        func_frame = ctk.CTkFrame(master=frame_2, width=400)
        func_frame.pack(pady=10)

        global radio_var
        radio_var = ctk.StringVar(value="")
        radio_buttons_frame = ctk.CTkFrame(master=func_frame)
        radio_buttons_frame.pack()
        radio_1 = ctk.CTkRadioButton(master=radio_buttons_frame, text="At the beginning", variable=radio_var, value="beginning")
        
        radio_1.grid(row=0, column=0, pady=10)
        radio_2 = ctk.CTkRadioButton(master=radio_buttons_frame, text="From end", variable=radio_var, value="end")
        
        radio_2.grid(row=0, column=2, pady=10)
        #entry to insert number of characters thats going to be deleted:
        validate_cmd=radio_buttons_frame.register(validate_insert_if_int)

        #entry to insert number:
        global delete_entry
        delete_entry = ctk.CTkEntry(
            master=radio_buttons_frame,
            placeholder_text="insert number of character to be deleted",
            width=250,
            validate="key",
            validatecommand=(validate_cmd, '%P')
            )
        delete_entry.grid(row=1, column =1, pady=10)

        #button to send value and preview:
        func_d_preview_button = ctk.CTkButton(
            master=radio_buttons_frame,
            text="Preview",
            command=delete_preview
        )
        func_d_preview_button.grid(row=2, column=2, pady=10)

        #button to save changes to files
        func_d_save_button = ctk.CTkButton(
            master=radio_buttons_frame,
            text="SAVE CHANGES",
            command=save_delete_preview
        )
        func_d_save_button.grid(row=2, column=3, pady=10)

    elif choice =="Add":
        

        title_label2.configure(text="Add")
        #func_frame = ctk.CTkFrame(master=frame_2, width=400)
        #func_frame.pack()
        #another functionalities
        
    elif choice =="Add numbering":
        
        title_label2.configure(text="Add numbering")
        func_frame = ctk.CTkFrame(master=frame_2, width=400)
        

    elif choice =="Find and change":
        
        title_label2.configure(text="Find and change")
        func_frame = ctk.CTkFrame(master=frame_2, width=400)
    
    func_frame.pack()

def delete_from_filenames(num_chars, position, list):
    #function that returns two list: new, modified and list with old and new paths
    modified_list = []
    old_and_new_path = []
    for item in list:
        try:
            name, format, date, full_path = item
        except ValueError as e:
            print ("error is: ", e)
            print (f"error when unpacking tuple 'item'. problematic element: {item}")
            continue
        if position == "beginning":
            new_name = name[num_chars:]
        elif position == "end":
            new_name = name[:-num_chars] if len(name) > num_chars else ""
        else:
            new_name = name

        old_path = full_path
        #new_path = os.path.join(os.path.dirname(full_path), f"{new_name}.{format}")
        new_path = os.path.normpath(os.path.join(os.path.dirname(full_path), f"{new_name}.{format}"))

        modified_list.append([new_name, format, date, new_path])
        old_and_new_path.append((old_path, new_path))

    return modified_list, old_and_new_path

def update_table(new_list):
#function to update table
    #delete current preview
    for item in table1.get_children():
        table1.delete(item)
    #add new preview
    for index, item in enumerate(new_list, start=1):
        name, format, date, full_path = item
        table1.insert('', 'end', values=(index, name, format, date))

def clear_frame():

    global func_frame
    if 'func_frame' in globals() and func_frame.winfo_exists():
        func_frame.destroy()
    #else:
    #    print (f"no frame found")
    

#GENERAL
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
#LAYOUT BELLOW
#window
window =ctk.CTk()
window.title('Renamer by Wuers')
window.geometry('800x800')
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
                                command=f_add_button
                                )
file_add_button.pack()

#Label - button updated label -live Counter
counter_label = ctk.CTkLabel(
    master = frame_1,
    text = 'Files not selected'
)
counter_label.pack()

#Empty review table:
table1 = ttk.Treeview(window, columns =('number', 'old_file_name','new_file_name','format', 'date'), 
                      show = 'headings')
table1.heading('number', text = 'Number') 
table1.heading('old_file_name', text = 'File name')
table1.heading('new_file_name', text ='New file name')
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
title_label2.pack()

#preview table:
prev_table = ctk.CTkTabview

window.mainloop()