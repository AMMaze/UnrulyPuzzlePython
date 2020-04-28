import tkinter as tk
import tkinter.ttk as ttk
from styles.Custom_Button import Round_Button
from styles.btn_styles import btn_small_style

# Main Window

help = tk.Tk()
help.title("Help")
help.rowconfigure((0, 1), weight=1)
help.columnconfigure((0, 1),  weight=1)

# Main Frame

root_frame = ttk.Frame(help)
root_frame.grid(row=1, column=1, padx=20, pady=20, sticky=tk.N+tk.E+tk.W+tk.S)

# Define and Put LabelFrame

rules_frame = tk.LabelFrame(
    root_frame, text="Rules", font=("Lucida Grande", 18))
rules_frame.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N+tk.E+tk.W+tk.S)

# Text
rules = """The player is given a grid of cells with size N x M. The color of \
the cell can be changed by clicking on it. Each square can take one \
of C possible colors. The player has to repaint the grid so that it \
satisfies the following rules:

1. Each row and column should contain the same number of
 cells of the same color.
2. No row or column may contain three consecutive squares
 of the same colour."""

text = tk.Text(rules_frame, width=35, wrap=tk.WORD, padx=10, pady=10)
text.insert(tk.END, rules)
text.grid()

# Buttons

btn_back = Round_Button(root_frame, **btn_small_style,
                        text="Back")

btn_back.grid(row=1, column=0, padx=5, pady=5, sticky=tk.S+tk.W+tk.E)

btn_small_style['background'] = ttk.Style().lookup('TFrame', 'background')

help.update()
help.minsize(help.winfo_width(), help.winfo_height())

help.mainloop()
