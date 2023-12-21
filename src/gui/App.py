import os
from PIL import Image
import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
        super().__init__()

        # Configure window
        self.title("Strike")
        self.geometry(f"{1280}x{720}")
        self.minsize(720, 480)

        # Configure grid layout (2*1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        print(self.grid_size())

        # Create sidebar
        self.sidebar_frame = ctk.CTkFrame(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        # load images with light and dark mode image
        assets_path = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."), "assets")
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(assets_path, "logo.jpeg")),
                                       size=(64, 64))
        self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(assets_path, "home.png")),
                                       dark_image=Image.open(os.path.join(assets_path, "home_dark.png")),
                                       size=(26, 26))
        self.profiles_image = ctk.CTkImage(light_image=Image.open(os.path.join(assets_path, "profiles.png")),
                                           dark_image=Image.open(os.path.join(assets_path, "profiles_dark.png")),
                                           size=(26, 26))

        # create navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Strike",
                                                   image=self.logo_image,
                                                   compound="left",
                                                   font=ctk.CTkFont(size=24, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=48, pady=24)

        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="Home",
                                         font=ctk.CTkFont(size=18),
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.profiles_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40,
                                             border_spacing=10, text="Profiles",
                                             font=ctk.CTkFont(size=18),
                                             fg_color="transparent", text_color=("gray10", "gray90"),
                                             hover_color=("gray70", "gray30"),
                                             image=self.profiles_image, anchor="w",
                                             command=self.profiles_button_event)
        self.profiles_button.grid(row=2, column=0, sticky="ew")

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.navigation_frame,
                                                      values=["System", "Light", "Dark"],
                                                      command=App.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(2, weight=1)

        self.home_frame_label = ctk.CTkLabel(self.home_frame, text="Home", font=ctk.CTkFont(size=20, weight="bold"))
        self.home_frame_label.grid(row=1, column=0, padx=20, pady=10)

        # create profiles frame
        self.profiles_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.profiles_frame.grid_columnconfigure(0, weight=1)
        self.profiles_frame.grid_rowconfigure(0, weight=1)
        self.profiles_frame.grid_rowconfigure(2, weight=1)

        self.profiles_frame_label = ctk.CTkLabel(self.profiles_frame, text="Profiles",
                                                 font=ctk.CTkFont(size=20, weight="bold"))
        self.profiles_frame_label.grid(row=1, column=0, padx=20, pady=10)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.profiles_button.configure(fg_color=("gray75", "gray25") if name == "profiles" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "profiles":
            self.profiles_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.profiles_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def profiles_button_event(self):
        self.select_frame_by_name("profiles")

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)