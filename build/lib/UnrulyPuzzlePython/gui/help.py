import tkinter as tk
import tkinter.ttk as ttk
from UnrulyPuzzlePython.gui.styles.Custom_Button import Round_Button
from UnrulyPuzzlePython.gui.styles.btn_styles import btn_small_style


class Help(tk.Frame):

    title = "Help"

    RULES = """The player is given a grid of cells with size N x M. The color of \
    the cell can be changed by clicking on it. Each square can take one \
    of C possible colors. The player has to repaint the grid so that it \
    satisfies the following rules:

    1. Each row and column should contain the same number of
     cells of the same color.
    2. No row or column may contain three consecutive squares
     of the same colour."""

    def __init__(self, master, controller=None):
        tk.Frame.__init__(self, master)

        # Define and Put LabelFrame

        self.rules_frame = tk.LabelFrame(
            self, text="Rules", font=("Lucida Grande", 18))
        self.rules_frame.grid(row=0, column=0, padx=5,
                              pady=5, sticky=tk.N+tk.E+tk.W+tk.S)

        # Define, Fill and Put Text Widget

        self.text = tk.Text(self.rules_frame, width=35,
                            wrap=tk.WORD, padx=10, pady=10)
        self.text.insert(tk.END, self.RULES)
        self.text.grid()

        # Make Text Uneditable

        self.text.config(state=tk.DISABLED)

        # Buttons Configuraton and Placement

        self.btn_back = Round_Button(
            self, **btn_small_style,
            text="Back",
            command=lambda: controller.show_frame("Main Menu")
        )

        self.btn_back.grid(row=1, column=0, padx=5,
                           pady=5, sticky=tk.S+tk.W+tk.E)

        # Style Configuration

        btn_small_style['background'] = ttk.Style().lookup(
            'TFrame', 'background')


if __name__ == "__main__":
    root = tk.Tk()
    main_menu = Help(root)
    root.mainloop()
