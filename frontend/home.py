import PySimpleGUI as sg
from frontend.register_film import Cadastro

class Home:
    def __init__(self):
        self.window = self.main_menu()

    def main_menu(self):
        sg.theme('Default1')

        layout = [
            [sg.Frame('',
                [
                    [
                        sg.Button("Cadastrar Filme", font=(None, 8), size=(11, 2), pad=(2, 0), key="cadastrar_filme"),
                        sg.Button("Listar Filmes", font=(None, 8), size=(11, 2), pad=(2, 0), key="listar_filmes"),
                        sg.Button("Editar Filme", font=(None, 8), size=(11, 2), pad=(2, 0), key="editar_filme"),
                        sg.Button("Deletar Filme", font=(None, 8), size=(11, 2), pad=(2, 0), key="deletar_filme"),
                        sg.Button("Sair", font=(None, 8), size=(11, 2), pad=(2, 0), key="sair"),
                    ],
                ], border_width=2, background_color="#181818", size=(1366, 115), pad=(0,0), element_justification="center"
            )],
            [sg.Text("Um produto desenvolvido por Daniel e Francinaldo® e licenciado para Pobre Flix.\nTelefone para suporte: 4002-8922\ndaniel.sousa @ufpi.edu.br e colocaemailaquinaldo@gmail.com",
                font=(None, 10), justification="center", size=(1366, 3), pad=(2, 0))
            ]
        ]
        return sg.Window("PobreFlix", layout=layout, finalize=True, resizable=True, size=(1366,768), margins=(0,0))

    def run(self):
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == "cadastrar_filme":
                Cadastro().show()  # Aqui chamamos a tela de cadastro
            elif event == "listar_filmes":
                pass
            elif event == "editar_filme":
                pass
            elif event == "deletar_filme":
                pass
            elif event == "sair":
                self.window.close()

        self.window.close()

if __name__ == "__main__":
    Home().run()
