import tkinter as tk

main_menu = tk.Tk()
main_menu.title("Main Menu")

root_frame = tk.Frame(main_menu)
root_frame.grid(row=0, column=0, padx=10, pady=5, sticky=tk.N+tk.E+tk.W)

title = tk.Label(main_menu, text="Unruly Puzzle", font=("Lucida Grande", 18))
title.grid(row=0, column=0, padx=5, pady=5)

main_menu.update()
main_menu.minsize(main_menu.winfo_width(), main_menu.winfo_height())

main_menu.mainloop()
