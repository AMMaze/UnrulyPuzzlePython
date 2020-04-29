import tkinter as tk
import tkinter.ttk as ttk
from styles.Custom_Button import Round_Button
from styles.btn_styles import btn_default_style
from game_window import GameWindow


# Main Window


class UnrulyGame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Main Menu")
        self.minsize(self.winfo_width(), self.winfo_height())
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        resetPhoto = tk.PhotoImage(file='../images/reset.png')
        lockPhoto = tk.PhotoImage(file='../images/lock.png')
        hintPhoto = tk.PhotoImage(file='../images/light_bulb.png')
        returnPhoto = tk.PhotoImage(file='../images/back_arrow.png')
        print(lockPhoto.width())
        gameWindowFrame = GameWindow(parent=container, controller=self,
                                     lockPhoto=lockPhoto,
                                     returnPhoto=returnPhoto,
                                     resetPhoto=resetPhoto,
                                     hintPhoto=hintPhoto)
        self.frames["GameWindow"] = gameWindowFrame
        gameWindowFrame.grid(row=0, column=0, sticky='NSEW')
        mainMenuFrame = MainMenu(parent=container, controller=self)
        self.frames["MainMenu"] = mainMenuFrame
        mainMenuFrame.grid(row=0, column=0, sticky='NSEW')
        self.show_frame("MainMenu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.grid(row=1, column=1, padx=20, pady=20,
                  sticky=tk.N + tk.E + tk.W + tk.S)

        title = ttk.Label(self, text="Unruly Puzzle",
                          font=("Lucida Grande", 18))
        title.grid(row=0, column=0, padx=5, pady=5,
                   sticky=tk.N + tk.E + tk.W + tk.S)

        btn_new_game = tk.Button(self, text="New Game",
                                    command=lambda: controller.show_frame("GameWindow"))
        btn_restart = Round_Button(self, **btn_default_style, text="Restart")
        btn_options = Round_Button(self, **btn_default_style, text="Options")
        btn_help = Round_Button(self, **btn_default_style, text="Help")
        btn_exit = Round_Button(self, **btn_default_style, text="Exit")

        # Style Definitions

        btn_default_style['background'] = ttk.Style().\
            lookup('TFrame', 'background')

        # Buttons Placement

        btn_new_game.grid(row=1, column=0, pady=10, sticky=tk.W + tk.E)
        btn_restart.grid(row=2, column=0, pady=10, sticky=tk.W + tk.E)
        btn_options.grid(row=3, column=0, pady=10, sticky=tk.W + tk.E)
        btn_help.grid(row=4, column=0, pady=10, sticky=tk.W + tk.E)
        btn_exit.grid(row=5, column=0, pady=10, sticky=tk.W + tk.E)


if __name__ == "__main__":
    app = UnrulyGame()
    app.mainloop()