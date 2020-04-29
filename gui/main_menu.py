import tkinter as tk
import tkinter.ttk as ttk
from styles.Custom_Button import Round_Button
from styles.btn_styles import btn_default_style

# Main Window


class MainMenu:

    def __init__(self, master):
        self.main_menu = master
        self.main_menu.title("Main Menu")
        self.main_menu.rowconfigure((0, 2), weight=1)
        self.main_menu.columnconfigure((0, 2),  weight=1)

        # Main Frame

        self.root_frame = ttk.Frame(self.main_menu)
        self.root_frame.grid(row=1, column=1, padx=20,
                             pady=20, sticky=tk.N+tk.E+tk.W+tk.S)

        # Define and Put Label

        self.title = ttk.Label(
            self.root_frame, text="Unruly Puzzle", font=("Lucida Grande", 18))
        self.title.grid(row=0, column=0, padx=5, pady=5,
                        sticky=tk.N+tk.E+tk.W+tk.S)

        # Buttons Definitions

        self.btn_new_game = Round_Button(
            self.root_frame, **btn_default_style, text="New Game")
        self.btn_restart = Round_Button(
            self.root_frame, **btn_default_style, text="Restart")
        self.btn_options = Round_Button(
            self.root_frame, **btn_default_style, text="Options")
        self.btn_help = Round_Button(
            self.root_frame, **btn_default_style, text="Help")
        self.btn_exit = Round_Button(
            self.root_frame, **btn_default_style, text="Exit")

        # Style Definitions

        btn_default_style['background'] = ttk.Style().lookup(
            'TFrame', 'background')

        # Buttons Placement

        self.btn_new_game.grid(row=1, column=0, pady=10, sticky=tk.W+tk.E)
        self.btn_restart.grid(row=2, column=0, pady=10, sticky=tk.W+tk.E)
        self.btn_options.grid(row=3, column=0, pady=10, sticky=tk.W+tk.E)
        self.btn_help.grid(row=4, column=0, pady=10, sticky=tk.W+tk.E)
        self.btn_exit.grid(row=5, column=0, pady=10, sticky=tk.W+tk.E)

        self.main_menu.update()
        self.main_menu.minsize(
            self.main_menu.winfo_width(), self.main_menu.winfo_height())


if __name__ == "__main__":
    root = tk.Tk()
    main_menu = MainMenu(root)
    root.mainloop()
