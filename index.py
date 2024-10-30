import customtkinter as ctk
from database.db import Database
from modules.user import User
from tkinter import filedialog

db = Database()

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Injection Dashboard")
        self._appearance = ctk.set_appearance_mode("dark")
        self._color = ctk.set_default_color_theme("blue")
        self.geometry(f"{1100}x{700}")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=3)
        self.grid_rowconfigure((0,1,2,3), weight=1)

        # Database and summary data
        self.data = db.fetch()
        self.total_hatched = 0
        self.total_injected = 0
        self.calculate_totals()

        # Main data frame
        self.data_frame = ctk.CTkFrame(self, corner_radius=0)
        self.data_frame.grid(row=0, column=2, rowspan=4, sticky="nswe")
        self.data_frame.grid_rowconfigure((0), weight=1)
        self.data_frame.grid_columnconfigure((0), weight=1)

        # Default/general data frame
        self.create_general_content()

        # Selection frame with buttons
        self.selection_frame = ctk.CTkFrame(self, corner_radius=0)
        self.selection_frame.grid(row=0, column=0, columnspan=2, rowspan=4, sticky='nswe')
        self.selection_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        self.selection_frame.grid_columnconfigure(0, weight=1)


        # Selection
        self.rich_button = ctk.CTkButton(self.selection_frame, text='Richard', command=lambda: self.show_frame('Richard'))
        self.rich_button.grid(row=0, column=0, padx=20, pady=20)
        self.kirin_button = ctk.CTkButton(self.selection_frame, text='Kirin', command=lambda: self.show_frame('Kirin'))
        self.kirin_button.grid(row=1, column=0, padx=20, pady=20)
        self.dylan_button = ctk.CTkButton(self.selection_frame, text='Dylan', command=lambda: self.show_frame('Dylan'))
        self.dylan_button.grid(row=2, column=0, padx=20, pady=20)
        self.connor_button = ctk.CTkButton(self.selection_frame, text='Connor', command=lambda: self.show_frame('Connor'))
        self.connor_button.grid(row=3, column=0, padx=20, pady=20)

        # Reset button to show the general frame again
        self.reset_button = ctk.CTkButton(self.selection_frame, text='Reset', command=self.return_to_menu)
        self.reset_button.grid(row=4, column=0, padx=20, pady=20)

        # Show the general frame by default
        # self.general_frame.tkraise()

    def calculate_totals(self):
        for row in self.data:
            self.total_hatched += row['hatched']
            self.total_injected += row['injected']
        self.total_hatched_rate = 100 * self.total_hatched / self.total_injected if self.total_injected else 0

    def upload_media(self):
        file_path = filedialog.askopenfilename()
        print(file_path)

    def create_general_content(self):
        for widget in self.data_frame.winfo_children():
            widget.destroy()
        self.general_frame = ctk.CTkFrame(self.data_frame, corner_radius=0)
        self.general_frame.grid(row=0, column=0, sticky="nswe")
        label = ctk.CTkLabel(self.general_frame, text="Data Analysis", font=('Times New Roman', 30))
        label.pack(pady=20)
        self.total_injected_label = ctk.CTkLabel(self.general_frame, text=f'Total Injected: {self.total_injected}')
        self.total_injected_label.pack(pady=10)
        self.total_hatched_label = ctk.CTkLabel(self.general_frame, text=f'Total Hatched: {self.total_hatched}')
        self.total_hatched_label.pack(pady=10)
        self.total_rate = ctk.CTkLabel(self.general_frame, text=f'Hatching Rate: {self.total_hatched_rate:.2f}%')
        self.total_rate.pack(pady=10)
        self.upload_button = ctk.CTkButton(self.general_frame, text="upload data", command=self.upload_media)
        self.upload_button.pack(pady=10)

    def return_to_menu(self):
        self.create_general_content()

    def show_frame(self, name):
        self.general_frame.destroy()
        User(self.master, self.data_frame, name)

        



if __name__ == '__main__':
    app = App()
    app.mainloop()
