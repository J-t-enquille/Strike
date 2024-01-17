import os
from PIL import Image
import customtkinter as ctk
import random
from functools import partial
<<<<<<< HEAD

=======
from src.gui.components.Profiles import Profiles
>>>>>>> e9478d8eeae222fc9274c8be905ef1a2afdfa195

def random_color():
    red = random.randint(30, 225)
    green = random.randint(30, 225)
    blue = random.randint(30, 225)

    color_hex = "#{:02X}{:02X}{:02X}".format(red, green, blue)

    return color_hex


class PlayerInfoWidgets:
    def __init__(self, playername, rounds, scoretab_frame):
        self.playerscore_frame = ctk.CTkFrame(scoretab_frame, corner_radius=0, fg_color="transparent")
        self.playerscore_label = ctk.CTkLabel(self.playerscore_frame, text=playername,
                                              font=ctk.CTkFont(size=20, weight="bold"))
        self.playerscore_label.grid(row=0, column=0, padx=20, pady=10)
        self.scorecase_frame_tab = []
        for round in range(rounds):
            self.scorecase_frame_tab.append(ScoreCaseFrame(round, rounds, self.playerscore_frame))
            self.scorecase_frame_tab[round].scorecase_frame.grid(row=0, column=round + 1, padx=2, pady=5)
            self.scorecase_frame_tab[round].scorecase_frame.grid_columnconfigure(0, weight=1)
            self.scorecase_frame_tab[round].scorecase_frame.grid_rowconfigure(2, weight=1)
            self.scorecase_frame_tab[round].trials_frame.grid(row=0, column=0)
            self.scorecase_frame_tab[round].trials_frame.grid_columnconfigure(3, weight=1)
            self.scorecase_frame_tab[round].trials_frame.grid_rowconfigure(1, weight=1)
            self.scorecase_frame_tab[round].firsttrial_frame.grid(row=0, column=0)
            self.scorecase_frame_tab[round].firsttrial_label.grid(row=0, column=0, padx=10)
            self.scorecase_frame_tab[round].secondtrial_frame.grid(row=0, column=1)
            self.scorecase_frame_tab[round].secondtrial_label.grid(row=0, column=0, padx=10)
            if round == rounds - 1:
                self.scorecase_frame_tab[round].thirdtrial_frame.grid(row=0, column=2)
                self.scorecase_frame_tab[round].firsttrial_label.grid(row=0, column=0, padx=5)
                self.scorecase_frame_tab[round].secondtrial_label.grid(row=0, column=0, padx=5)
                self.scorecase_frame_tab[round].thirdtrial_label.grid(row=0, column=0, padx=5)
            self.scorecase_frame_tab[round].sumscoretrial_frame.grid(row=1, column=0)
            self.scorecase_frame_tab[round].sumscoretrial_label.grid(row=0, column=0, padx=20, pady=10)
        self.totalscore_frame = ctk.CTkFrame(self.playerscore_frame, corner_radius=0, fg_color="transparent")
        self.totalscore_frame.grid(row=0, column=rounds + 1, padx=20, pady=10)
        self.totalscore_label = ctk.CTkLabel(self.totalscore_frame, text="0",
                                             font=ctk.CTkFont(size=20, weight="bold"))
        self.totalscore_label.grid(row=0, column=0, padx=20, pady=10)


