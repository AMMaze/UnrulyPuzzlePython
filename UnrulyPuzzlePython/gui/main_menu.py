import tkinter as tk
import tkinter.ttk as ttk
from gui.styles.Custom_Button import Round_Button
from gui.styles.btn_styles import btn_default_style


class MainMenu(tk.Frame):

    title = "Main Menu"

    def __init__(self, master, controller=None):
        tk.Frame.__init__(self, master)

        # Define and Put Label

        self.title = ttk.Label(
            self, text="Unruly Puzzle", font=("Lucida Grande", 18))
        self.title.grid(row=0, column=0, padx=5, pady=5,
                        sticky=tk.N+tk.E+tk.W)

        # Buttons Definitions

        self.btn_new_game = Round_Button(
            self, **btn_default_style, text="New Game",
            command=lambda: controller.show_frame("Unruly Puzzle"))
        self.btn_restart = Round_Button(
            self, **btn_default_style, text="Continue",
            command=lambda: controller.continue_game())
        self.btn_options = Round_Button(
            self, **btn_default_style, text="Settings",
            command=lambda: controller.show_frame("Settings"))
        self.btn_help = Round_Button(
            self, **btn_default_style, text="Help",
            command=lambda: controller.show_frame("Help"))
        self.btn_exit = Round_Button(
            self, **btn_default_style, text="Exit",
            command=master.winfo_toplevel().destroy)

        # Style Definitions

        btn_default_style['background'] = ttk.Style().lookup(
            'TFrame', 'background')

        # Buttons Placement

        self.btn_new_game.grid(row=1, column=0, pady=10, sticky=tk.W+tk.E)
        if controller.puzzle_frame is not None:
            self.btn_restart.grid(row=2, column=0, pady=10, sticky=tk.W+tk.E)
        self.btn_options.grid(row=3, column=0, pady=10, sticky=tk.W+tk.E)
        self.btn_help.grid(row=4, column=0, pady=10, sticky=tk.W+tk.E)
        self.btn_exit.grid(row=5, column=0, pady=10, sticky=tk.W+tk.E)


if __name__ == "__main__":
    root = tk.Tk()
    main_menu = MainMenu(root)
    root.mainloop()
