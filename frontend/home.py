import PySimpleGUI as sg

class Home:
    def menu_principal(self):
        sg.theme('Default1')

        layout = [
            [sg.Frame('', 
                [
                    [
                        sg.Button("Castrar Filme", font=(None, 8), size=(11, 2), pad=(2, 0)),
                        sg.Button("Listar Filmes", font=(None, 8), size=(11, 2), pad=(2, 0)),
                        sg.Button("Editar Filme", font=(None, 8), size=(11, 2), pad=(2, 0)),
                        sg.Button("Deletar Filme", font=(None, 8), size=(11, 2), pad=(2, 0)),
                    ],
                ], border_width=2, background_color="#181818", size=(1366, 115), pad=(0,0), element_justification="left")
            ],
            [sg.Image(filename="img\\foto.png", size=(500, 500), key="foto")],
            [sg.Text("Um produto desenvolvido por Daniel e Francinaldo® e licenciado para Pobre Flix.\nTelefone para suporte: 4002-8922\ndaniel.sousa @ufpi.edu.br e colocaemailaquinaldo@gmail.com", 
                font=(None, 10), justification="center", size=(1366, 3), pad=(2, 0))
            ]
        ]
        return sg.Window("PobreFlix", layout=layout, finalize=True, resizable=True, size=(1366,768), margins=(0,0))
