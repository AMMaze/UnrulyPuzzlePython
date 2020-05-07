from setuptools import setup, Command
import glob
import pathlib
import subprocess

cmdclasses = dict()


class BuildSphinx(Command):

    """Build Sphinx documentation."""

    description = 'Build Sphinx documentation'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from sphinx.ext import apidoc
        from sphinx.cmd.build import build_main
        apidoc.main(['-M', '-q', '-f', '-o',
                     'doc/toctree', 'UnrulyPuzzlePython'])
        build_main(
            ['-b', 'html', '.', 'doc/html']
        )


cmdclasses['build_sphinx'] = BuildSphinx


with open("README.md", "r") as readme_file:
    readme = readme_file.read()

with open("requirements.txt", "r") as req_file:
    requirements = req_file.readlines()

PO_FILES = 'localization/lang/*/LC_MESSAGES/UnrulyPuzzlePython.po'


def create_mo_files():
    mo_files = []
    prefix = 'UnrulyPuzzlePython'

    for po_path in glob.glob(str(pathlib.Path(prefix) / PO_FILES)):
        mo = pathlib.Path(po_path.replace('.po', '.mo'))

        subprocess.run(['msgfmt', '-o', str(mo), po_path], check=True)
        mo_files.append(str(mo.relative_to(prefix)))

    return mo_files


setup(
    name="UnrulyPuzzlePython",
    version="0.0.1",
    author="Marat Abbas, Dina Kizhinkeeva, Jaroslav Komarov",
    author_email='abbasmm@protonmail.com',
    description='Unruly puzzle with tkinter gui',
    long_description=readme,
    url="https://github.com/AMMaze/UnrulyPuzzlePython",
    install_requires=requirements,
    test_requires=["pytest>=2"],
    classifiers=[
        "Programming Language :: Python :: 3.7"
    ],
    packages=['UnrulyPuzzlePython'],
    package_dir={'UnrulyPuzzlePython': 'UnrulyPuzzlePython'},
    package_data={'UnrulyPuzzlePython':
                  ['gui/Assets/images/*.png',
                   'gui/Assets/fonts/Roboto-Regular.ttf'
                   ] + create_mo_files(),
                  },
    py_modules=[
        'UnrulyPuzzlePython.gui.game_window',
        'UnrulyPuzzlePython.gui.main_menu',
        'UnrulyPuzzlePython.gui.help',
        'UnrulyPuzzlePython.gui.settings',
        'UnrulyPuzzlePython.gui.congratulations_window',
        'UnrulyPuzzlePython.gui.styles.Custom_Button',
        'UnrulyPuzzlePython.gui.styles.btn_styles',
        'UnrulyPuzzlePython.localization.setup_loc',
        'UnrulyPuzzlePython.solver.unruly_solver',
        'UnrulyPuzzlePython.solver.check_solution'
    ],
    cmdclass=cmdclasses
)
