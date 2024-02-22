import PySimpleGUI as sg

class Cadastro:
    def __init__(self) -> None:
        self.window = self.tela_cadastro()
        
    def tela_cadastro(self):
        sg.theme('DefaultNoMoreNagging')
        layout = [
            [sg.Frame('Dados do cliente e entrega (obrigatório)',
                [
                    [sg.Text("Nome do Filme/Série: ", background_color="#e0e0e0")],
                    [sg.InputText(key="filme-serie", size=(115,2))],
                    [sg.Text("Plataforma de Streaming: ", background_color="#e0e0e0")],
                    [sg.InputText(key="-plataforma-", size=(115,2))],
                    [sg.Text("Gênero: ", background_color="#e0e0e0")],
                    [sg.InputText(key="-genero-", size=(115,2))],
                    [sg.Text("Duração do Filme:", background_color="#e0e0e0")],
                    [sg.InputText(key="-duracao-", size=(115,2), default_text="00:00:00")],
                    [sg.Text("Avalie com uma nota entre 1 e 5:", background_color="#e0e0e0")],
                    [sg.InputText(key="-nota-", size=(115,2))],
                    
                ], size=(800, 180), background_color="#e0e0e0"
            )],
        ]
        return sg.Window('Cadastrar', layout=layout, finalize=True, size=(600, 600))

    def show(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'OK':
                break
        self.window.close()