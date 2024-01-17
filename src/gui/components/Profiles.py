import customtkinter as ctk
from functools import partial
from src.gui.components.PlayersFrame import PlayersFrame


class ToplevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="ToplevelWindow")
        self.label.pack(padx=20, pady=20)


player_frame_row = 2


class Profiles(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(corner_radius=0, fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(player_frame_row, weight=1)

        self.profiles_label = ctk.CTkLabel(self, text="Players list",
                                           font=ctk.CTkFont(size=38, weight="bold"))
        self.profiles_label.grid(row=1, column=0, padx=20, pady=10, sticky="new")

        self.players_list = ["Player 1", "Player 2", "Player 3", "Player 4"]

        self.players_frame = PlayersFrame(self, onClick=print, players=self.players_list)
        self.players_frame.grid(row=player_frame_row, column=0, padx=20, pady=10)

        # Add player frame -----------------------------------------------------
        self.add_player_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.add_player_frame.grid(row=4, column=0, padx=20, pady=10, sticky="n")

        self.add_player_input = ctk.CTkEntry(self.add_player_frame, corner_radius=10, height=50, width=300)
        self.add_player_input.grid(row=0, column=0, padx=20, pady=10)

        self.add_player_btn = ctk.CTkButton(self.add_player_frame, corner_radius=10, height=50,
                                            font=ctk.CTkFont(size=18, weight="bold"),
                                            text="New player",
                                            command=lambda: self.createplayer_button(self.add_player_input.get()))
        self.add_player_btn.grid(row=0, column=1, padx=20, pady=10)
        # ----------------------------------------------------------------------

        self.warning_label = ctk.CTkLabel(self, text="",
                                          font=ctk.CTkFont(size=20, weight="bold", slant="italic"), text_color="red")

    def createplayer_button(self, playername):
        if playername == "":
            self.warning_label.configure(text="Please enter a name")
            self.warning_label.grid(row=3, column=0, padx=20, pady=10, sticky="sew")
            return
        if playername in self.players_list:
            self.warning_label.configure(text="This name already exist")
            self.warning_label.grid(row=3, column=0, padx=20, pady=10, sticky="sew")
            return
        self.warning_label.grid_forget()
        self.players_frame.destroy()
        self.players_list.append(playername)
        self.players_frame = PlayersFrame(self, onClick=print, players=self.players_list)
        self.players_frame.grid(row=player_frame_row, column=0, padx=20, pady=10)
