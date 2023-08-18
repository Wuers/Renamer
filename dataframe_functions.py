import customtkinter as ctk
from tkinter import filedialog as fd
import pandas as pd


#functions

def ws_counter_label (new_label_name, place, display_text):
    new_label_name = ctk.CTkLabel(
    master = place,
    text = display_text
    )
    new_label_name.pack()
    
def add_button_func2(new_label_name):
    #selection
    file_list2 = fd.askopenfilenames(
        initialdir= 'E:/0_Wuer/5 Projekty/Python/P2_Renamer/TEST FILES'
    )
    #counting 
    selected_files_numb2 = len(file_list2)
    # displaying number of files
    new_label_name.configure(text = f'({selected_files_numb2}) files are selected')
    #return (selected_files_numb2)

"""#functions should be use to operate on file nemes with iterations
not using global variables:
1)CTK function should return data: list of file names - 


def add_button_func():
    #selecting files, counting them and returning number
    file_list = fd.askopenfilenames(
        initialdir='E:/0_Wuer/5 Projekty/Python/P2_Renamer/TEST FILES'
        )
    #2 couting files
    return len(file_list)
    """