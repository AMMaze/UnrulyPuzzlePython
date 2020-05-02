import random
import tkinter
# from PIL import ImageTk, Image
from solver.unruly_solver import Solver
from tkinter import messagebox


class GameWindow(tkinter.Frame):

    title = "Unruly Puzzle"

    colorArray = ['white', 'black', 'red', 'green', 'blue', 'cyan',
                  'yellow', 'magenta']
    colors = []
    rows = 0
    cols = 0
    colorNumber = 0
    buttons = []
    solution = []

    def __init__(self, master, controller=None):
        tkinter.Frame.__init__(self, master)
        resetPhoto = tkinter.PhotoImage(file='gui/Assets/images/reset.png')
        lockPhoto = tkinter.PhotoImage(file='gui/Assets/images/lock.png')
        hintPhoto = tkinter.PhotoImage(file='gui/Assets/images/light_bulb.png')
        returnPhoto = tkinter.PhotoImage(
            file='gui/Assets/images/back_arrow.png')

        self.cols = controller.width
        self.rows = controller.height
        self.colorNumber = controller.colors
        self.controller = controller
        F = tkinter.Frame(self, borderwidth=3, relief=tkinter.GROOVE)
        F.grid(row=0, column=0, sticky="NSEW")
        menuFrame = tkinter.Frame(self, relief=tkinter.GROOVE,
                                  bg='#4EB8FF')
        menuFrame.grid(row=1, column=0, sticky="NSEW")
        while True:
            inititallyBlockedCellNumber = round(self.rows*self.cols/6)
            initialBoard = [[1 for j in range(self.cols)]
                            for i in range(self.rows)]
            while inititallyBlockedCellNumber > 0:
                randomRow = random.randint(0, self.rows - 1)
                randomCol = random.randint(0, self.cols - 1)
                if initialBoard[randomRow][randomCol] == 1:
                    initialBoard[randomRow][randomCol] = 0
                    inititallyBlockedCellNumber -= 1
            colors = [[0 if initialBoard[i][j] == 1 else
                       random.randint(0, self.colorNumber - 1)
                       for j in range(self.cols)] for i in range(self.rows)]
            fixed_cells = []
            for i in range(self.rows):
                for j in range(self.cols):
                    if initialBoard[i][j] == 0:
                        fixed_cells.append((i, j, colors[i][j]))
            solver = Solver(rows=self.rows, columns=self.cols,
                            colors=self.colorNumber, fixed_cells=fixed_cells)
            try:
                self.solution = solver.solve()
                for i in range(self.rows):
                    for j in range(self.cols):
                        self.solution[i][j] = int(self.solution[i][j])
                blockedCellNumber = random.randint(
                    round(self.rows*self.cols/5),
                    round(self.rows*self.cols/3))
                initialBoard = [[1 for j in range(self.cols)]
                                for i in range(self.rows)]
                while blockedCellNumber > 0:
                    randomRow = random.randint(0, self.rows - 1)
                    randomCol = random.randint(0, self.cols - 1)
                    if initialBoard[randomRow][randomCol] == 1:
                        initialBoard[randomRow][randomCol] = 0
                        blockedCellNumber -= 1
                colors = [[0 if initialBoard[i][j] == 1 else
                           self.solution[i][j]
                           for j in range(self.cols)]
                          for i in range(self.rows)]
                break
            except TypeError:
                continue
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
        checkButton = tkinter.Button(menuFrame, bg='#4EB8FF',
                                     activebackground='#4EB8FF',
                                     text='Check',
                                     font='Arial 20',
                                     command=self.check)
        checkButton.pack(side='left', fill='both', expand=True)

    def buttonClicked(self, x, y):
        self.colors[x][y] = (self.colors[x][y] + 1) % min(self.colorNumber,
                                                          len(self.colorArray))
        self.buttons[x][y]['bg'] = self.colorArray[self.colors[x][y]]
        self.buttons[x][y].config(activebackground=self.buttons[x][y].
                                  cget('background'))

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
        return True

    def check(self):
        if self.checkIfSolved():
            self.controller.show_frame("Congratulations")
        else:
            tkinter.messagebox.showinfo(title='Oops',
                                        message='Seems like the puzzle' +
                                                ' is not solved yet!')

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
        for i in range(self.rows):
            for j in range(self.cols):
                self.colors[i][j] = int(self.solution[i][j])
                self.buttons[i][j]['bg'] = self.colorArray[self.colors[i][j]]
                self.buttons[i][j].config(activebackground=self.buttons[i][j].
                                          cget('background'))


if __name__ == "__main__":
    root = tkinter.Tk()
    container = tkinter.Frame(root)
    container.pack(side='top', fill='both', expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    frame = GameWindow(master=container, controller=root)
    frame.grid(row=0, column=0, sticky='NSEW')
    root.mainloop()
