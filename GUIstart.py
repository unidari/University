import PySimpleGUI as sg


import Functions.compress_image
import Functions.file_manager
import Functions.pdf_docx


def checkFormats(dirc):
    fl1 = 0
    fl2 = 0
    fl3 = 0
    for i in [*values.get(dirc)]:
        img_finder = ('.png', '.jpg', '.jpeg', '.gif')
        if i.endswith(img_finder) and fl3 == 0:
            fl3 = 1
        if i.endswith('.pdf') and fl1 == 0:
            fl1 = 1
        if i.endswith('.docx') and fl2 == 0:
            fl2 = 1
    if fl1 + fl2 + fl3 == 1:
        if fl1:
            return 1
        elif fl2:
            return 2
        elif fl3:
            return 3
        else:  # failsafe
            return 0
    else:
        return 0

def pdftodocx(option, docs):
    try:
        Functions.pdf_docx.pdf_to_docx(option, docs)
        sg.popup('Успешно!')
    except:
        sg.popup('Произошла ошибка!')


def docxtopdf(option, docs):
    try:
        Functions.pdf_docx.docx_to_pdf(option, docs)
        sg.popup('Успешно!')
    except:
        sg.popup('Произошла ошибка!')


def compress_img(option, images, compression):
    try:
        Functions.compress_image.compress_img(option, images, compression)
        if int(compression) not in range(1,101):
            raise Exception
        sg.popup('Успешно!')
    except:
        sg.popup('Произошла ошибка!')

def delFiles(substr, type):
    try:
        if Functions.file_manager.find_files(substr, type=type) != {}:
            Functions.file_manager.delete_files(str(type), substr)
            sg.popup('Успешно!')
        else:
            sg.popup('Файлы не найдены!')
    except:
        sg.popup('Произошла ошибка!')


def create_delete_window():
    sg.theme('DarkPurple4')
    del_layout = [
        [sg.Radio('Удалить все файлы начинающиеся на введенную подстроку', "doption")],
        [sg.Radio('Удалить все файлы оканчивающиеся на введенную подстроку', "doption")],
        [sg.Radio('Удалить все файлы содержащие введенную подстроку', "doption")],
        [sg.Radio('Удалить файлы по расширению', "doption")],
        [sg.Text('Подстрока'), sg.InputText(key='substr')],
        [sg.Button('Продолжить'), sg.Button('Выйти')]
    ]
    return sg.Window('Окно удаления', del_layout, finalize=True, icon='thumbnail.ico')


def create_selection_window():
    sg.theme('DarkPurple4')
    sel_layout = [
        [sg.Radio('Выбрать все подходящие файлы', "soption")],
        [sg.Radio('Выбрать только выделенные файлы', "soption")],
        [sg.Text('Выберите степень сжатия (1-100, наиб.- наим.)', visible=False, key='comptxt'), sg.Spin(values=[i for i in range(1, 101)], visible=False, initial_value=1, key='compression')],
        [sg.Button('Продолжить'), sg.Button('Выйти')]
    ]
    return sg.Window('Окно выбора', sel_layout, finalize=True, icon='thumbnail.ico')

sg.theme('DarkPurple4')
layout_left = [
    [sg.Text(f"Рабочий каталог: "), sg.Text(Functions.file_manager.current_directory(), key='dirtext'), sg.Button('Выбрать каталог')],
    [sg.Listbox(values=[], select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED, enable_events=True, size=(60, 20), key='file_dir')],
    [sg.Button('Выход')]
]
layout_right = [
    [sg.Text('Выберите функцию')],
    [sg.Button('Преобразовать PDF в Docx', key='option1', disabled=True)],
    [sg.Button('Преобразовать Docx в PDF', key='option2', disabled=True)],
    [sg.Button('Произвести сжатие изображений', key='option3', disabled=True)],
    [sg.Button('Удалить группу файлов', key='option4')]
]
layout = [[sg.Column(layout_left), sg.VSeperator(), sg.Column(layout_right)]]

main_window, del_win, sel_win = sg.Window('Основное окно', layout, finalize=True, icon='thumbnail.ico'), None, None
main_window['file_dir'].update(Functions.file_manager.os.listdir())
flag = 0
while True:
    window, event, values = sg.read_all_windows()
    if window == main_window and event in (sg.WINDOW_CLOSED, 'Выход'):
        break
    elif window == main_window and event == 'Выбрать каталог':
        try:
            Functions.file_manager.os.chdir(sg.popup_get_folder('Выберите папку', title='Выбор папки'))
            main_window['dirtext'].update(Functions.file_manager.current_directory())
            main_window['file_dir'].update('')
            main_window['file_dir'].update(Functions.file_manager.os.listdir())
        except TypeError:
            pass
        except:
            sg.popup('Произошла ошибка!')
    elif window == main_window and event == 'file_dir':
        sel_files = values.get('file_dir')
        main_window['option1'].update(disabled=True)
        main_window['option2'].update(disabled=True)
        main_window['option3'].update(disabled=True)
        if checkFormats('file_dir') > 0:
            flag = checkFormats('file_dir')
            if flag == 1:
                main_window['option1'].update(disabled=False)
            elif flag == 2:
                main_window['option2'].update(disabled=False)
            elif flag == 3:
                main_window['option3'].update(disabled=False)
    elif window == main_window and event == 'option1':
        sel_win = create_selection_window()
    elif window == main_window and event == 'option2':
        sel_win = create_selection_window()
    elif window == main_window and event == 'option3':
        sel_win = create_selection_window()
        sel_win['comptxt'].update(visible=True)
        sel_win['compression'].update(visible=True)
    elif window == main_window and event == 'option4':
        del_win = create_delete_window()
    elif window == del_win and event in (sg.WINDOW_CLOSED, 'Выйти'):
        del_win.close()
    elif window == del_win and event == 'Продолжить':
        if values[0]:
            delFiles(values['substr'], 1)
        elif values[1]:
            delFiles(values['substr'], 2)
        elif values[2]:
            delFiles(values['substr'], 3)
        elif values[3]:
            delFiles(values['substr'], 0)
        main_window['file_dir'].update(Functions.file_manager.os.listdir())
    elif window == sel_win and event in (sg.WINDOW_CLOSED, 'Выйти'):
        sel_win.close()
    elif window == sel_win and event == 'Продолжить' and values[0] or values[1]:
        if flag == 1:
            if values[0]:
                pdftodocx('0', Functions.file_manager.find_files('.pdf', type=0))
            else:
                pdftodocx('1', sel_files)
        elif flag == 2:
            if values[0]:
                docxtopdf('0', Functions.file_manager.find_files('.docx', type=0))
            else:
                docxtopdf('1', sel_files)
        elif flag == 3:
            if values[0]:
                compress_img('0', Functions.file_manager.find_files('.jpg', '.jpeg', '.gif', '.png', type=0), values['compression'])
            else:
                compress_img('1', sel_files, values['compression'])
        main_window['file_dir'].update(Functions.file_manager.os.listdir())

main_window.close()