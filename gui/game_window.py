import tkinter


def buttonClicked(x, y):
    # изменяем текст кнопки
    # print(len(colorArray))
    colors[x][y] = (colors[x][y] + 1) % min(c, len(colorArray))
    buttons[x][y]['bg'] = colorArray[colors[x][y]]
    buttons[x][y].config(activebackground=buttons[x][y].cget('background'))


def resetCells():
    for i in range(n):
        for j in range(m):
            colors[i][j] = 0
            buttons[i][j]['bg'] = colorArray[colors[i][j]]
            buttons[i][j].config(activebackground=buttons[i][j].
                                 cget('background'))


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

colorArray = ['white', 'black', 'red', 'green', 'blue', 'cyan', 'yellow',
              'magenta']

m = 4
n = 5
c = 50

root = tkinter.Tk()
tkinter.Grid.rowconfigure(root, 0, weight=1)
tkinter.Grid.columnconfigure(root, 0, weight=1)
F = tkinter.Frame(root, borderwidth=3, relief=tkinter.GROOVE)
F.master.columnconfigure(0, weight=1)
F.master.rowconfigure(0, weight=1)
F.grid(row=0, column=0, sticky="NSEW")

colors = [[0 for j in range(m)] for i in range(n)]
buttons = [[tkinter.Button(F, bg=colorArray[colors[i][j]],
                           command=lambda i=i, j=j:buttonClicked(i, j))
            for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        tkinter.Grid.rowconfigure(F, i, weight=1)
        tkinter.Grid.columnconfigure(F, j, weight=1)
        buttons[i][j].grid(row=i, column=j, sticky="NSEW")
        buttons[i][j].config(activebackground=buttons[i][j].cget('background'))
        # buttons[i][j].bind('<Motion>', dump)


tkinter.Grid.rowconfigure(F, n, weight=1)
resetButton = tkinter.Button(F, bg='white', activebackground='white',
                             text='Reset all cells', command=resetCells)
resetButton.grid(row=n, column=0, columnspan=m, sticky="NSEW")

root.mainloop()