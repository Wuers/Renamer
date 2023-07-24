
#22.07.2023
import customtkinter as ctk

#variables
files_numb = 4
#methods
def add_button_func():
    counter_output.set('counter_output value here')

#button
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
counter_output = ctk.StringVar()
counter_label = ctk.CTkLabel(
    master=window,
    text = 'This is Selected files counter label',
    textvariable = counter_output
)
counter_label.pack()

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

#frame 3 - Preview of changes
#frame 4 - Rename execute button
#frame 5 - excel import export buttons



#RUN
window.mainloop()