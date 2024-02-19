import PySimpleGUI as sg
import os
import sys
from frontend.home import Home

class Program:
    def __init__(self):
        self.home = Home()  

    def run(self):
        self.home.start()  
        self.home.close()  
        sys.exit()

if __name__ == "__main__":
    Program().run() 
