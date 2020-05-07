import tkinter
import os
from ..localization import lang_init
"""
Congratulations window module
=============================
"""


class CongratulationsWindow(tkinter.Frame):
    """
    Class that show congratulations window
    when the user solved the puzzle

    :param master: the Frame where game window must be placed in
    :param controller: the main class
    :cvar title: the name of the window
    """
    pathToFile = os.path.dirname(__file__)
    title = "Congratulations"

    def __init__(self, master, controller=None):
        _ = lang_init()
        tkinter.Frame.__init__(self, master)
        self.configure(bg='#4EB8FF')
        for i in range(5):
            self.rowconfigure(i, minsize=100, weight=1)
        congratulationsText = tkinter.Label(
            self, bg='#4EB8FF',
            text=_('Congratulations!\n') + _('You have beaten the puzzle!'),
            font='Arial 40')
        congratulationsText.grid(row=1, column=0, columnspan=2, sticky="NSEW")

        # loading images

        menuPhoto = tkinter.PhotoImage(
            file=os.path.join(
                CongratulationsWindow.pathToFile,
                'Assets/images/home_big.png')
        )
        resetPhoto = tkinter.PhotoImage(
            file=os.path.join(
                CongratulationsWindow.pathToFile,
                'Assets/images/reset_big.png')
        )

        # control buttons

        returnToMenuButton = tkinter.Button(self, bg='#4EB8FF',
                                            activebackground='#4EB8FF',
                                            image=menuPhoto,
                                            command=lambda:
                                            controller.show_frame("Main Menu"))
        returnToMenuButton.image = menuPhoto
        returnToMenuButton.grid(row=4, column=0, sticky="NSEW")
        restartButton = tkinter.Button(self, bg='#4EB8FF',
                                       activebackground='#4EB8FF',
                                       image=resetPhoto,
                                       command=lambda:
                                       controller.show_frame("Unruly Puzzle"))
        restartButton.image = resetPhoto
        restartButton.grid(row=4, column=1, sticky="NSEW")
