
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