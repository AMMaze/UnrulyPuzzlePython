import tkinter as tk
import tkinter.ttk as ttk
from styles.Custom_Button import Round_Button

# Main Window

main_menu = tk.Tk()
main_menu.title("Main Menu")
main_menu.rowconfigure((0, 2), weight=1)
main_menu.columnconfigure((0, 2),  weight=1)

# Main Frame

root_frame = ttk.Frame(main_menu)
root_frame.grid(row=1, column=1, padx=20, pady=20, sticky=tk.N+tk.E+tk.W+tk.S)

# Define and Put Label

title = ttk.Label(root_frame, text="Unruly Puzzle", font=("Lucida Grande", 18))
title.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N+tk.E+tk.W+tk.S)

# Buttons Definitions

btn_default_style = {
    'size': 5,
    'static_colour': (149, 213, 255),
    'static_t_colour': (0, 0, 0),
    'transformation_colour': (74, 184, 255),
    'transformation_t_colour': (0, 0, 0),
    'background': ttk.Style().lookup('TFrame', 'background')
}

btn_new_game = Round_Button(root_frame, **btn_default_style,
                            text="New Game")
# btn_new_game = ttk.Button(root_frame,
# text="New Game", command=None)
btn_restart = Round_Button(root_frame, **btn_default_style,
                           text="Restart")
btn_options = Round_Button(root_frame, **btn_default_style,
                           text="Options")
btn_help = Round_Button(root_frame, **btn_default_style,
                        text="Help")
btn_exit = Round_Button(root_frame, **btn_default_style,
                        text="Exit")

# Style Definitions

btn_style = ttk.Style()
btn_style.configure('TButton', padding=15, background='#95D5FF', relief="flat")

# Buttons Placement

btn_new_game.grid(row=1, column=0, pady=10, sticky=tk.W+tk.E)
btn_restart.grid(row=2, column=0, pady=10, sticky=tk.W+tk.E)
btn_options.grid(row=3, column=0, pady=10, sticky=tk.W+tk.E)
btn_help.grid(row=4, column=0, pady=10, sticky=tk.W+tk.E)
btn_exit.grid(row=5, column=0, pady=10, sticky=tk.W+tk.E)

main_menu.update()
main_menu.minsize(main_menu.winfo_width(), main_menu.winfo_height())

main_menu.mainloop()
