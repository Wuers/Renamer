
#22.07.2023
import customtkinter as ctk
from tkinter import filedialog as fd
import pandas as pd
# df from list?
#variables
files_numb = 4
#methods
def add_button_func():
    #1 selecting files
    file_list = fd.askopenfilenames(
        initialdir='C:/Users'
        )
    #2 couting files
    selected_files_numb = len(file_list)
    #3 displaying number of files
    counter_label.configure(text = f'({selected_files_numb}) files are selected')

#general
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

#window
window =ctk.CTk()
window.title('Renamer by Wuers')
window.geometry('600x400')
#label
title_label = ctk.CTkLabel(window,height=20,width=100,
                           padx=10, pady=20,
                           text="Select Files and Rules:")
title_label.pack()

#FRAME 1 - Adding files and live counter
frame_1 = ctk.CTkFrame (window,
                        width=200,
                        height = 50)
frame_1.pack(pady=10)
#add_button
file_add_button = ctk.CTkButton(master = frame_1,
                                text='Add files',
                                command=add_button_func
                                )
file_add_button.pack()
#live Counter - button updated label
counter_label = ctk.CTkLabel(
    master = frame_1,
    text = 'Files not selected'
)
counter_label.pack()

#preview table?

#FRAME 2 - Adding rules and rules list (preview??)
frame_2 = ctk.CTkFrame (window,
                        width=200,
                        height = 50)
frame_2.pack(pady=10)
#add_button
rule_add_button = ctk.CTkButton(master = frame_2,
                                text='Add rules'
                                )
rule_add_button.pack()

#frame 3 - Preview of changes - table with files and aplied rules in e.g red 

#frame 4 - Rename execute button
#frame 5 - excel import export buttons


#RUN
window.mainloop()