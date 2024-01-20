from functools import partial

import customtkinter as ctk


class FormInput(ctk.CTkFrame):
    """
    FormInput is a custom widget that contains an entry and a button.
    """

    def __init__(self, master, onSubmit,
                 placeholder_text='',
                 btn_text='Submit',
                 warning_text='',
                 warning_callback=None,
                 allow_empty=False,
                 reset_on_submit=False,
                 number_only=False,
                 **kwargs):
        """
        :type master: ctk.CTkFrame
        :param master: parent
        :param onSubmit: callback function that takes the entry value as parameter
        :param placeholder_text: a placeholder text for the entry
        :param btn_text:
        :param warning_text:
        :param warning_callback: callback function that returns a boolean (true if the warning should be displayed)
        :param allow_empty: if false, the entry can't be empty
        :param reset_on_submit: if true, the entry will be cleared after the submit
        :param kwargs:
        """
        self.onSubmit = onSubmit
        self.warning_callback = warning_callback
        self.warning_text = warning_text
        self.allow_empty = allow_empty
        self.reset_on_submit = reset_on_submit
        self.number_only = number_only

        super().__init__(master, **kwargs)

        self.configure(corner_radius=0, fg_color="transparent", height=50)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=0)
        self.grid_columnconfigure(3, weight=1)

        self.entry = ctk.CTkEntry(self, corner_radius=10, height=50,
                                  placeholder_text=placeholder_text, font=ctk.CTkFont(size=18))
        self.entry.grid(row=1, column=1, sticky="ew", padx=10, pady=10)

        self.add_player_btn = ctk.CTkButton(self, corner_radius=10,
                                            height=50,
                                            font=ctk.CTkFont(size=18, weight="bold"),
                                            text=btn_text,
                                            command=self.submit)
        self.add_player_btn.grid(row=1, column=2)

        # Bind enter key to add player button
        self.entry.bind("<Return>", lambda event: self.add_player_btn.invoke())
        # Bind focus in (mouse l-click) to clear warning label
        self.entry.bind("<Button-1>", lambda event: self.warning_label.configure(text=""))

        self.warning_label = ctk.CTkLabel(self, text="",
                                          font=ctk.CTkFont(size=20, weight="bold", slant="italic"), text_color="red")
        self.warning_label.grid(row=0, column=1, pady=10, sticky="sew")

    def submit(self):
        if not self.allow_empty and self.entry.get() == "":
            self.warning_label.configure(text="Empty entry are not allowed !")
            self.warning_label.grid(row=0, column=1, pady=10, sticky="sew")
            return

        if self.number_only and not self.entry.get().isdigit():
            self.warning_label.configure(text="Only numbers are allowed !")
            self.warning_label.grid(row=0, column=1, pady=10, sticky="sew")
            self.entry.delete(0, "end")
            return

        if self.warning_callback is not None and self.warning_callback(
                self.entry.get() if not self.number_only else int(self.entry.get())):
            self.warning_label.configure(text=self.warning_text)
            self.warning_label.grid(row=0, column=1, pady=10, sticky="sew")
            self.entry.delete(0, "end")
            return

        self.warning_label.configure(text="")
        self.onSubmit(self.entry.get() if not self.number_only else int(self.entry.get()))
        if self.reset_on_submit:
            self.entry.delete(0, "end")
