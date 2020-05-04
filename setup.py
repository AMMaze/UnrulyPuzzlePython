from setuptools import setup

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

with open("requirements.txt", "r") as req_file:
    requirements = req_file.readlines()

setup(
    name="UnrulyPuzzlePython",
    version="0.0.1",
    author_email='abbasmm@protonmail.com',
    description='Unruly puzzle with tkinter gui',
    long_description=readme,
    url="https://github.com/AMMaze/UnrulyPuzzlePython",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ],
    packages=['UnrulyPuzzlePython'],
    package_dir={'UnrulyPuzzlePython': 'UnrulyPuzzlePython'},
    package_data={'UnrulyPuzzlePython':
                  ['gui/Assets/images/*.png',
                   'gui/Assets/fonts/Roboto-Regular.ttf']
                  },
    py_modules=[
        'UnrulyPuzzlePython.gui.game_window',
        'UnrulyPuzzlePython.gui.main_menu',
        'UnrulyPuzzlePython.gui.help',
        'UnrulyPuzzlePython.gui.settings',
        'UnrulyPuzzlePython.gui.congratulations_window',
        'UnrulyPuzzlePython.gui.styles.Custom_Button',
        'UnrulyPuzzlePython.gui.styles.btn_styles',
        'UnrulyPuzzlePython.solver.unruly_solver'
    ]
)
