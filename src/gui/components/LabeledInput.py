import customtkinter as ctk


class LabeledInput(ctk.CTkFrame):

    def __init__(self, master, entry_width, inline=False, label=None, placeholder_text='', **kwargs):
        """
        LabeledInput is a custom widget that contains a label and an entry.
        :type master: ctk.CTkFrame
        :param master: ctk.CTkFrame
        :param entry_width: if inline not set, if the entry width is lower than 80, it will be inlined
        :param inline: bool
        :param label:
        :param placeholder_text:
        :param kwargs:
        """
        if entry_width <= 80 or inline:
            self.entry_row = 0
            self.entry_column = 1
        else:
            self.entry_row = 1
            self.entry_column = 0

        super().__init__(master, **kwargs)

        self.configure(corner_radius=0, fg_color="transparent")

        if label is not None:
            self.label = ctk.CTkLabel(self, text=label, font=ctk.CTkFont(size=18, weight="bold"))
            self.label.grid(row=0, column=0, pady=10, padx=10, sticky="sw")

        self.entry = ctk.CTkEntry(self, corner_radius=10, height=50, placeholder_text=placeholder_text,
                                  font=ctk.CTkFont(size=16), width=entry_width)
        self.entry.grid(row=self.entry_row, column=self.entry_column, sticky="w")

    def get(self):
        return self.entry.get()
