import customtkinter as ctk

class User(ctk.CTkFrame):
    def __init__(self, master, data_frame, name):
        super().__init__(master)
        self._appearance = ctk.set_appearance_mode("dark")
        self._color = ctk.set_default_color_theme("blue")

        self.name_label = ctk.CTkLabel(data_frame, text=f"Name:{name}", font=("Arial", 12), text_color="white")
        self.name_label.grid(row=0, column=0)
