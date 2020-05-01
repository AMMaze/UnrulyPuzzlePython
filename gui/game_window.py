import random
import tkinter
# from PIL import ImageTk, Image
# from solver.unruly_solver import Grid, Commands


class GameWindow(tkinter.Frame):

    colorArray = ['white', 'black', 'red', 'green', 'blue', 'cyan',
                  'yellow', 'magenta']
    colors = []
    rows = 0
    cols = 0
    colorNumber = 0
    buttons = []

    def __init__(self, master, controller=None):
        tkinter.Frame.__init__(self, master)
        # self.minsize(600, 600)
        resetPhoto = tkinter.PhotoImage(file='images/reset.png')
        lockPhoto = tkinter.PhotoImage(file='images/lock.png')
        hintPhoto = tkinter.PhotoImage(file='images/light_bulb.png')
        returnPhoto = tkinter.PhotoImage(file='images/back_arrow.png')
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

        self.cols = controller.width
        self.rows = controller.height
        self.colorNumber = controller.colors
        F = tkinter.Frame(self, borderwidth=3, relief=tkinter.GROOVE)
        F.grid(row=0, column=0, sticky="NSEW")
        menuFrame = tkinter.Frame(self, relief=tkinter.GROOVE,
                                  bg='#4EB8FF')
        menuFrame.grid(row=1, column=0, sticky="NSEW")

        # F.master.columnconfigure(0, weight=1)
        # F.master.rowconfigure(1, weight=1)
        # menuFrame.master.columnconfigure(0, weight=1)
        # menuFrame.master.rowconfigure(0, weight=1)

        while True:
            initialBoard = [[random.randint(0, 1) for j in range(self.cols)]
                            for i in range(self.rows)]
            colors = [[0 if initialBoard[i][j] == 1 else
                       random.randint(0, self.colorNumber - 1)
                       for j in range(self.cols)] for i in range(self.rows)]
            # Check if this configuration is valid using solver
            break

        self.colors = colors
        self.buttons = [[tkinter.Button(F,
                                        bg=self.colorArray[self.colors[i][j]],
                                        command=lambda i=i, j=j:
                                        self.buttonClicked(i, j))
                         for j in range(self.cols)] for i in range(self.rows)]
        for i in range(self.rows):
            tkinter.Grid.rowconfigure(F, i, weight=1, minsize=64)
        for i in range(self.cols):
            tkinter.Grid.columnconfigure(F, i, weight=1, minsize=64)
        for i in range(self.rows):
            for j in range(self.cols):
                self.buttons[i][j].grid(row=i, column=j, sticky="NSEW")
                self.buttons[i][j].config(activebackground=self.buttons[i][j].
                                          cget('background'))
                if initialBoard[i][j] == 0:
                    self.buttons[i][j].config(state=tkinter.DISABLED,
                                              image=lockPhoto
                                              )
                    self.buttons[i][j].image = lockPhoto
        returnToMenuButton = tkinter.Button(menuFrame, bg='white',
                                            activebackground='white',
                                            image=returnPhoto,
                                            command=lambda:
                                            controller.show_frame("Main Menu"))
        returnToMenuButton.image = returnPhoto
        returnToMenuButton.pack(side='left', fill='both', expand=False)
        resetButton = tkinter.Button(menuFrame, bg='white',
                                     activebackground='white',
                                     image=resetPhoto,
                                     command=self.resetCells)
        resetButton.image = resetPhoto
        resetButton.pack(side='left', fill='both', expand=False)
        hintButton = tkinter.Button(menuFrame, bg='white',
                                    activebackground='white',
                                    image=hintPhoto,
                                    command=self.getHint)
        hintButton.image = hintPhoto
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
        if self.checkIfSolved():
            # Do something here
            return

    def checkIfSolved(self):
        for i in range(self.rows):
            colorCount = [0 for j in range(self.colorNumber)]
            for j in range(self.cols):
                colorCount[self.colors[i][j]] += 1
                if j >= 2 \
                        and self.colors[i][j] == self.colors[i][j - 1] \
                        and self.colors[i][j] == self.colors[i][j - 2]:
                    return False
            for j in range(self.colorNumber):
                if colorCount[j] != self.cols/self.colorNumber:
                    return False

        for j in range(self.cols):
            colorCount = [0 for j in range(self.colorNumber)]
            for i in range(self.rows):
                colorCount[self.colors[i][j]] += 1
                if i >= 2 \
                        and self.colors[i][j] == self.colors[i - 1][j] \
                        and self.colors[i][j] == self.colors[i - 2][j]:
                    return False
            for i in range(self.colorNumber):
                if colorCount[i] != self.cols/self.colorNumber:
                    return False

    def resetCells(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.buttons[i][j]['state'] != tkinter.DISABLED:
                    self.colors[i][j] = 0
                    self.buttons[i][j]['bg'] = \
                        self.colorArray[self.colors[i][j]]
                    self.buttons[i][j].config(
                        activebackground=self.buttons[i][j].cget('background'))

    def getHint(self):
        return


if __name__ == "__main__":
    root = tkinter.Tk()
    container = tkinter.Frame(root)
    container.pack(side='top', fill='both', expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    # resetPhoto = tkinter.PhotoImage(file='images/reset.png')
    # lockPhoto = tkinter.PhotoImage(file='images/lock.png')
    # hintPhoto = tkinter.PhotoImage(file='images/light_bulb.png')
    # returnPhoto = tkinter.PhotoImage(file='images/back_arrow.png')
    # print(lockPhoto.width())
    frame = GameWindow(master=container, controller=root)
    frame.grid(row=0, column=0, sticky='NSEW')
    root.mainloop()
