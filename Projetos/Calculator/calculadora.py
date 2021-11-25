# AlexXander28 github
# Calculadora Simples

import PySimpleGUI as sg


def aviso():
    # Sub Layout de aviso
    sg.theme('LightBrown13')
    layoutaviso = [
        [sg.Text('É impossível realizar esta operação. Modifique o segundo valor.')],
        [sg.Text('                                    '), sg.Button('OK', size=(6, 1))]
    ]
    # Sub Window de aviso
    janelaaviso = sg.Window('ATENÇÃO!', layoutaviso)
    # Sub Events de aviso
    while True:
        eventosaviso, valoresaviso = janelaaviso.Read()
        # print(eventosaviso, valoresaviso)
        if eventosaviso == 'OK':
            janelaaviso.Close()
        if eventosaviso == sg.WINDOW_CLOSED:
            break


# Layout
sg.theme('Reddit')
layout = [
    [sg.Button('C', size=(2, 2)), sg.Text(' Primeiro valor:'), sg.InputText('', key='primeiro', size=(20, 3))],
    [sg.Text('         Segundo valor:'), sg.InputText('', key='segundo', size=(20, 1))],
    [sg.Text('         '),
     sg.Button('√', size=(2, 1)), sg.Button('^', size=(2, 1)), sg.Button('+', size=(2, 1)),
     sg.Button('-', size=(2, 1)),
     sg.Button('x', size=(2, 1)), sg.Button('/', size=(2, 1)), sg.Button('%', size=(2, 1))],
    [sg.Text('               Resultado:'), sg.InputText('', key='resultado', size=(20, 1))]
]
# Window
janela = sg.Window('Calculadora Xander', layout)
# Events
while not sg.WINDOW_CLOSED:
    eventos, valores = janela.Read()
    if not valores['primeiro'].isnumeric():
        valores['primeiro'] = '0'
    if not valores['segundo'].isnumeric():
        valores['segundo'] = '0'
    if eventos == 'C':
        valores['primeiro'] = ''
        valores['segundo'] = ''
        valores['resultado'] = ''
    if eventos == '√':
        if float(valores['segundo']) != 0:
            valores['resultado'] = str(float(valores['primeiro']) ** (1 / float(valores['segundo'])))
        else:
            valores['segundo'] = ''
            aviso()
    elif eventos == '^':
        valores['resultado'] = str(float(valores['primeiro']) ** float(valores['segundo']))
    elif eventos == '+':
        valores['resultado'] = str(float(valores['primeiro']) + float(valores['segundo']))
    elif eventos == '-':
        valores['resultado'] = str(float(valores['primeiro']) - float(valores['segundo']))
    elif eventos == 'x':
        valores['resultado'] = str(float(valores['primeiro']) * float(valores['segundo']))
    elif eventos == '/':
        if float(valores['segundo']) != 0:
            valores['resultado'] = str(float(valores['primeiro']) / float(valores['segundo']))
        else:
            valores['segundo'] = ''
            aviso()
    elif eventos == '%':
        valores['resultado'] = str(float(valores['primeiro']) * (float(valores['segundo']) / 100))
    janela.Element('primeiro').Update(valores['primeiro'])
    janela.Element('segundo').Update(valores['segundo'])
    janela.Element('resultado').Update(valores['resultado'])
    # print(eventos, valores)
