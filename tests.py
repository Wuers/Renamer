
#22.07.2023
import customtkinter as ctk

#button
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

buttonapp = ctk.CTk()
buttonapp.geometry("400x240")
buttonapp.title("Button.exe")

def button_function():
    print("button pressed")

button = ctk.CTkButton(master=buttonapp, text = "Button", command = button_function)
button.place(relx=0.5, rely=0.5, anchor = ctk.CENTER)

#buttonapp.mainloop()

#window
window =ctk.CTk()
window.title('custom app')
window.geometry('600x400')

#widgets
label = ctk.CTkLabel(master = window, text = 'A ctk label')
label.pack()

#button
def add_button_func():
    print("i will be usefull some day :)")

add_button = ctk.CTkButton (master = window, text = "ADD", command = add_button_func)
add_button.pack()

#frame
frame = ctk.CTkFrame(master = window)
frame.pack()

#slider
slider = ctk.CTkSlider (master = frame)
slider.pack(padx = 20, pady=20)

#switch
switch = ctk.CTkSwitch(window, text='Exercise Switch',
                       switch_height=30,
                       switch_width=50,
                       corner_radius=2,
                       button_hover_color='yellow',
                       progress_color="white",
                       fg_color='red',
                       border_color='blue',
                       button_color='green')
switch.pack()

#switch example
def switch_event():
    print("switch toggled, current value:", switch_var.get())
switch_var = ctk.StringVar(value="on")
switch2 = ctk.CTkSwitch(window, text="CTkSwitch", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")
switch2.pack()

#RUN
window.mainloop()