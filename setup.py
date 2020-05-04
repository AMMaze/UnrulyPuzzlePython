from setuptools import setup, find_packages

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
    # packages=find_packages(),
    url="https://github.com/AMMaze/UnrulyPuzzlePython",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ],
    packages=['UnrulyPuzzlePython'],
    package_dir={'UnrulyPuzzlePython': 'UnrulyPuzzlePython'},
    package_data={'UnrulyPuzzlePython': ['gui/Assets/images/*.png']},
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
    # package_dir={
    #     'gui': '',
    #     'solver': ''
    # },
    # data_files=[
    #     ('gui/Assets/images',
    #      ['UnrulyPuzzlePython/gui/Assets/images/reset.png',
    #       'UnrulyPuzzlePython/gui/Assets/images/reset_big.png',
    #       'UnrulyPuzzlePython/gui/Assets/images/lock.png',
    #       'UnrulyPuzzlePython/gui/Assets/images/light_bulb.png',
    #       'UnrulyPuzzlePython/gui/Assets/images/home.png',
    #       'UnrulyPuzzlePython/gui/Assets/images/home_big.png',
    #       'UnrulyPuzzlePython/gui/Assets/images/back_arrow.png'])
    # ]
)
