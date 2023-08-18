
#22.07.2023
import customtkinter as ctk
from tkinter import filedialog as fd
import dataframe_functions

file_list = []

#button functions
def add_button_func():
    #1 selecting files
    file_list = fd.askopenfilenames(
        initialdir='E:/0_Wuer/5 Projekty/Python/P2_Renamer/TEST FILES'
        )
    #2 couting files
    selected_files_numb = len(file_list)
    #3 displaying number of files
    counter_label.configure(text = f'({selected_files_numb}) files are selected')
    return file_list

#GENERAL
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

#LAYOUT BELLOW
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
#add_button for files
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

#live Counter - button updated label
counter_label = ctk.CTkLabel(
    master = frame_1,
    text = 'Files not selected'
)
counter_label.pack()


#dataframe_functions.ws_counter_label('label3', frame_1,'files not selected2')
#dataframe_functions.add_button_func2(label3)

#preview table?

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