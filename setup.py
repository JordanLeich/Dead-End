""" Basic setup file for the game installation support for certain coding editors. """
from setuptools import setup

setup(
    name='Dead End',
    version='v5.0',
    packages=[''],
    url='https://github.com/JordanLeich/Dead-End',
    license='MIT',
    author='Jordan Leich',
    author_email='jordanleich@gmail.com',
    description='This is a zombie survival game where you must make the best choices and decisions possible in order '
                'to live. As a survivor, you will encounter zombies, weapons, people, and a merchant to buy from with '
                'an in-game currency. Every decision you make has a cause and effect while some lead you to fortune '
                'and others lead you to death.',
    install_requires=['pygame', 'colored', 'prettytable', 'pillow']
)
