import tkinter as tk
import tkinter.ttk as ttk
from styles.Custom_Button import Round_Button
from styles.btn_styles import btn_small_style

# Settings


class Settings:

    def __init__(self, master):

        self.settings = master
        self.settings.title("Settings")
        self.settings.rowconfigure((0, 1), weight=1)
        self.settings.columnconfigure((0, 1),  weight=1)

        # Main Frame

        self.root_frame = ttk.Frame(self.settings)
        self.root_frame.grid(row=1, column=1, padx=20,
                             pady=20, sticky=tk.N+tk.E+tk.W+tk.S)

        # Frame Grid Configuration

        self.root_frame.grid_rowconfigure(3, minsize=100)

        # Define and Put Labels

        self.lbl_width = ttk.Label(
            self.root_frame, text='Width:', font=("Lucida Grande", 12))
        self.lbl_width.grid(row=0, column=0, padx=5,
                            pady=5, sticky=tk.N+tk.W)

        self.lbl_height = ttk.Label(
            self.root_frame, text='Height:', font=("Lucida Grande", 12))
        self.lbl_height.grid(row=1, column=0, padx=5,
                             pady=5, sticky=tk.W)

        self.lbl_colors = ttk.Label(
            self.root_frame, text='Colors:', font=("Lucida Grande", 12))
        self.lbl_colors.grid(row=2, column=0, padx=5,
                             pady=5, sticky=tk.W)

        # Textvariables for Textboxes

        self.width_str = tk.StringVar()
        self.height_str = tk.StringVar()
        self.colors_str = tk.StringVar()

        # Define and Put Textboxes

        self.tb_width = ttk.Entry(
            self.root_frame, width=10, textvariable=self.width_str)
        self.tb_height = ttk.Entry(
            self.root_frame, width=10, textvariable=self.height_str)
        self.tb_colors = ttk.Entry(
            self.root_frame, width=10, textvariable=self.colors_str)

        self.tb_width.grid(row=0, column=1, padx=5,
                           pady=5, sticky=tk.N+tk.E)
        self.tb_height.grid(row=1, column=1, padx=5,
                            pady=5, sticky=tk.E)
        self.tb_colors.grid(row=2, column=1, padx=5,
                            pady=5, sticky=tk.E)

        # Buttons

        self.btn_ok = Round_Button(self.root_frame, **btn_small_style,
                                   text="Ok")
        self.btn_back = Round_Button(self.root_frame, **btn_small_style,
                                     text="Back")

        self.btn_ok.grid(row=4, column=1, padx=5,
                         pady=5, sticky=tk.S+tk.E)
        self.btn_back.grid(row=4, column=0, padx=5,
                           pady=5, sticky=tk.S+tk.W)

        btn_small_style['background'] = ttk.Style().lookup(
            'TFrame', 'background')

        self.settings.update()
        self.settings.minsize(self.settings.winfo_width(),
                              self.settings.winfo_height())

# settings.mainloop()
