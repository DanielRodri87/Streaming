import PySimpleGUI as sg

class Cadastro:
    def __init__(self) -> None:
        self.window = self.oimundo()
        
    def oimundo(self):
        sg.theme('Default1')
        layout = [
            [sg.Text('O cadastreo vai aqui')],
            [sg.Button('OK')]
        ]
        return sg.Window('Cadastrar', layout=layout, finalize=True)

    def show(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'OK':
                break
        self.window.close()