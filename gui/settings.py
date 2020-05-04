import tkinter as tk
import tkinter.ttk as ttk
from gui.styles.Custom_Button import Round_Button
from gui.styles.btn_styles import btn_small_style
from gui.setup_loc import lang_init

# Settings


class Settings(tk.Frame):

    title = "Settings"

    def __init__(self, master, controller=None):
        tk.Frame.__init__(self, master)
        _ = lang_init()
        # Main Frame Configuration

        self.grid(row=1, column=1, padx=20,
                  pady=20, sticky=tk.N+tk.E+tk.W+tk.S)
        self.grid_rowconfigure(3, minsize=100)

        # Define and Put Labels

        self.lbl_width = ttk.Label(
            self, text=_('Width:'), font=("Lucida Grande", 12))
        self.lbl_width.grid(row=0, column=0, padx=5,
                            pady=5, sticky=tk.N+tk.W)

        self.lbl_height = ttk.Label(
            self, text=_('Height:'), font=("Lucida Grande", 12))
        self.lbl_height.grid(row=1, column=0, padx=5,
                             pady=5, sticky=tk.W)

        self.lbl_colors = ttk.Label(
            self, text=_('Colors:'), font=("Lucida Grande", 12))
        self.lbl_colors.grid(row=2, column=0, padx=5,
                             pady=5, sticky=tk.W)

        # Textvariables for Textboxes

        self.width_str = tk.IntVar(value=controller.width)
        self.height_str = tk.IntVar(value=controller.height)
        self.colors_str = tk.IntVar(value=controller.colors)

        # Define and Put Textboxes

        self.tb_width = ttk.Entry(
            self, width=10, textvariable=self.width_str)
        self.tb_height = ttk.Entry(
            self, width=10, textvariable=self.height_str)
        self.tb_colors = ttk.Entry(
            self, width=10, textvariable=self.colors_str)

        self.tb_width.grid(row=0, column=1, padx=5,
                           pady=5, sticky=tk.N+tk.E)
        self.tb_height.grid(row=1, column=1, padx=5,
                            pady=5, sticky=tk.E)
        self.tb_colors.grid(row=2, column=1, padx=5,
                            pady=5, sticky=tk.E)

        # Buttons Configuration and Placement

        self.btn_ok = Round_Button(
            self, **btn_small_style,
            text=_("Ok"), command=lambda: self.ok_click(controller))
        self.btn_back = Round_Button(
            self, **btn_small_style,
            text=_("Back"), command=lambda: controller.show_frame("Main Menu"))

        self.btn_ok.grid(row=4, column=1, padx=5,
                         pady=5, sticky=tk.S+tk.E)
        self.btn_back.grid(row=4, column=0, padx=5,
                           pady=5, sticky=tk.S+tk.W)

        btn_small_style['background'] = ttk.Style().lookup(
            'TFrame', 'background')

    def get_values(self):
        return self.width_str.get(), self.height_str.get(), self.colors_str.get()

    def ok_click(self, controller):
        controller.get_settings(self.get_values)
        controller.show_frame("Main Menu")
