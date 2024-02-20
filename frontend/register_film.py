import PySimpleGUI as sg

class Cadastro:
    def __init__(self) -> None:
        self.window = self.tela_cadastro()
        
    def tela_cadastro(self):
        sg.theme('Default1')
        layout = [
            [sg.Text('Nome do Filme/Série: '), sg.InputText('')],
            [sg.Text('Plataforma de Streaming: '), sg.InputText('')],
            [sg.Text('Gênero: '), sg.InputText('')],
            [sg.Text('Ano de Lançamento: '), sg.InputText('')],
            [sg.Text('Avaliação: '), sg.InputText('')],
        ]
        return sg.Window('Cadastrar', layout=layout, finalize=True, size=(600, 600))

    def show(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'OK':
                break
        self.window.close()