import customtkinter as ctk
import random
from functools import partial


class PlayersFrame(ctk.CTkFrame):
    def __init__(self, master, onClick, players, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(corner_radius=0, fg_color="transparent")

        self.player_button = {}
        i = 0
        row = 0
        for player in players:
            color = random_color()
            self.player_button[player] = ctk.CTkButton(self, text=player,
                                                       font=ctk.CTkFont(size=20, weight="bold"), fg_color=color,
                                                       corner_radius=10, command=partial(onClick, player))
        for player in self.player_button:
            self.player_button[player].grid(row=row, column=i, padx=5, pady=10)
            i += 1
            if i == 4:
                i = 0
                row += 1


def random_color():
    red = random.randint(30, 225)
    green = random.randint(30, 225)
    blue = random.randint(30, 225)

    color_hex = "#{:02X}{:02X}{:02X}".format(red, green, blue)

    return color_hex
