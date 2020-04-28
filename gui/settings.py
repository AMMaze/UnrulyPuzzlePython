import tkinter as tk
import tkinter.ttk as ttk
from styles.Custom_Button import Round_Button

# Main Window

settings = tk.Tk()
settings.title("Settings")
settings.rowconfigure((0, 1), weight=1)
settings.columnconfigure((0, 1),  weight=1)

# Main Frame

root_frame = ttk.Frame(settings)
root_frame.grid(row=1, column=1, padx=20, pady=20, sticky=tk.N+tk.E+tk.W+tk.S)

# Define and Put Labels

lbl_width = ttk.Label(root_frame, text='Width:', font=("Lucida Grande", 15))
lbl_width.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N+tk.W)

lbl_height = ttk.Label(root_frame, text='Hright:', font=("Lucida Grande", 15))
lbl_height.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

lbl_colors = ttk.Label(root_frame, text='Colors:', font=("Lucida Grande", 15))
lbl_colors.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

# Textvariables for Textboxes

width_str = tk.StringVar()
height_str = tk.StringVar()
colors_str = tk.StringVar()

# Define and Put Textboxes

tb_width = ttk.Entry(root_frame, width=10, textvariable=width_str)
tb_height = ttk.Entry(root_frame, width=10, textvariable=height_str)
tb_colors = ttk.Entry(root_frame, width=10, textvariable=colors_str)

settings.mainloop()
