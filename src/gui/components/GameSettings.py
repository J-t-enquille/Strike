import customtkinter as ctk

from src.Player import Player
from src.gui.components.FormInput import FormInput
from src.gui.components.LabeledInput import LabeledInput
from src.gui.components.PlayersFrame import PlayersFrame
from src.Parser import Parser
from src.Partie import Partie


class GameSettings(ctk.CTkFrame):
    def __init__(self, master, partie, start_game, **kwargs):

        self.partie = partie

        super().__init__(master, **kwargs)

        # Configure the frame
        self.configure(corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Players frame ---------------------------------------------------------
        self.add_player_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.add_player_frame.grid_rowconfigure(1, weight=1)
        self.add_player_frame.grid(row=0, column=0, pady=10, sticky="ns")

        self.add_player_label = ctk.CTkLabel(self.add_player_frame, text="Select players for the game",
                                             font=ctk.CTkFont(size=34, weight="bold"))
        self.add_player_label.grid(row=0, column=0, padx=20, pady=10, sticky="s")

        self.parser = Parser()
        self.parser.getPlayers()

        self.players_frame = PlayersFrame(self.add_player_frame, onClick=self.select_player, players=self.parser.player)
        self.players_frame.grid(row=1, column=0)

        self.add_player_form = FormInput(self.add_player_frame,
                                         onSubmit=self.add_player_button,
                                         placeholder_text="Player name", btn_text="Add player",
                                         warning_callback=self.warning,
                                         warning_text="This player already exist !",
                                         allow_empty=False,
                                         reset_on_submit=True)
        self.add_player_form.grid(row=2, column=0, sticky="sew")
        # ----------------------------------------------------------------------

        # Game config frame -----------------------------------------------------
        self.game_config_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.game_config_frame.grid_columnconfigure(0, weight=1)
        self.game_config_frame.grid_columnconfigure(1, weight=1)
        self.game_config_frame.grid(row=1, column=0, padx=10, pady=20, sticky="sew")

        self.pins_input = LabeledInput(self.game_config_frame, label="Number of bowling pins :",
                                       placeholder_text=partie.nombre_quilles,
                                       entry_width=80)
        self.pins_input.grid(row=0, column=0, padx=50, sticky="e")

        self.rounds_input = LabeledInput(self.game_config_frame, label="Number of rounds :",
                                         placeholder_text=partie.nombre_tours,
                                         entry_width=80)
        self.rounds_input.grid(row=0, column=1, padx=50, sticky="w")
        # ----------------------------------------------------------------------

        # Bottom frame ----------------------------------------------------------

        self.bottom_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid(row=3, column=0, padx=20, pady=10, sticky="sew")
        self.start_game_button = ctk.CTkButton(self.bottom_frame, corner_radius=10, height=60, width=120,
                                               text="Start", font=ctk.CTkFont(size=20, weight="bold"),
                                               command=start_game, state="disabled")
        self.start_game_button.grid(row=0, column=0, sticky='e')
        # ----------------------------------------------------------------------

    # add player button handler
    def add_player_button(self, playername):
        self.players_frame.destroy()
        self.parser.addPlayer(playername)
        self.players_frame = PlayersFrame(self.add_player_frame, onClick=self.select_player, players=self.parser.player)
        for player in list(self.partie.scores):
            self.players_frame.get_player_button(player).configure(border_width=5, border_color="gray75")
        self.players_frame.grid(row=1, column=0, sticky='ew')

    def select_player(self, playername):
        if playername not in list(self.partie.scores):
            self.players_frame.get_player_button(playername).configure(border_width=5, border_color="gray75")
            self.partie.addPlayer(Player(playername))
        else:
            self.players_frame.get_player_button(playername).configure(border_width=0)
            self.partie.scores.pop(playername)

        if len(self.partie.scores) > 0:
            self.start_game_button.configure(state="normal")
        else:
            self.start_game_button.configure(state="disabled")

    def warning(self, playername):
        player_name_list = []
        for player in self.parser.player:
            player_name_list.append(player.get_name())
        return playername in player_name_list

    def get_pins(self):
        if self.pins_input.get() == "":
            return self.partie.nombre_quilles
        return int(self.pins_input.get())

    def get_rounds(self):
        if self.rounds_input.get() == "":
            return self.partie.nombre_tours
        return int(self.rounds_input.get())