class ScoreCaseFrame:
    def __init__(self, activeround, rounds, playerscore_frame):
        self.scorecase_frame = ctk.CTkFrame(playerscore_frame, corner_radius=10)
        self.trials_frame = ctk.CTkFrame(self.scorecase_frame, corner_radius=0, fg_color="transparent")
        self.firsttrial_frame = ctk.CTkFrame(self.trials_frame, corner_radius=0, fg_color="transparent")
        self.firsttrial_label = ctk.CTkLabel(self.firsttrial_frame, text="1",
                                             font=ctk.CTkFont(size=20, weight="bold"))
        self.secondtrial_frame = ctk.CTkFrame(self.trials_frame, corner_radius=0, fg_color="transparent",
                                              border_width=2)
        self.secondtrial_label = ctk.CTkLabel(self.secondtrial_frame, text="2",
                                              font=ctk.CTkFont(size=20, weight="bold"))
        if activeround == rounds - 1:
            self.thirdtrial_frame = ctk.CTkFrame(self.trials_frame, corner_radius=0, fg_color="transparent",
                                                 border_width=2)
            self.thirdtrial_label = ctk.CTkLabel(self.thirdtrial_frame, text="3",
                                                 font=ctk.CTkFont(size=20, weight="bold"))
        self.sumscoretrial_frame = ctk.CTkFrame(self.scorecase_frame, corner_radius=0, fg_color="transparent")
        self.sumscoretrial_label = ctk.CTkLabel(self.sumscoretrial_frame, text="3",
                                                font=ctk.CTkFont(size=20, weight="bold"))


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

        # load images with light and dark mode image
        assets_path = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), ".."), "assets")
        # Icons and images ----------------------------------------------------------------
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(assets_path, "logo.jpeg")),
                                       size=(64, 64))
        self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(assets_path, "home.png")),
                                       dark_image=Image.open(os.path.join(assets_path, "home_dark.png")),
                                       size=(26, 26))
        self.profiles_image = ctk.CTkImage(light_image=Image.open(os.path.join(assets_path, "profiles.png")),
                                           dark_image=Image.open(os.path.join(assets_path, "profiles_dark.png")),
                                           size=(26, 26))
<<<<<<< HEAD
        self.play_image = ctk.CTkImage(light_image=Image.open(os.path.join(assets_path, "newgame.png")),
                                       dark_image=Image.open(os.path.join(assets_path, "newgame_dark.png")),
                                       size=(26, 26))
=======
        self.newgame_image = ctk.CTkImage(light_image=Image.open(os.path.join(assets_path, "newgame.png")),
                                          dark_image=Image.open(os.path.join(assets_path, "newgame_dark.png")),
                                          size=(26, 26))
