import PySimpleGUI as sg
import os
import sys
from frontend.home import Home

class Program:
    def __init__(self):
        self.home = Home()

    def run(self):
        self.home.run()

if __name__ == "__main__":
    Program().run()
