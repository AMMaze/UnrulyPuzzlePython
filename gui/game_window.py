import random
import tkinter


class GameWindow(tkinter.Frame):

    colorArray = ['white', 'black', 'red', 'green', 'blue', 'cyan',
                  'yellow', 'magenta']
    colors = []
    rows = 0
    cols = 0
    colorNumber = 0
    buttons = []

    def __init__(self, parent, controller, lockPhoto, returnPhoto, resetPhoto,
                 hintPhoto):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        # colorArray = ['#FF6633', '#FFB399', '#FF33FF',
        #               '#FFFF99', '#00B3E6', '#E6B333',
        #               '#3366E6', '#999966', '#99FF99',
        #               '#B34D4D', '#80B300', '#809900',
        #               '#E6B3B3', '#6680B3', '#66991A',
        #               '#FF99E6', '#CCFF1A', '#FF1A66',
        #               '#E6331A', '#33FFCC', '#66994D',
        #               '#B366CC', '#4D8000', '#B33300',
        #               '#CC80CC', '#66664D', '#991AFF',
        #               '#E666FF', '#4DB3FF', '#1AB399',
        #               '#E666B3', '#33991A', '#CC9999',
        #               '#B3B31A', '#00E680', '#4D8066',
        #               '#809980', '#E6FF80', '#1AFF33',
        #               '#999933', '#FF3380', '#CCCC00',
        #               '#66E64D', '#4D80CC', '#9900B3',
        #               '#E64D66', '#4DB380', '#FF4D4D',
        #               '#99E6E6', '#6666FF']

        # This variables should be given as parameters
        self.cols = 4
        self.rows = 5
        self.colorNumber = 8
        initialBoard = [[random.randint(0, 1) for j in range(self.cols)]
                        for i in range(self.rows)]
        tkinter.Grid.rowconfigure(self, 0, weight=1)
        tkinter.Grid.columnconfigure(self, 0, weight=1)
        F = tkinter.Frame(self, borderwidth=3, relief=tkinter.GROOVE)
        # F.master.columnconfigure(0, weight=1)
        # F.master.rowconfigure(1, weight=1)
        F.grid(row=0, column=0, sticky="NSEW")
        menuFrame = tkinter.Frame(self, relief=tkinter.GROOVE,
                                  bg='#4EB8FF')
        # menuFrame.master.columnconfigure(0, weight=1)
        # menuFrame.master.rowconfigure(0, weight=1)
        menuFrame.grid(row=1, column=0, sticky="NSEW")

        colors = [[0 if initialBoard[i][j] == 1 else
                   random.randint(0, self.colorNumber - 1)
                   for j in range(self.cols)] for i in range(self.rows)]
        self.colors = colors
        self.buttons = [[tkinter.Button(F,
                                        bg=self.colorArray[self.colors[i][j]],
                                        command=lambda i=i, j=j:
                                        self.buttonClicked(i, j))
                         for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                tkinter.Grid.rowconfigure(F, i + 1, weight=1)
                tkinter.Grid.columnconfigure(F, j, weight=1)
                self.buttons[i][j].grid(row=i + 1, column=j, sticky="NSEW")
                self.buttons[i][j].config(activebackground=self.buttons[i][j].
                                          cget('background'),
                                          width=64, height=64)
                if initialBoard[i][j] == 0:
                    self.buttons[i][j].config(state=tkinter.DISABLED,
                                              image=lockPhoto)
                # buttons[i][j].bind('<Motion>', dump)

        returnToMenuButton = tkinter.Button(menuFrame, bg='white',
                                            activebackground='white',
                                            image=returnPhoto,
                                            command=self.returnToMenu)
        returnToMenuButton.pack(side='left', fill='both', expand=False)
        resetButton = tkinter.Button(menuFrame, bg='white',
                                     activebackground='white',
                                     image=resetPhoto, command=self.resetCells)
        resetButton.pack(side='left', fill='both', expand=False)
        hintButton = tkinter.Button(menuFrame, bg='white',
                                    activebackground='white',
                                    image=hintPhoto, command=self.getHint)
        hintButton.pack(side='left', fill='both', expand=False)
        # resetButton.grid(row=0, column=2, columnspan=2, sticky="NSEW")
        # returnToMenuButton.grid(row=0, column=0, columnspan=2, sticky="NSEW")

    def buttonClicked(self, x, y):
        # изменяем текст кнопки
        # print(len(colorArray))
        self.colors[x][y] = (self.colors[x][y] + 1) % min(self.colorNumber,
                                                          len(self.colorArray))
        self.buttons[x][y]['bg'] = self.colorArray[self.colors[x][y]]
        self.buttons[x][y].config(activebackground=self.buttons[x][y].
                                  cget('background'))

    def resetCells(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.buttons[i][j]['state'] != tkinter.DISABLED:
                    self.colors[i][j] = 0
                    self.buttons[i][j]['bg'] = self.colorArray[self.colors[i][j]]
                    self.buttons[i][j].config(activebackground=self.buttons[i][j].
                                              cget('background'))

    def returnToMenu(self):
        return

    def getHint(self):
        return


# if __name__ == "__main__":
#     root = tkinter.Tk()
#     container = tkinter.Frame(root)
#     container.pack(side='top', fill='both', expand=True)
#     container.grid_rowconfigure(0, weight=1)
#     container.grid_columnconfigure(0, weight=1)
#     resetPhoto = tkinter.PhotoImage(file='../images/reset.png')
#     lockPhoto = tkinter.PhotoImage(file='../images/lock.png')
#     hintPhoto = tkinter.PhotoImage(file='../images/light_bulb.png')
#     returnPhoto = tkinter.PhotoImage(file='../images/back_arrow.png')
#     print(lockPhoto.width())
#     frame = GameWindow(parent=container, controller=root, lockPhoto=lockPhoto,
#                        returnPhoto=returnPhoto, resetPhoto=resetPhoto, hintPhoto=hintPhoto)
#     frame.grid(row=0, column=0, sticky='NSEW')
#     root.mainloop()