>>>>>>> e9478d8eeae222fc9274c8be905ef1a2afdfa195
        self.home_bowling_image = ctk.CTkImage(light_image=Image.open(os.path.join(assets_path, "home_img.png")),
                                               dark_image=Image.open(os.path.join(assets_path, "home_img_dark.png")),
                                               size=(400, 400))
        # ---------------------------------------------------------------------------------
        # create sidebar frame
        self.sidebar_frame = ctk.CTkFrame(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # Global Logo frame containing logo / title / description => 1 row, 2 columns
        self.sidebar_logo_frame = ctk.CTkFrame(self.sidebar_frame, corner_radius=0, fg_color="transparent")
        self.sidebar_logo_frame.grid(row=0, column=0, sticky="ew", pady=24, padx=32)

        self.sidebar_logo_frame_logo = ctk.CTkLabel(self.sidebar_logo_frame,
                                                    image=self.logo_image,
                                                    text="")
        self.sidebar_logo_frame_logo.grid(row=0, column=0)

        # Text beside logo => Frame with 1 column, 2 rows
        self.sidebar_logo_text_frame = ctk.CTkFrame(self.sidebar_logo_frame, corner_radius=0, fg_color="transparent")
        self.sidebar_logo_text_frame.grid(row=0, column=1, padx=(12, 0))

        self.sidebar_logo_frame_label = ctk.CTkLabel(self.sidebar_logo_text_frame, text="Strike",
                                                     font=ctk.CTkFont(size=24, weight="bold"))
        self.sidebar_logo_frame_label.grid(row=0, column=0, sticky="w")
        self.sidebar_logo_frame_description = ctk.CTkLabel(self.sidebar_logo_text_frame, text="Bowling scoring app",
                                                           font=ctk.CTkFont(size=14))
        self.sidebar_logo_frame_description.grid(row=1, column=0, sticky="w")

        # Buttons used for "routes"
        self.home_button = ctk.CTkButton(self.sidebar_frame, corner_radius=0, height=40, border_spacing=10,
                                         text="Home",
                                         font=ctk.CTkFont(size=18),
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.profiles_button = ctk.CTkButton(self.sidebar_frame, corner_radius=0, height=40,
                                             border_spacing=10, text="Profiles",
                                             font=ctk.CTkFont(size=18),
                                             fg_color="transparent", text_color=("gray10", "gray90"),
                                             hover_color=("gray70", "gray30"),
                                             image=self.profiles_image, anchor="w",
                                             command=self.profiles_button_event)
        self.profiles_button.grid(row=2, column=0, sticky="ew")

<<<<<<< HEAD
        self.play_button = ctk.CTkButton(self.sidebar_frame, corner_radius=0, height=40,
                                         border_spacing=10, text="Play",
                                         font=ctk.CTkFont(size=18),
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         image=self.play_image, anchor="w",
                                         command=self.play_button_event)
        self.play_button.grid(row=3, column=0, sticky="ew")
=======
        self.newgame_button = ctk.CTkButton(self.sidebar_frame, corner_radius=0, height=40,
                                            border_spacing=10, text="New Game",
                                            font=ctk.CTkFont(size=18),
                                            fg_color="transparent", text_color=("gray10", "gray90"),
                                            hover_color=("gray70", "gray30"),
                                            image=self.newgame_image, anchor="w",
                                            command=self.newgame_button_event)
        self.newgame_button.grid(row=3, column=0, sticky="ew")
>>>>>>> e9478d8eeae222fc9274c8be905ef1a2afdfa195

        self.appearance_mode_menu = ctk.CTkOptionMenu(self.sidebar_frame,
                                                      values=["System", "Light", "Dark"],
                                                      command=App.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # ========= Pages displayed from "routes" ===================
        # create home frame
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(2, weight=1)

        self.home_frame_label = ctk.CTkLabel(self.home_frame, text="Welcome,\n start a new game to begin. ",
                                             font=ctk.CTkFont(size=20, weight="bold"))
        self.home_frame_label.grid(row=1, column=0, padx=20, pady=10)

        self.home_frame_label.grid(row=1, column=0, padx=20, pady=10)
        self.home_frame_bowling_image = ctk.CTkLabel(self.home_frame,
                                                     image=self.home_bowling_image,
                                                     text="")
        self.home_frame_bowling_image.grid(row=2, column=0, padx=20, pady=10)

        # create profiles frame
        self.profiles_frame = Profiles(self)

        # create play frame
        self.play_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.play_frame.grid_columnconfigure(0, weight=1)
        self.play_frame.grid_rowconfigure(0, weight=1)
        self.play_frame.grid(row=0, column=0, sticky="nsew")

<<<<<<< HEAD
        class SettingsGame:
            def __init__(self, numberofbowlingpins, numberofrounds):
                self.numberofbowlingpins = numberofbowlingpins
                self.numberofrounds = numberofrounds
                self.playersofthisgame = []

        self.settings = SettingsGame(10, 10)
        # create settings frame of play frame
        self.settings_frame = ctk.CTkFrame(self.play_frame, corner_radius=0, fg_color="transparent")
        self.settings_frame.grid(row=0, column=0, sticky="nsew")
        self.settings_frame.grid_columnconfigure(0, weight=1)
        self.settings_frame.grid_rowconfigure(0, weight=1)
        self.settings_frame.grid_rowconfigure(3, weight=1)

        self.newplayer_frame = ctk.CTkFrame(self.settings_frame, corner_radius=0, fg_color="transparent")
        self.newplayer_frame.grid(row=0, column=0, padx=20, pady=10, sticky="s")
        self.newplayer_frame_label = ctk.CTkLabel(self.newplayer_frame, text="Select players for the game",
                                                  font=ctk.CTkFont(size=20, weight="bold"))
        self.newplayer_frame_label.grid(row=0, column=0, padx=20, pady=10, sticky="n")
=======
        self.newplayer_frame_label = ctk.CTkLabel(self.newgame_frame, text="Select players for the game",
                                                  font=ctk.CTkFont(size=20, weight="bold"))
        self.newplayer_frame_label.grid(row=0, column=0, padx=20, pady=10, sticky="s")
>>>>>>> e9478d8eeae222fc9274c8be905ef1a2afdfa195

        self.player_list_frame = ctk.CTkFrame(self.newplayer_frame, corner_radius=0, fg_color="transparent")
        self.player_list_frame.grid(row=1, column=0, padx=20, pady=10)

        self.list_player = ["Vladimir", "Gaston", "Julie", "Lorenzo"]
        self.player_button = {}
        i = 0
        row = 0
        for player in self.list_player:
            color = random_color()
            self.player_button[player] = ctk.CTkButton(self.player_list_frame, text=player,
                                                       font=ctk.CTkFont(size=20, weight="bold"), fg_color=color,
                                                       corner_radius=10, command=partial(self.selectplayer, player))
        for player in self.player_button:
            self.player_button[player].grid(row=row, column=i, padx=5, pady=10)
            i += 1
            if i == 4:
                i = 0
                row += 1

        self.newplayer_entry_frame = ctk.CTkFrame(self.newplayer_frame, corner_radius=0, fg_color="transparent")
        self.newplayer_entry_frame.grid(row=2, column=0, padx=20, pady=10, sticky="n")
        self.newplayer_entry = ctk.CTkEntry(self.newplayer_entry_frame, corner_radius=10, height=50, width=300)
        self.newplayer_entry.grid(row=0, column=0, padx=20, pady=10)

        self.newplayer_button = ctk.CTkButton(self.newplayer_entry_frame, corner_radius=10, height=50,
                                              text="New player",
                                              command=lambda: self.createplayer_button(self.newplayer_entry.get()))
        self.newplayer_button.grid(row=0, column=1, padx=20, pady=10)
        self.warning_label = ctk.CTkLabel(self.newplayer_entry_frame, text="",
                                          font=ctk.CTkFont(size=20, weight="bold", slant="italic"), text_color="red")
<<<<<<< HEAD

        self.configgame_frame = ctk.CTkFrame(self.settings_frame, corner_radius=0, fg_color="transparent")
        self.configgame_frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")
        self.numberofbowlingpins_frame = ctk.CTkFrame(self.configgame_frame, corner_radius=0, fg_color="transparent")
        self.numberofbowlingpins_frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")
        self.numberofbowlingpins_frame_label = ctk.CTkLabel(self.numberofbowlingpins_frame,
                                                            text="Number of bowling pins :",
                                                            font=ctk.CTkFont(size=20, weight="bold"))
        self.numberofbowlingpins_frame_label.grid(row=0, column=0, padx=20, pady=10, sticky="n")
        self.numberofbowlingpins_frame_entry = ctk.CTkEntry(self.numberofbowlingpins_frame, corner_radius=10, height=50,
                                                            width=100, placeholder_text="10")
        self.numberofbowlingpins_frame_entry.grid(row=0, column=1, padx=20, pady=10, sticky="n")
        self.numberofrounds_frame = ctk.CTkFrame(self.configgame_frame, corner_radius=0, fg_color="transparent")
        self.numberofrounds_frame.grid(row=1, column=2, padx=20, pady=10, sticky="n")
        self.numberofrounds_frame_label = ctk.CTkLabel(self.numberofrounds_frame,
                                                       text="Number of rounds :",
                                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.numberofrounds_frame_label.grid(row=0, column=0, padx=20, pady=10)
        self.numberofrounds_frame_entry = ctk.CTkEntry(self.numberofrounds_frame, corner_radius=10, height=50,
                                                       width=100, placeholder_text="10")
        self.numberofrounds_frame_entry.grid(row=0, column=1, padx=20, pady=10)

        self.startgame_frame = ctk.CTkFrame(self.settings_frame, corner_radius=0, fg_color="transparent")
        self.startgame_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ne")
        self.startgame_button = ctk.CTkButton(self.startgame_frame, corner_radius=10, height=50, width=100,
                                              text="Start", font=ctk.CTkFont(size=20, weight="bold"),
                                              command=self.startgame, state="disabled")
        self.startgame_button.grid(row=0, column=0, padx=20, pady=10)

        # create playgame frame of play frame
        self.activeplayer = 0
        self.activeround = 1

        self.playgame_frame = ctk.CTkFrame(self.play_frame, corner_radius=0, fg_color="transparent")
        self.playgame_frame.grid_columnconfigure(0, weight=1)
        self.playgame_frame.grid_rowconfigure(0, weight=1)
        self.playgame_frame.grid_rowconfigure(2, weight=1)

        self.scoretab_frame = ctk.CTkFrame(self.playgame_frame, corner_radius=0, fg_color="transparent")
        self.scoretab_frame.grid(row=0, column=0, padx=20, pady=10)
        self.scoretab_frame.grid_rowconfigure(0, weight=1)
        self.scoretab_frame.grid_columnconfigure(1, weight=1)
        self.headertab_frame = ctk.CTkFrame(self.scoretab_frame, corner_radius=0, fg_color="transparent")
        self.headertab_frame.grid(row=0, column=0, padx=20, pady=10)
        self.playerscore_widgets = {}

        self.enterscore_frame = ctk.CTkFrame(self.playgame_frame, corner_radius=0, fg_color="transparent")
        self.enterscore_frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")
        self.enterscore_label = ctk.CTkLabel(self.enterscore_frame,
                                             text="Enter score for ", font=ctk.CTkFont(size=20, weight="bold"))
        self.enterscore_label.grid(row=0, column=0, padx=20, pady=10, sticky="n")
        self.enterscore_entry_frame = ctk.CTkFrame(self.enterscore_frame, corner_radius=0, fg_color="transparent")
        self.enterscore_entry_frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")
        self.enterscore_entry = ctk.CTkEntry(self.enterscore_entry_frame, corner_radius=10)
        self.enterscore_entry.grid(row=0, column=0, padx=20, pady=10)
        self.enterscore_button = ctk.CTkButton(self.enterscore_entry_frame, corner_radius=10, width=100, height=50,
                                               text="Validate", font=ctk.CTkFont(size=20, weight="bold"))
        self.enterscore_button.grid(row=0, column=1, padx=20, pady=10)

=======
>>>>>>> e9478d8eeae222fc9274c8be905ef1a2afdfa195
        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.profiles_button.configure(fg_color=("gray75", "gray25") if name == "profiles" else "transparent")
<<<<<<< HEAD
        self.play_button.configure(fg_color=("gray75", "gray25") if name == "play" else "transparent")
=======
        self.newgame_button.configure(fg_color=("gray75", "gray25") if name == "newgame" else "transparent")
>>>>>>> e9478d8eeae222fc9274c8be905ef1a2afdfa195
        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "profiles":
            self.profiles_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.profiles_frame.grid_forget()
        if name == "play":
            self.play_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.play_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def profiles_button_event(self):
        self.select_frame_by_name("profiles")

    def play_button_event(self):
        self.select_frame_by_name("play")

    def createplayer_button(self, playername):
        if playername != "" and playername not in self.list_player:
            self.warning_label.grid_forget()
            self.list_player.append(playername)
            self.player_button[playername] = ctk.CTkButton(self.player_list_frame, text=playername,
                                                           font=ctk.CTkFont(size=20, weight="bold"),
                                                           fg_color=random_color(), corner_radius=10,
                                                           command=partial(self.selectplayer, playername))

            for player in self.player_button:
                self.player_button[player].grid_forget()
            i = 0
            row = 0
            for player in self.player_button:
                self.player_button[player].grid(row=row, column=i, padx=5, pady=10)
                i += 1
                if i == 4:
                    i = 0
                    row += 1
        if playername == "":
            self.warning_label.configure(text="Please enter a name")
            self.warning_label.grid(row=4, column=0, padx=20, pady=10, sticky="n")
        if playername in self.list_player:
            self.warning_label.configure(text="This name already exist")
            self.warning_label.grid(row=4, column=0, padx=20, pady=10, sticky="n")

    def selectplayer(self, playername):
        print(playername)
        for player in self.player_button:
            if player == playername and self.player_button[player].cget("border_width") == 0:
                self.player_button[player].configure(border_color="gray75", border_width=5)
                self.settings.playersofthisgame.append(playername)
            elif player == playername and self.player_button[player].cget("border_width") == 5:
                self.player_button[player].configure(border_width=0)
                self.settings.playersofthisgame.remove(playername)
        if len(self.settings.playersofthisgame) > 0:
            self.startgame_button.configure(state="normal")
        else:
            self.startgame_button.configure(state="disabled")

<<<<<<< HEAD
    def startgame(self):
        if self.numberofbowlingpins_frame_entry.get() != "":
            self.settings.numberofbowlingpins = int(self.numberofbowlingpins_frame_entry.get())
        if self.numberofrounds_frame_entry.get() != "":
            self.settings.numberofrounds = int(self.numberofrounds_frame_entry.get())
        print(self.settings.numberofbowlingpins)
        print(self.settings.numberofrounds)
        print(self.settings.playersofthisgame)
        self.settings_frame.grid_forget()
        self.playgame_frame.grid(row=0, column=0, sticky="ew")
        self.editplaygameframe()

    def editplaygameframe(self):
        self.headertab_frame.grid_columnconfigure(self.settings.numberofrounds + 1, weight=1)

        for rounds in range(self.settings.numberofrounds):
            self.round_frame = ctk.CTkFrame(self.headertab_frame, corner_radius=0, fg_color="transparent", width=25,
                                            border_width=1)
            self.round_frame.grid(row=0, column=rounds + 1, pady=10)
            self.round_label = ctk.CTkLabel(self.round_frame, text=str(rounds + 1),
                                            font=ctk.CTkFont(size=20, weight="bold"))
            self.round_label.grid(row=0, column=0, padx=20, pady=10)

        for player in range(len(self.settings.playersofthisgame)):
            self.playerscore_widgets[self.settings.playersofthisgame[player]] = PlayerInfoWidgets(
                self.settings.playersofthisgame[player], self.settings.numberofrounds, self.scoretab_frame)

            self.playerscore_widgets[self.settings.playersofthisgame[player]].playerscore_frame.grid(row=player + 1,
                                                                                                     column=0, padx=20,
                                                                                                     pady=10)
            self.playerscore_widgets[self.settings.playersofthisgame[player]].playerscore_frame.grid_columnconfigure(
                self.settings.numberofrounds + 2, weight=1)
        self.enterscore_label.configure(text="Enter score for " + self.settings.playersofthisgame[self.activeplayer])

    def enterscore(self):
        # if self.enterscore_entry.get() != "":
        #    self.totalscore_label.configure(text=self.enterscore_entry.get())
        #    self.activeround += 1
        #    self.enterscore_label.configure(
        #        text="Enter score for " + self.settings.playersofthisgame[self.activeplayer])
        #    self.enterscore_entry.delete(0, "end")
        return 0

=======
>>>>>>> e9478d8eeae222fc9274c8be905ef1a2afdfa195
    @staticmethod
    def change_appearance_mode_event(new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
