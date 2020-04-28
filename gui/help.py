import tkinter as tk
import tkinter.ttk as ttk
from styles.Custom_Button import Round_Button
from styles.btn_styles import btn_small_style

# Help Window


class Help:

    RULES = """The player is given a grid of cells with size N x M. The color of \
    the cell can be changed by clicking on it. Each square can take one \
    of C possible colors. The player has to repaint the grid so that it \
    satisfies the following rules:

    1. Each row and column should contain the same number of
     cells of the same color.
    2. No row or column may contain three consecutive squares
     of the same colour."""

    def __init__(self, master):

        self.help = master
        self.help.title("Help")
        self.help.rowconfigure((0, 1), weight=1)
        self.help.columnconfigure((0, 1),  weight=1)

        # Main Frame

        self.root_frame = ttk.Frame(self.help)
        self.root_frame.grid(row=1, column=1, padx=20,
                             pady=20, sticky=tk.N+tk.E+tk.W+tk.S)

        # Define and Put LabelFrame

        self.rules_frame = tk.LabelFrame(
            self.root_frame, text="Rules", font=("Lucida Grande", 18))
        self.rules_frame.grid(row=0, column=0, padx=5,
                              pady=5, sticky=tk.N+tk.E+tk.W+tk.S)

        self.text = tk.Text(self.rules_frame, width=35,
                            wrap=tk.WORD, padx=10, pady=10)
        self.text.insert(tk.END, self.RULES)
        self.text.grid()

        # Buttons

        self.btn_back = Round_Button(self.root_frame, **btn_small_style,
                                     text="Back")

        self.btn_back.grid(row=1, column=0, padx=5,
                           pady=5, sticky=tk.S+tk.W+tk.E)

        btn_small_style['background'] = ttk.Style().lookup(
            'TFrame', 'background')

        self.help.update()
        self.help.minsize(help.winfo_width(), help.winfo_height())

# help.mainloop()
