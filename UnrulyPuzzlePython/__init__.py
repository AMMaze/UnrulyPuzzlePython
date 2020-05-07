"""
==================
UnrulyPuzzlePython
==================

Python implementation of from Simon Tatham's Portable Puzzle
Collection with variable number of colors.

Interface:
==========

    In main menu player can push button 'New Game'
    to start new game with random grid. After starting
    new game and returning to main menu the 'Continue'
    button will appear. This button allows to continiue
    game without generating new grid.

    Press 'Settings' to define grid parameters.
    Height and width of the grid should be greater than
    2 and should be divisible by the number of color.
    The number of colors should be no more than 8.

    Press 'Help' button to see rules.

    On game window use arrow button to return to main menu.
    Use circle arrow to reset the grid. Use light bulb
    button to solve puzzle. Finally, use 'Check' button
    to check your solution.


Rules:
======

    The player is given a grid of cells with size N x M. The color of \
    the cell can be changed by clicking on it. Each square can take one \
    of C possible colors. The player has to repaint the grid so that it \
    satisfies the following rules:

    1. Each row and column should contain the same number of
     cells of the same color.
    2. No row or column may contain three consecutive squares
     of the same colour.
"""

name = 'UnrulyPuzzlePython'
__version__ = '0.0.1'
