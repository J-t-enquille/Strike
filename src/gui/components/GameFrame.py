import customtkinter as ctk

from src.gui.components.FormInput import FormInput


class GameFrame(ctk.CTkFrame):
    def __init__(self, master, partie, reset_command, **kwargs):
        self.partie = partie
        self.stategame = StateGame(0, "", 0, 1, self.partie.nombre_quilles)

        super().__init__(master, **kwargs)

        self.configure(corner_radius=0, fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        self.scoretab_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.scoretab_frame.grid(row=0, column=0, padx=20, pady=10)
        self.scoretab_frame.grid_rowconfigure(0, weight=1)
        self.scoretab_frame.grid_columnconfigure(1, weight=1)
        self.headertab_frame = ctk.CTkFrame(self.scoretab_frame, corner_radius=0, fg_color="transparent")
        self.headertab_frame.grid(row=0, column=0, padx=20, pady=10)
        self.playerscore_widgets = {}

        self.enterscore_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.enterscore_frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")
        self.remainingpins_label = ctk.CTkLabel(self.enterscore_frame, text="Remaining pins: " + str(self.stategame.remainingpins), font=ctk.CTkFont(size=20, weight="bold"))
        self.remainingpins_label.grid(row=0, column=0, padx=20, pady=10, sticky="n")
        self.enterscore_label = ctk.CTkLabel(self.enterscore_frame,
                                             text="Enter first score for ", font=ctk.CTkFont(size=20, weight="bold"))
        self.enterscore_label.grid(row=1, column=0, padx=20, pady=10, sticky="n")

        self.score_input = FormInput(self.enterscore_frame, onSubmit=self.enterscore,
                                     placeholder_text="Score", btn_text="Validate",
                                     warning_callback=self.warning,
                                     warning_text="Please enter a number between 0 and " + str(
                                         self.stategame.remainingpins),
                                     allow_empty=False, reset_on_submit=True, number_only=True)
        self.score_input.grid(row=2, column=0, padx=20, pady=10, sticky="n")

        self.msg_endofgame_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.enofgame_label = ctk.CTkLabel(self.msg_endofgame_frame, text="End of game",
                                           font=ctk.CTkFont(size=20, weight="bold"))
        self.enofgame_label.grid(row=0, column=0, padx=20, pady=10, sticky="n")
        self.congrats_label = ctk.CTkLabel(self.msg_endofgame_frame, text="",
                                           font=ctk.CTkFont(size=25, weight="bold"), text_color="#1f6aa5")
        self.congrats_label.grid(row=1, column=0, padx=20, pady=10, sticky="n")
        self.reset_label = ctk.CTkLabel(self.msg_endofgame_frame, text="Reset to play again",
                                        font=ctk.CTkFont(size=20, weight="bold"))
        self.reset_label.grid(row=2, column=0, padx=20, pady=10, sticky="n")
        self.back_btn = ctk.CTkButton(self, corner_radius=10, text="Reset", font=ctk.CTkFont(size=18, weight="bold"),
                                      command=reset_command)
        self.back_btn.grid(row=2, column=0, padx=20, pady=10, sticky="n")

        self.stategame.activeplayer = list(self.partie.scores)[self.stategame.iplayer]
        self.buildscoretab_frame()
        self.playerscore_widgets[self.stategame.activeplayer].playerscore_label.configure(
            text_color="#1f6aa5")
        self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
            self.stategame.activeround].firsttrial_frame.configure(fg_color="#1f6aa5")

    def buildscoretab_frame(self):
        """
        Build the scoretab_frame with the game settings (number of rounds, number of pins) and the players
        """
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
            text="Enter a first score for " + self.stategame.activeplayer)

    def enterscore(self, score):
        """
        Enter a score for a player and update the scoretab_frame
        :param score: int
        """
        if score <= self.stategame.remainingpins:
            if score != "":
                self.stategame.remainingpins = self.stategame.remainingpins - score
                self.score_input.set_warning_text("Please enter a number between 0 and " + str(
                                         self.stategame.remainingpins))
                if self.stategame.activetrial == 1:
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].firsttrial_label.configure(text=score)
                elif self.stategame.activetrial == 2:
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].secondtrial_label.configure(text=score)
                elif self.stategame.activetrial == 3:
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].thirdtrial_label.configure(text=score)
                self.partie.addScore(self.stategame.activeplayer, self.stategame.activeround, int(
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].firsttrial_label.cget("text")), int(
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].secondtrial_label.cget("text")), int(
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].thirdtrial_label.cget(
                        "text")) if self.stategame.activetrial == 3 else 0)

                if self.stategame.remainingpins != 0:
                    allscore_currentplayer = next(
                        (item for item in self.partie.displayScores() if item["player"] == self.stategame.activeplayer),
                        None)
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].sumscoretrial_label.configure(
                        text=allscore_currentplayer["tableau"][self.stategame.activeround])
                    self.playerscore_widgets[self.stategame.activeplayer].totalscore_label.configure(
                        text=allscore_currentplayer["total_score"])

                self.whoplaynext()
                self.remainingpins_label.configure(text="Remaining pins: " + str(self.stategame.remainingpins))

    def warning(self, score):
        return score > self.stategame.remainingpins

    def whoplaynext(self):
        """
        determine who is the next player and the next trial
        Display the next player and the next trial
        """
        # trial = 2 or strike or spare
        if self.stategame.activetrial == 2 or self.stategame.remainingpins == 0:
            # last round
            if self.stategame.activeround == self.partie.nombre_tours - 1:
                # strike for last round
                if self.stategame.activetrial == 1 and self.stategame.remainingpins == 0:
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].firsttrial_frame.configure(fg_color="transparent")
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].secondtrial_frame.configure(fg_color="#1f6aa5")
                    self.stategame.thirdtrial = True
                    self.stategame.activetrial = 2
                    self.stategame.remainingpins = self.partie.nombre_quilles
                    self.enterscore_label.configure(text="Enter second score for " + self.stategame.activeplayer)
                # spare for last round
                elif self.stategame.activetrial == 2 and self.stategame.remainingpins == 0:
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].secondtrial_frame.configure(fg_color="transparent")
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].thirdtrial_frame.configure(fg_color="#1f6aa5")
                    self.stategame.thirdtrial = True
                    self.stategame.activetrial = 3
                    self.stategame.remainingpins = self.partie.nombre_quilles
                    self.enterscore_label.configure(text="Enter third score for " + self.stategame.activeplayer)
                elif self.stategame.thirdtrial and self.stategame.activetrial == 2:
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].secondtrial_frame.configure(fg_color="transparent")
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].thirdtrial_frame.configure(fg_color="#1f6aa5")
                    self.stategame.thirdtrial = False
                    self.stategame.activetrial = 3
                    self.enterscore_label.configure(text="Enter third score for " + self.stategame.activeplayer)
                elif self.stategame.activetrial == 3:
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].thirdtrial_frame.configure(fg_color="transparent")
                    self.playerscore_widgets[self.stategame.activeplayer].playerscore_label.configure(
                        text_color="gray75")
                    allscore_currentplayer = next(
                        (item for item in self.partie.displayScores() if
                         item["player"] == self.stategame.activeplayer),
                        None)
                    for round in range(self.stategame.activeround+1):
                        self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                            round].sumscoretrial_label.configure(
                            text=allscore_currentplayer["tableau"][round])
                    if not self.endofgame():
                        self.stategame.activetrial = 1
                        self.stategame.remainingpins = self.partie.nombre_quilles
                        self.stategame.iplayer += 1
                        self.stategame.thirdtrial = False
                        # last player
                        if self.stategame.iplayer == len(self.partie.scores):
                            self.stategame.iplayer = 0
                            self.stategame.activeround += 1
                        self.stategame.activeplayer = list(self.partie.scores)[self.stategame.iplayer]
                        self.playerscore_widgets[self.stategame.activeplayer].playerscore_label.configure(
                            text_color="#1f6aa5")
                        self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                            self.stategame.activeround].firsttrial_frame.configure(fg_color="#1f6aa5")
                        self.enterscore_label.configure(text="Enter first score for " + self.stategame.activeplayer)
                else:
                    self.stategame.activetrial = 1
                    self.stategame.remainingpins = self.partie.nombre_quilles
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].firsttrial_frame.configure(fg_color="transparent")
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        self.stategame.activeround].secondtrial_frame.configure(fg_color="transparent")
                    self.playerscore_widgets[self.stategame.activeplayer].playerscore_label.configure(
                        text_color="gray75")
                    allscore_currentplayer = next(
                        (item for item in self.partie.displayScores() if
                         item["player"] == self.stategame.activeplayer),
                        None)
                    for round in range(self.stategame.activeround):
                        self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                            round].sumscoretrial_label.configure(
                            text=allscore_currentplayer["tableau"][round])
                    if not self.endofgame():
                        self.stategame.iplayer += 1
                        self.stategame.thirdtrial = False
                        # last player
                        if self.stategame.iplayer == len(self.partie.scores):
                            self.stategame.iplayer = 0
                            self.stategame.activeround += 1
                        self.stategame.activeplayer = list(self.partie.scores)[self.stategame.iplayer]
                        self.playerscore_widgets[self.stategame.activeplayer].playerscore_label.configure(
                            text_color="#1f6aa5")
                        self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                            self.stategame.activeround].firsttrial_frame.configure(fg_color="#1f6aa5")
                        self.enterscore_label.configure(text="Enter first score for " + self.stategame.activeplayer)
            # not last round
            else:
                self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                    self.stategame.activeround].firsttrial_frame.configure(fg_color="transparent")
                self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                    self.stategame.activeround].secondtrial_frame.configure(fg_color="transparent")
                self.playerscore_widgets[self.stategame.activeplayer].playerscore_label.configure(text_color="gray75")
                self.stategame.activetrial = 1
                self.stategame.remainingpins = self.partie.nombre_quilles
                allscore_currentplayer = next(
                    (item for item in self.partie.displayScores() if
                     item["player"] == self.stategame.activeplayer),
                    None)
                for round in range(self.stategame.activeround):
                    self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                        round].sumscoretrial_label.configure(
                        text=allscore_currentplayer["tableau"][round])
                self.stategame.iplayer += 1
                # last player
                if self.stategame.iplayer == len(self.partie.scores):
                    self.stategame.iplayer = 0
                    self.stategame.activeround += 1
                self.stategame.activeplayer = list(self.partie.scores)[self.stategame.iplayer]
                self.playerscore_widgets[self.stategame.activeplayer].playerscore_label.configure(text_color="#1f6aa5")
                self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                    self.stategame.activeround].firsttrial_frame.configure(fg_color="#1f6aa5")
                self.enterscore_label.configure(text="Enter first score for " + self.stategame.activeplayer)
        # trial = 1
        elif self.stategame.activetrial == 1:
            self.stategame.activetrial = 2
            self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                self.stategame.activeround].firsttrial_frame.configure(fg_color="transparent")
            self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                self.stategame.activeround].secondtrial_frame.configure(fg_color="#1f6aa5")
            self.enterscore_label.configure(text="Enter second score for " + self.stategame.activeplayer)
        elif self.stategame.activetrial == 3:
            self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                self.stategame.activeround].thirdtrial_frame.configure(fg_color="transparent")
            self.playerscore_widgets[self.stategame.activeplayer].playerscore_label.configure(text_color="gray75")
            allscore_currentplayer = next(
                (item for item in self.partie.displayScores() if
                 item["player"] == self.stategame.activeplayer),
                None)
            for round in range(self.stategame.activeround):
                self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                    round].sumscoretrial_label.configure(
                    text=allscore_currentplayer["tableau"][round])
            if not self.endofgame():
                self.stategame.activetrial = 1
                self.stategame.remainingpins = self.partie.nombre_quilles
                self.stategame.iplayer += 1
                self.stategame.thirdtrial = False

                # last player
                if self.stategame.iplayer == len(self.partie.scores):
                    self.stategame.iplayer = 0
                    self.stategame.activeround += 1
                self.stategame.activeplayer = list(self.partie.scores)[self.stategame.iplayer]
                self.playerscore_widgets[self.stategame.activeplayer].playerscore_label.configure(text_color="#1f6aa5")
                self.playerscore_widgets[self.stategame.activeplayer].scorecase_frame_tab[
                    self.stategame.activeround].firsttrial_frame.configure(fg_color="#1f6aa5")
                self.enterscore_label.configure(text="Enter first score for " + self.stategame.activeplayer)

    def endofgame(self):
        """
        Display the end of the game
        :return: True if the game is over
        """
        if self.stategame.activeround == self.partie.nombre_tours - 1 and self.stategame.iplayer == len(
                self.partie.scores) - 1:

            for player in self.partie.scores:
                allscore_currentplayer = next(
                    (item for item in self.partie.displayScores() if
                     item["player"] == player),
                    None)
                for round in range(self.partie.nombre_tours):
                    self.playerscore_widgets[player].scorecase_frame_tab[
                        round].sumscoretrial_label.configure(
                        text=allscore_currentplayer["tableau"][round])
                self.playerscore_widgets[player].totalscore_label.configure(text=allscore_currentplayer["total_score"])
            self.enterscore_frame.grid_forget()
            self.msg_endofgame_frame.grid(row=1, column=0, padx=20, pady=10, sticky="n")
            if len(self.partie.scores) > 1:
                winner = list(self.partie.scores)[0]
                for player in self.partie.scores:
                    if self.partie.scores[player].scoreTotal() > self.partie.scores[winner].scoreTotal():
                        winner = player
                self.congrats_label.configure(text="Congrats to " + winner + " !")
            return True


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


class StateGame:
    def __init__(self, iplayer, activeplayer, activeround, activetrial, remainingpins):
        self.iplayer = iplayer
        self.activeplayer = activeplayer
        self.activeround = activeround
        self.activetrial = activetrial
        self.remainingpins = remainingpins
        self.thirdtrial = False
