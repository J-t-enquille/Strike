import os
from PIL import Image
import customtkinter as ctk
import random
from functools import partial

from src.gui.components.GameSettings import GameSettings
from src.gui.components.PlayersFrame import PlayersFrame
from src.gui.components.Profiles import Profiles
from src.Partie import Partie
from src.Score import Score
from src.Parser import Parser


def random_color():
    red = random.randint(30, 225)
    green = random.randint(30, 225)
    blue = random.randint(30, 225)

    color_hex = "#{:02X}{:02X}{:02X}".format(red, green, blue)

    return color_hex


class PlayerInfoWidgets:
    def __init__(self, playername, rounds, scoretab_frame):
        self.playerscore_frame = ctk.CTkFrame(scoretab_frame, corner_radius=0, fg_color="transparent", border_width=2)
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
        self.firsttrial_label = ctk.CTkLabel(self.firsttrial_frame, text="0",
                                             font=ctk.CTkFont(size=20, weight="bold"))
        self.secondtrial_frame = ctk.CTkFrame(self.trials_frame, corner_radius=0, fg_color="transparent",
                                              border_width=2)
        self.secondtrial_label = ctk.CTkLabel(self.secondtrial_frame, text="0",
                                              font=ctk.CTkFont(size=20, weight="bold"))
        if activeround == rounds - 1:
            self.thirdtrial_frame = ctk.CTkFrame(self.trials_frame, corner_radius=0, fg_color="transparent",
                                                 border_width=2)
            self.thirdtrial_label = ctk.CTkLabel(self.thirdtrial_frame, text="0",
                                                 font=ctk.CTkFont(size=20, weight="bold"))
        self.sumscoretrial_frame = ctk.CTkFrame(self.scorecase_frame, corner_radius=0, fg_color="transparent")
        self.sumscoretrial_label = ctk.CTkLabel(self.sumscoretrial_frame, text="0",
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
        self.play_image = ctk.CTkImage(light_image=Image.open(os.path.join(assets_path, "newgame.png")),
                                       dark_image=Image.open(os.path.join(assets_path, "newgame_dark.png")),
                                       size=(26, 26))
        self.newgame_image = ctk.CTkImage(light_image=Image.open(os.path.join(assets_path, "newgame.png")),
                                          dark_image=Image.open(os.path.join(assets_path, "newgame_dark.png")),
                                          size=(26, 26))
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

        self.play_button = ctk.CTkButton(self.sidebar_frame, corner_radius=0, height=40,
                                         border_spacing=10, text="Play",
                                         font=ctk.CTkFont(size=18),
                                         fg_color="transparent", text_color=("gray10", "gray90"),
                                         hover_color=("gray70", "gray30"),
                                         image=self.play_image, anchor="w",
                                         command=self.play_button_event)
        self.play_button.grid(row=3, column=0, sticky="ew")


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

        class SettingsGame:
            def __init__(self, numberofbowlingpins, numberofrounds):
                self.numberofbowlingpins = numberofbowlingpins
                self.numberofrounds = numberofrounds
                self.playersofthisgame = []


        self.partie = Partie()

        # create settings frame of play frame
        self.game_settings = GameSettings(self.play_frame, self.partie, start_game=self.start_game)
        self.game_settings.grid(row=0, column=0, sticky="nsew")

        # create playgame frame of play frame
        self.activeplayer = ""
        self.activetrial = 1
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
                                             text="Enter first score for ", font=ctk.CTkFont(size=20, weight="bold"))
        self.enterscore_label.grid(row=0, column=0, padx=20, pady=10, sticky="n")
        self.enterscore_entry_frame = ctk.CTkFrame(self.enterscore_frame, corner_radius=0, fg_color="transparent")
        self.enterscore_entry_frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")
        self.enterscore_entry = ctk.CTkEntry(self.enterscore_entry_frame, corner_radius=10)
        self.enterscore_entry.grid(row=0, column=0, padx=20, pady=10)
        self.enterscore_button = ctk.CTkButton(self.enterscore_entry_frame, corner_radius=10, width=100, height=50,
                                               text="Validate", font=ctk.CTkFont(size=20, weight="bold"),
                                               command=self.enterscore)
        self.enterscore_button.grid(row=0, column=1, padx=20, pady=10)
        self.enterscore_warning_label = ctk.CTkLabel(self.enterscore_entry_frame, text="",
                                                     font=ctk.CTkFont(size=20, weight="bold", slant="italic"),
                                                     text_color="red")
        self.enterscore_warning_label.grid(row=1, column=0, padx=20, pady=10, sticky="n")

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.profiles_button.configure(fg_color=("gray75", "gray25") if name == "profiles" else "transparent")
        self.play_button.configure(fg_color=("gray75", "gray25") if name == "play" else "transparent")
        # self.newgame_button.configure(fg_color=("gray75", "gray25") if name == "newgame" else "transparent")
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

    def start_game(self):
        self.indiceplayer = 0
        self.activeplayer = list(self.partie.scores)[self.indiceplayer]
        if self.game_settings.get_pins() != 0:
            self.partie.nombre_quilles = self.game_settings.get_pins()
        if self.game_settings.get_rounds() != 0:
            self.partie.nombre_tours = self.game_settings.get_rounds()
        print(self.partie.nombre_quilles)
        print(self.partie.nombre_tours)
        print(list(self.partie.scores))
        self.game_settings.destroy()
        self.playgame_frame.grid(row=0, column=0, sticky="ew")
        self.buildscoretab_frame()
        self.playerscore_widgets[self.activeplayer].playerscore_label.configure(
            text_color="#1f6aa5")
        self.playerscore_widgets[self.activeplayer].scorecase_frame_tab[
            self.activeround - 1].firsttrial_frame.configure(fg_color="#1f6aa5")

    def buildscoretab_frame(self):
        self.headertab_frame.grid_columnconfigure(self.partie.nombre_tours + 1, weight=1)

        for rounds in range(self.partie.nombre_tours):
            self.round_frame = ctk.CTkFrame(self.headertab_frame, corner_radius=0, fg_color="transparent", width=25,
                                            border_width=1)
            self.round_frame.grid(row=0, column=rounds + 1, pady=10)
            self.round_label = ctk.CTkLabel(self.round_frame, text=str(rounds + 1),
                                            font=ctk.CTkFont(size=20, weight="bold"))
            self.round_label.grid(row=0, column=0, padx=20, pady=10)
        cpt = 0
        for player in self.partie.scores:
            self.playerscore_widgets[player] = PlayerInfoWidgets(player, self.partie.nombre_tours, self.scoretab_frame)

            self.playerscore_widgets[player].playerscore_frame.grid(row=cpt + 1,
                                                                                                     column=0, padx=20,
                                                                                                     pady=10)
            self.playerscore_widgets[player].playerscore_frame.grid_columnconfigure(
                self.partie.nombre_tours + 2, weight=1)
            cpt += 1
        self.enterscore_label.configure(
            text="Enter a first score for " + self.activeplayer)

    def enterscore(self):
        trial = ""
        numberofpins = self.partie.nombre_quilles
        if self.enterscore_entry.get().isdigit() and int(
                self.enterscore_entry.get()) <= self.partie.nombre_quilles:
            self.enterscore_warning_label.configure(text="")
            if self.enterscore_entry.get() != "":
                if self.activetrial == 1:
                    self.playerscore_widgets[self.activeplayer].scorecase_frame_tab[
                        self.activeround - 1].firsttrial_label.configure(text=self.enterscore_entry.get())
                    self.playerscore_widgets[self.activeplayer].scorecase_frame_tab[
                        self.activeround - 1].sumscoretrial_label.configure(text=self.enterscore_entry.get())
                    sumscorerounds = int(self.playerscore_widgets[self.activeplayer].totalscore_label.cget(
                        "text")) + int(self.playerscore_widgets[self.activeplayer].scorecase_frame_tab[
                                           self.activeround - 1].sumscoretrial_label.cget("text"))
                    self.playerscore_widgets[
                        self.activeplayer].totalscore_label.configure(
                        text=sumscorerounds)

                    self.playerscore_widgets[self.activeplayer].scorecase_frame_tab[
                        self.activeround - 1].firsttrial_frame.configure(fg_color="transparent")

                    if int(self.enterscore_entry.get()) == self.partie.nombre_quilles:
                        if self.activeplayer == list(self.partie.scores)[len(self.partie.scores) - 1]:
                            self.indiceplayer = 0
                            self.activeplayer = list(self.partie.scores)[self.indiceplayer]
                            self.activeround += 1
                        else:
                            self.indiceplayer += 1
                            self.activeplayer = list(self.partie.scores)[self.indiceplayer]
                        self.activetrial = 1
                        self.enterscore_label.configure(
                            text="Enter first score for " + self.activeplayer)
                        self.playerscore_widgets[
                            self.activeplayer].playerscore_label.configure(
                            text_color="#1f6aa5")
                        self.playerscore_widgets[
                            self.activeplayer].scorecase_frame_tab[
                            self.activeround - 1].firsttrial_frame.configure(fg_color="#1f6aa5")
                    else:
                        self.activetrial += 1

                        self.playerscore_widgets[
                            self.activeplayer].scorecase_frame_tab[
                            self.activeround - 1].secondtrial_frame.configure(fg_color="#1f6aa5")
                        self.enterscore_label.configure(
                            text="Enter second score for " + self.activeplayer)
                    self.enterscore_entry.delete(0, "end")
                elif self.activetrial == 2:
                    self.playerscore_widgets[self.activeplayer].scorecase_frame_tab[
                        self.activeround - 1].secondtrial_label.configure(text=self.enterscore_entry.get())
                    sumtrials = int(
                        self.playerscore_widgets[
                            self.activeplayer].scorecase_frame_tab[
                            self.activeround - 1].firsttrial_label.cget("text")) + int(
                        self.playerscore_widgets[
                            self.activeplayer].scorecase_frame_tab[
                            self.activeround - 1].secondtrial_label.cget("text"))
                    self.playerscore_widgets[self.activeplayer].scorecase_frame_tab[
                        self.activeround - 1].sumscoretrial_label.configure(text=str(sumtrials))
                    sumscorerounds = int(self.playerscore_widgets[
                                             self.activeplayer].totalscore_label.cget(
                        "text")) + int(self.playerscore_widgets[
                                           self.activeplayer].scorecase_frame_tab[
                                           self.activeround - 1].sumscoretrial_label.cget("text"))
                    self.playerscore_widgets[
                        self.activeplayer].totalscore_label.configure(
                        text=sumscorerounds)
                    self.activetrial = 1
                    self.playerscore_widgets[
                        self.activeplayer].playerscore_label.configure(
                        text_color="gray75")
                    self.playerscore_widgets[self.activeplayer].scorecase_frame_tab[
                        self.activeround - 1].secondtrial_frame.configure(fg_color="transparent")

                    if self.activeplayer == list(self.partie.scores)[len(self.partie.scores) - 1]:
                        self.indiceplayer = 0
                        self.activeplayer = list(self.partie.scores)[self.indiceplayer]
                        self.activeround += 1

                    else:
                        self.indiceplayer += 1
                        self.activeplayer = list(self.partie.scores)[self.indiceplayer]
                    self.playerscore_widgets[
                        self.activeplayer].playerscore_label.configure(
                        text_color="#1f6aa5")
                    self.playerscore_widgets[self.activeplayer].scorecase_frame_tab[
                        self.activeround - 1].firsttrial_frame.configure(fg_color="#1f6aa5")

                    self.enterscore_label.configure(
                        text="Enter first score for " + self.activeplayer)
                    self.enterscore_entry.delete(0, "end")

                self.enterscore_entry.delete(0, "end")

        elif not self.enterscore_entry.get().isdigit():
            self.enterscore_entry.delete(0, "end")
            self.enterscore_warning_label.configure(text="Please enter a number")
        elif int(self.enterscore_entry.get()) > self.partie.nombre_quilles:
            self.enterscore_entry.delete(0, "end")
            self.enterscore_warning_label.configure(
                text="Please enter a number between 0 and " + str(self.partie.nombre_quilles))

    @staticmethod
    def change_appearance_mode_event(new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
