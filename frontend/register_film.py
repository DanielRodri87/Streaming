import PySimpleGUI as sg

class Cadastro:
    def __init__(self) -> None:
        self.window = self.tela_cadastro()
        
    def tela_cadastro(self):
        sg.theme('Default1')  
        layout = [
            [sg.Text("Cadastro de Filme/Série", font=('Helvetica', 20), justification='center')],
            [sg.Text('_' * 100, justification='center')],
            [sg.Text("Nome do Filme/Série: ", size=(15, 1)), 
             sg.InputText(key="filme-serie", size=(50, 1))],
            [sg.Text("Plataforma de Streaming: ", size=(15, 1)), 
             sg.InputText(key="-plataforma-", size=(50, 1))],
            [sg.Text("Gênero: ", size=(15, 1)), 
             sg.InputText(key="-genero-", size=(50, 1))],
            [sg.Text("Duração do Filme:", size=(15, 1)), 
             sg.InputText(key="-duracao-", size=(50, 1), default_text="00:00:00")],
            [sg.Text("Avalie com uma nota entre 1 e 5:", size=(15, 1)), 
             sg.InputText(key="-nota-", size=(50, 1))],
            [sg.Button("Enviar", size=(10, 2), key="enviar"),
             sg.Button("Cancelar", size=(10, 2), key="cancelar")],
        ]
        return sg.Window('Cadastrar', layout=layout, finalize=True, size=(600, 350))

    def show(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED or event == 'enviar' or event == 'cancelar':
                break
        self.window.close()
        
if __name__ == "__main__":
    Cadastro().show()
