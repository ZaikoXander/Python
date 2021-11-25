import os
import PySimpleGUI as sg

total_size = 0
p = 0
while True:
    if p == 0:
        start_path = '%temp%'
    elif p == 1:
        start_path = '%userprofile%\AppData\LocalLow\Temp'
    elif p == 2:
        start_path = 'C:\Windows\Temp'
    else:
        start_path = 'C:\Windows\Prefetch'
    for path, dirs, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp) / 1000000000
    if p == 3:
        break
    p += 1
autor = f'{"By Xandinho":>80}'
sg.theme('Reddit')
layout = [
    [sg.Text(f'Temp folders size in your PC: {total_size:.6f} GB', font=('', 12), key='total_size')],
    [sg.Button('Cleanup', size=(16, 2)), sg.Text('', size=(17, 0), key='done')],
    [sg.Text(autor)]
]
# Window
janela = sg.Window('TFE', layout)
# Events
while True:
    eventos, valores = janela.Read()
    if eventos == 'Cleanup':
        os.system('del /f /s /q %temp%')
        os.system('del /f /s /q %userprofile%\AppData\LocalLow\Temp')
        os.system('del /f /s /q C:\Windows\Temp')
        os.system('del /f /s /q C:\Windows\Prefetch')
    total_size = 0
    while True:
        if p == 0:
            start_path = '%temp%'
        elif p == 1:
            start_path = '%userprofile%\AppData\LocalLow\Temp'
        elif p == 2:
            start_path = 'C:\Windows\Temp'
        else:
            start_path = 'C:\Windows\Prefetch'
        for path, dirs, files in os.walk(start_path):
            for f in files:
                fp = os.path.join(path, f)
                total_size += os.path.getsize(fp) / 1000000000
        if p == 3:
            break
        p += 1
    janela.Element('total_size').Update(f'Temp folders size in your PC: {total_size:.6f} GB')
    janela.Element('done').Update('  Work done!', font=('', 17), text_color='lightgreen')
    if eventos == sg.WINDOW_CLOSED:
        break
