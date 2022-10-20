import PySimpleGUI as sg

layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('loguin')],
    [sg.Text('', key='mensagem')]
]

window = sg.Window('loguin', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'loguin':
        senha_correta = '123456'
        usuario_correto = 'Macena'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('loguin feito com sucesso')
        else: window['mensagem'].update('senha ou usuario incorreto')