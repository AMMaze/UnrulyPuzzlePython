import tkinter as tk
import tkinter.ttk as ttk
from gui.game_window import GameWindow
from gui.main_menu import MainMenu
from gui.help import Help
from gui.settings import Settings


class UnrulyPuzzle(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self._frame = None
        self.frames = {}
        self.container = tk.Frame(self)
        self.container.rowconfigure((0, 2), weight=1)
        self.container.columnconfigure((0, 2),  weight=1)
        self.container.grid(row=0, column=0, sticky=tk.N+tk.E+tk.W+tk.S)
        self.frames['Main Menu'] = MainMenu
        self.frames['Help'] = Help
        # self.frames['Settings'] = Settings(super(), self)
        self.show_frame("Main Menu")

    def show_frame(self, page_name):
        frame_class = self.frames[page_name]
        if self._frame is not None:
            self._frame.destroy()
        self.title(page_name)
        self._frame = frame_class(self.container, self)
        self._frame.grid(row=1, column=1, padx=20, pady=20,
                         sticky=tk.N+tk.E+tk.W+tk.S)
        self._frame.update()
        self.geometry("{}x{}".format(self._frame.winfo_width() +
                                     50, self._frame.winfo_height() + 50))
        self.minsize(self._frame.winfo_width() + 50,
                     self._frame.winfo_height() + 50)


if __name__ == "__main__":
    app = UnrulyPuzzle()
    app.mainloop()
