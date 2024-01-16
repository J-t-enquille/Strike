import customtkinter as ctk


class Profiles(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(corner_radius=0, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.profiles_frame_label = ctk.CTkLabel(self, text="Profiles",
                                                 font=ctk.CTkFont(size=20, weight="bold"))
        self.profiles_frame_label.grid(row=1, column=0, padx=20, pady=10)
