import PySimpleGUI as sg

class Home:
    def __init__(self):
        self.window = self.menu_principal()

    def menu_principal(self):
        sg.theme('Default1')

        layout = [
            [sg.Frame('', 
                [], border_width=2, background_color="#EEAD2D", size=(1366, 115), pad=(0,0), element_justification="left")],
        

            [sg.Text("Um produto desenvolvido por Daniel® e licenciado para Pobre Flix.\nTelefone para suporte: 0800-000-1234\ndaniel.sousa@ufpi.edu.br", 
                font=(None, 10), justification="center", size=(1366, 3), pad=(2, 0))]
        ]
        return sg.Window("Pobre Flix", layout, size=(1366, 768), element_justification="center", finalize=True)
    def start(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == "Sair":
                break
            if event == "Entrar":
                self.window.close()
                break
        return "Start"

    def close(self):
        self.window.close()
