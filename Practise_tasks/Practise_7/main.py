import os
import PySimpleGUI as sg
from pdf2docx import Converter
from docx2pdf import convert
from PIL import Image

def compress_image(file, quality):
    img = Image.open(file)
    img.save(file, optimize=True, quality=quality)
    return f"Изображение {file} сжато с качеством {quality}%"

def pdf_to_docx(file):
    docx_file = file.replace('.pdf', '.docx')
    cv = Converter(file)
    cv.convert(docx_file)
    cv.close()
    return f"Файл {file} преобразован в {docx_file}."

def docx_to_pdf(file):
    convert(file)
    return f"Файл {file} преобразован в PDF."

layout = [
    [sg.Text("Выберите папку"), sg.Input(key="-FOLDER-", enable_events=True), sg.FolderBrowse()],
    [sg.Listbox(values=[], enable_events=True, size=(50, 10), key="-FILE LIST-")],
    [sg.Button("Преобразовать PDF в DOCX"), sg.Button("Преобразовать DOCX в PDF"), sg.Button("Сжать изображения"), sg.Exit()]
]

window = sg.Window("Office Tweaks", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            file_list = os.listdir(folder)
        except FileNotFoundError:
            file_list = []
        files = [f for f in file_list if os.path.isfile(os.path.join(folder, f))]
        window["-FILE LIST-"].update(files)
    elif event == "-FILE LIST-":
        selected_files = values["-FILE LIST-"]
    elif event == "Преобразовать PDF в DOCX":
        for file in selected_files:
            if file.endswith(".pdf"):
                result = pdf_to_docx(os.path.join(folder, file))
                sg.popup(result)
    elif event == "Преобразовать DOCX в PDF":
        for file in selected_files:
            if file.endswith(".docx"):
                result = docx_to_pdf(os.path.join(folder, file))
                sg.popup(result)
    elif event == "Сжать изображения":
        for file in selected_files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                result = compress_image(os.path.join(folder, file), quality=50)
                sg.popup(result)

window.close()
