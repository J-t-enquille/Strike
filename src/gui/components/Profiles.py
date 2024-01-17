import os

import customtkinter as ctk
from functools import partial

from PIL import Image

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

        # Icons ----------------------------------------------------------------
        assets_path = os.path.join(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", ".."), "assets")
        self.trash_image = ctk.CTkImage(light_image=Image.open(os.path.join(assets_path, "trash.png")),
                                        dark_image=Image.open(os.path.join(assets_path, "trash_dark.png")),
                                        size=(26, 26))
        # ----------------------------------------------------------------------

        self.profiles_label = ctk.CTkLabel(self, text="Players list",
                                           font=ctk.CTkFont(size=38, weight="bold"))
        self.profiles_label.grid(row=1, column=0, padx=20, pady=10, sticky="new")

        self.players_list = ["Player 1", "Player 2", "Player 3", "Player 4"]

        self.players_frame = PlayersFrame(self, onClick=self.delete_player, players=self.players_list)
        self.players_frame.grid(row=player_frame_row, column=0, padx=20, pady=10)

        # Add player frame -----------------------------------------------------
        self.add_player_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent", height=50)
        self.add_player_frame.grid_columnconfigure(0, weight=2)
        self.add_player_frame.grid_columnconfigure(1, weight=2)
        self.add_player_frame.grid_columnconfigure(2, weight=0)
        self.add_player_frame.grid_columnconfigure(3, weight=1)
        self.add_player_frame.grid_columnconfigure(4, weight=0)
        self.add_player_frame.grid_rowconfigure(0, weight=1)
        self.add_player_frame.grid(row=4, column=0, sticky="sew")

        self.add_player_input = ctk.CTkEntry(self.add_player_frame, corner_radius=10, height=50,
                                             placeholder_text="Player name", font=ctk.CTkFont(size=18))
        self.add_player_input.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

        self.add_player_btn = ctk.CTkButton(self.add_player_frame, corner_radius=10,
                                            height=50,
                                            font=ctk.CTkFont(size=18, weight="bold"),
                                            text="New player",
                                            command=lambda: self.create_player_button(self.add_player_input.get()))
        self.add_player_btn.grid(row=0, column=2)

        self.trash_btn_active = False
        self.trash_btn = ctk.CTkButton(self.add_player_frame, corner_radius=10,
                                       border_spacing=10,
                                       width=40,
                                       text='',
                                       fg_color="transparent",
                                       hover_color='firebrick1',
                                       border_color=("grey50", "grey80"),
                                       image=self.trash_image,
                                       command=self.delete_player_button)
        self.trash_btn.grid(row=0, column=4, padx=10, sticky="e")
        # ----------------------------------------------------------------------

        self.warning_label = ctk.CTkLabel(self, text="",
                                          font=ctk.CTkFont(size=20, weight="bold", slant="italic"), text_color="red")

    # Create player button handler
    def create_player_button(self, playername):
        if playername == "":
            self.warning_label.configure(text="Please enter a name")
            self.warning_label.grid(row=3, column=0, pady=10, sticky="sew")
            return
        if playername in self.players_list:
            self.warning_label.configure(text="This name already exist")
            self.warning_label.grid(row=3, column=0, pady=10, sticky="sew")
            return
        self.warning_label.grid_forget()
        self.players_frame.destroy()
        self.players_list.append(playername)
        self.players_frame = PlayersFrame(self, onClick=self.delete_player, players=self.players_list)
        self.players_frame.grid(row=player_frame_row, column=0, pady=10)

    # Trash button handler
    def delete_player_button(self):
        self.trash_btn_active = not self.trash_btn_active
        self.trash_btn.configure(fg_color="firebrick1" if self.trash_btn_active else "transparent",
                                 border_width=2 if self.trash_btn_active else 0)

    # Delete player handler - if trash button is active
    def delete_player(self, playername):
        if not self.trash_btn_active:
            return

        self.players_frame.destroy()
        self.players_list.remove(playername)
        self.players_frame = PlayersFrame(self, onClick=self.delete_player, players=self.players_list)
        self.players_frame.grid(row=player_frame_row, column=0, pady=10)
