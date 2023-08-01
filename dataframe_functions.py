import customtkinter as ctk
from tkinter import filedialog as fd
import pandas as pd


#METHODS

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