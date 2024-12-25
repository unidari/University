import os


def find_files(*args, option: int = 0):
    searching_for = tuple([*args])
    file_list = os.listdir(os.getcwd())
    file_nums = {}
    if option == 0:
        print(f'Поиск файлов с расширением {", ".join([*args])} в данном каталоге')
    match option:
        case 0:
            for i in file_list:
                if i.endswith(searching_for):
                    file_nums[len(file_nums) + 1] = i
                    print(str(len(file_nums)) + ': ' + i)
        case 1:
            for i in file_list:
                if i.startswith(searching_for):
                    file_nums[len(file_nums) + 1] = i
                    print(str(len(file_nums)) + ': ' + i)
        case 2:
            for i in file_list:
                end = i.rindex('.')
                if i[:end].endswith(searching_for):
                    file_nums[len(file_nums) + 1] = i
                    print(str(len(file_nums)) + ': ' + i)
        case 3:
            for i in file_list:
                end = i.rindex('.')
                for wanted in searching_for:
                    if wanted in i[:end]:
                        file_nums[len(file_nums) + 1] = i
                        print(str(len(file_nums)) + ': ' + i)
    if file_nums == {}:
        print('Файлы не найдены. Попробуйте другой каталог')
    return file_nums


def delete_files(option, substr):
    match option:
        case '1':
            for i in list(find_files(substr, option=1).values()):
                try:
                    os.remove(i)
                    print(f'Файл {i} удален успешно')
                except PermissionError:
                    print('Недостаточно прав для удаления!')
        case '2':
            for i in list(find_files(substr, option=2).values()):
                try:
                    os.remove(i)
                    print(f'Файл {i} удален успешно')
                except PermissionError:
                    print('Недостаточно прав для удаления!')
        case '3':
            for i in list(find_files(substr, option=3).values()):
                try:
                    os.remove(i)
                    print(f'Файл {i} удален успешно')
                except PermissionError:
                    print('Недостаточно прав для удаления!')

        case '4':
            if not substr.startswith('.'):
                substr = '.' + substr
            for i in list(find_files(substr, option=0).values()):
                try:
                    os.remove(i)
                    print(f'Файл {i} удален успешно')
                except PermissionError:
                    print('Недостаточно прав для удаления!')


def current_directory():
    return os.getcwd()
