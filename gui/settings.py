import tkinter as tk
import tkinter.ttk as ttk
from styles.Custom_Button import Round_Button
from styles.btn_styles import btn_small_style

# Main Window

settings = tk.Tk()
settings.title("Settings")
settings.rowconfigure((0, 1), weight=1)
settings.columnconfigure((0, 1),  weight=1)

# Main Frame

root_frame = ttk.Frame(settings)
root_frame.grid(row=1, column=1, padx=20, pady=20, sticky=tk.N+tk.E+tk.W+tk.S)

# Frame Grid Configuration

root_frame.grid_rowconfigure(3, minsize=100)

# Define and Put Labels

lbl_width = ttk.Label(root_frame, text='Width:', font=("Lucida Grande", 12))
lbl_width.grid(row=0, column=0, padx=5, pady=5, sticky=tk.N+tk.W)

lbl_height = ttk.Label(root_frame, text='Height:', font=("Lucida Grande", 12))
lbl_height.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

lbl_colors = ttk.Label(root_frame, text='Colors:', font=("Lucida Grande", 12))
lbl_colors.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

# Textvariables for Textboxes

width_str = tk.StringVar()
height_str = tk.StringVar()
colors_str = tk.StringVar()

# Define and Put Textboxes

tb_width = ttk.Entry(root_frame, width=10, textvariable=width_str)
tb_height = ttk.Entry(root_frame, width=10, textvariable=height_str)
tb_colors = ttk.Entry(root_frame, width=10, textvariable=colors_str)

tb_width.grid(row=0, column=1, padx=5, pady=5, sticky=tk.N+tk.E)
tb_height.grid(row=1, column=1, padx=5, pady=5, sticky=tk.E)
tb_colors.grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)

# Buttons

btn_ok = Round_Button(root_frame, **btn_small_style,
                      text="Ok")
btn_back = Round_Button(root_frame, **btn_small_style,
                        text="Back")

btn_ok.grid(row=4, column=1, padx=5, pady=5, sticky=tk.S+tk.E)
btn_back.grid(row=4, column=0, padx=5, pady=5, sticky=tk.S+tk.W)

btn_small_style['background'] = ttk.Style().lookup('TFrame', 'background')

settings.update()
settings.minsize(settings.winfo_width(), settings.winfo_height())

settings.mainloop()
