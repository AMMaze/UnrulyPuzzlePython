import tkinter


class CongratulationsWindow(tkinter.Frame):

    title = "Congratulations"

    def __init__(self, master, controller=None):
        tkinter.Frame.__init__(self, master)
        self.configure(bg='#4EB8FF')
        for i in range(5):
            self.rowconfigure(i, minsize=100, weight=1)
        congratulationsText = tkinter.Label(self, bg='#4EB8FF',
                                            text='Congratulations!\n' +
                                                 'You have beaten the puzzle!',
                                            font='Arial 40')
        congratulationsText.grid(row=1, column=0, columnspan=2, sticky="NSEW")
        menuPhoto = tkinter.PhotoImage(
            file='gui/Assets/images/home_big.png')
        resetPhoto = tkinter.PhotoImage(file='gui/Assets/images/reset_big.png')
        print(resetPhoto.width(), resetPhoto.height())
        # menuFrame = tkinter.Frame(self, relief=tkinter.GROOVE,
        #                           bg='#4EB8FF')
        # menuFrame.grid(row=1, column=0, columnspan=2, sticky="NSEW")
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