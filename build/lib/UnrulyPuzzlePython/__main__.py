import tkinter as tk
import tkinter.ttk as ttk
from UnrulyPuzzlePython.gui.game_window import GameWindow
from UnrulyPuzzlePython.gui.main_menu import MainMenu
from UnrulyPuzzlePython.gui.help import Help
from UnrulyPuzzlePython.gui.settings import Settings
from UnrulyPuzzlePython.gui.game_window import GameWindow
from UnrulyPuzzlePython.gui.congratulations_window import CongratulationsWindow


class UnrulyPuzzle(tk.Tk):
    width = 8
    height = 8
    colors = 2

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Root Window Cofiguration

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Current Frame and Dict for Frames

        self._frame = None
        self.frames = {}

        # Current puzzle frame

        self.puzzle_frame = None

        # Root Frame Configuration and Placement

        self.container = tk.Frame(self)
        self.container.rowconfigure((0, 2), weight=1)
        self.container.columnconfigure((0, 2),  weight=1)
        self.container.grid(row=0, column=0, sticky=tk.N+tk.E+tk.W+tk.S)

        # Frames Dictionary Initialization

        self.frames[MainMenu.title] = MainMenu
        self.frames[Help.title] = Help
        self.frames[Settings.title] = Settings
        self.frames[GameWindow.title] = GameWindow
        self.frames[CongratulationsWindow.title] = CongratulationsWindow

        self.show_frame("Main Menu")

    def show_frame(self, page_name):
        """
        Shows frame specified by name from dictionary self.frames

        Destroys current frame if present, resizes root window to fit new frame

        :param page_name: name from self.frames dictionary
        """
        frame_class = self.frames[page_name]
        if self._frame is not None:
            # Using destroy causes freezes, so I replaced it with grid_forget
            # It may cause memory leaks,
            # but in most cases it won't because of garbage collector
            self._frame.grid_forget()
            # self._frame.destroy()
        self.title(page_name)

        # Creating and Configuring New Frame

        self._frame = frame_class(self.container, self)
        self._frame.grid(row=1, column=1, padx=20, pady=20,
                         sticky=tk.N+tk.E+tk.W+tk.S)
        self._frame.update()

        # Window Resizing

        self.geometry("{}x{}".format(self._frame.winfo_width() + 50,
                                     self._frame.winfo_height() + 50))
        self.minsize(self._frame.winfo_width() + 50,
                     self._frame.winfo_height() + 50)

        # Saving puzzle frame
        if page_name == GameWindow.title:
            self.puzzle_frame = self._frame

    def continue_game(self):
        if self._frame is not None:
            self._frame.grid_forget()
        self.title(self.puzzle_frame.title)
        self._frame = self.puzzle_frame
        self._frame.grid(row=1, column=1, padx=20, pady=20,
                         sticky=tk.N + tk.E + tk.W + tk.S)
        self._frame.update()

        # Window Resizing

        self.geometry("{}x{}".format(self._frame.winfo_width() + 50,
                                     self._frame.winfo_height() + 50))
        self.minsize(self._frame.winfo_width() + 50,
                     self._frame.winfo_height() + 50)

    def forget_game(self):
        self.puzzle_frame = None

    def get_settings(self, getter):
        self.width, self.height, self.colors = getter()


if __name__ == "__main__":
    app = UnrulyPuzzle()
    app.mainloop()