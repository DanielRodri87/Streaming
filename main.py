import PySimpleGUI as sg
import os
import sys
from frontend.home import Home

class Program:
    def __init__(self):
        self.home = Home()  

    def run(self):
        window = self.home.menu_principal()  
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
        window.close()  
        sys.exit()

if __name__ == "__main__":
    Program().run()