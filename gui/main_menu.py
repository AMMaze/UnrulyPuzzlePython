import tkinter as tk

# Main Window

main_menu = tk.Tk()
main_menu.title("Main Menu")
main_menu.rowconfigure((0, 2), weight=1)
main_menu.columnconfigure((0, 2),  weight=1)

# Main Frame

root_frame = tk.Frame(main_menu)
root_frame.grid(row=1, column=1, padx=20, pady=20, sticky=tk.N+tk.E+tk.W+tk.S)

# Define and Put Label

title = tk.Label(root_frame, text="Unruly Puzzle", font=("Lucida Grande", 18))
title.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N+tk.E+tk.W+tk.S)

# Buttons Definitions

btn_new_game = tk.Button(root_frame,
                         text="New Game", padx=15, pady=15,  command=None)
btn_restart = tk.Button(root_frame,
                        text="Restart", padx=15, pady=15,  command=None)
btn_options = tk.Button(root_frame,
                        text="Options", padx=15, pady=15,  command=None)
btn_help = tk.Button(root_frame,
                     text="Help", padx=15, pady=15,  command=None)
btn_exit = tk.Button(root_frame,
                     text="Exit", padx=15, pady=15,  command=None)

# Buttons Placement

btn_new_game.grid(row=1, column=0, pady=10, sticky=tk.W+tk.E)
btn_restart.grid(row=2, column=0, pady=10, sticky=tk.W+tk.E)
btn_options.grid(row=3, column=0, pady=10, sticky=tk.W+tk.E)
btn_help.grid(row=4, column=0, pady=10, sticky=tk.W+tk.E)
btn_exit.grid(row=5, column=0, pady=10, sticky=tk.W+tk.E)

main_menu.update()
main_menu.minsize(main_menu.winfo_width(), main_menu.winfo_height())

main_menu.mainloop()
