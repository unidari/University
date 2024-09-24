{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOjbDmMfsBuDV20dJLvKN+W",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/unidari/University/blob/main/Extra_Tasks/Ex_task_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "2cn8472_pFwf"
      },
      "outputs": [],
      "source": [
        "d={}\n",
        "print('Консольное приложение // Телефонная книга')\n",
        "print('''Выберите номер функции:\n",
        "\n",
        " >>>> 1 > добавить контакт\n",
        " >>>> 2 > удалить контакт\n",
        " >>>> 3 > открыть телефонную книгу\n",
        " >>>> 4 > изменить номер телефона\n",
        " >>>> 5 > выход''')\n",
        "while True:\n",
        "  task=input('Введите номер функции: ')\n",
        "\n",
        "  if int(task)==5:\n",
        "    print('Выход')\n",
        "    break\n",
        "\n",
        "  elif int(task)==1:\n",
        "   name=input('Введите название для контакта: ').title()\n",
        "   if name in d.keys(): print('Контакт уже записан в телефонную книжку')\n",
        "   else:\n",
        "    nomerr=(input('Введите номер контакта (без +7): '))\n",
        "    if len((' '.join(nomerr)).split())<10:\n",
        "      print('Введите номер корректно с новой команды')\n",
        "    else:\n",
        "      d[name]='+'+'7'+nomerr\n",
        "      print('Контакт добавлен!')\n",
        "\n",
        "  elif int(task)==2:\n",
        "    udalit=input('Введите название контакта: ').title()\n",
        "    del d[udalit]\n",
        "    print('Контакт удалён!')\n",
        "\n",
        "  elif int(task)==3:\n",
        "    if bool(d)==False: print('Список контактов пуст')\n",
        "    else: print('Список контактов')\n",
        "    for key, value in sorted(d.items()):\n",
        "      print(key, value)\n",
        "\n",
        "  elif int(task)==4:\n",
        "    izmenit=input('Введите название контакта, у которого хотите изменить номер: ').title()\n",
        "    if izmenit not in d.keys(): print('Контакт не найден')\n",
        "    else:\n",
        "      nomer=(input('Введите номер контакта (без +7): '))\n",
        "      if len((' '.join(nomer)).split())<10:\n",
        "        print('Введите номер корректно с новой команды')\n",
        "      else:\n",
        "        d[izmenit]='+'+'7'+nomer\n",
        "        print('Номер контакта изменён!')"
      ]
    }
  ]
}