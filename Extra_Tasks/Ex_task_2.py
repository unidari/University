{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPa/rYxGpE6sX51UEqvq9lI",
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
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zaWfp0OCbD3g",
        "outputId": "350b6bd0-e3bd-4888-cc19-32f7aaec543b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Консольное приложение // Телефонная книга\n",
            "Выберите номер функции:\n",
            "\n",
            " >>>> 1 > добавить контакт\n",
            " >>>> 2 > удалить контакт\n",
            " >>>> 3 > открыть телефонную книгу\n",
            " >>>> 4 > изменить номер телефона\n",
            " >>>> 5 > выход\n",
            "Введите номер функции: 1\n",
            "Введите название для контакта: lk\n",
            "Введите номер контакта (без +7): 5623985647\n",
            "Контакт добавлен!\n",
            "Введите номер функции: 4\n",
            "Введите название контакта, у которого хотите изменить номер: lk\n",
            "Введите номер контакта (без +7): lk\n",
            "Ведите номер телефона в виде цифр (без +7): uj\n",
            "Ведите номер телефона в виде цифр (без +7): 854\n",
            "Введите номер корректно (в виде цифр и длиной в 10 символов): 1236547895\n",
            "Контакт добавлен!\n",
            "Номер контакта изменён!\n",
            "Введите номер функции: 5\n",
            "Выход\n"
          ]
        }
      ],
      "source": [
        "d = {}\n",
        "print('Консольное приложение // Телефонная книга')\n",
        "print('''Выберите номер функции:\n",
        "\n",
        " >>>> 1 > добавить контакт\n",
        " >>>> 2 > удалить контакт\n",
        " >>>> 3 > открыть телефонную книгу\n",
        " >>>> 4 > изменить номер телефона\n",
        " >>>> 5 > выход''')\n",
        "\n",
        "commands=['1','2','3','4','5']\n",
        "def nomer_(nomerr):\n",
        "  while not(nomerr.isdigit()):\n",
        "    nomerr=input('Ведите номер телефона в виде цифр (без +7): ')\n",
        "    continue\n",
        "  while len([i for i in nomerr]) < 10:\n",
        "    nomerr=input('Введите номер корректно (в виде цифр и длиной в 10 символов): ')\n",
        "  else:\n",
        "    d[name] = '+' + '7' + nomerr\n",
        "\n",
        "while True:\n",
        "    task = input('Введите номер функции: ')\n",
        "\n",
        "    if task not in commands:\n",
        "      while True:\n",
        "        task=input('Введите допустимую функцию: ')\n",
        "        continue\n",
        "\n",
        "    if task==commands[4]:\n",
        "        print('Выход')\n",
        "        break\n",
        "\n",
        "    elif task==commands[0]:\n",
        "        name = input('Введите название для контакта: ').title()\n",
        "        if name in d.keys(): print('Контакт уже записан в телефонную книжку')\n",
        "        else:\n",
        "          nomerr = input('Введите номер контакта (без +7): ')\n",
        "          nomer_(nomerr)\n",
        "          print('Контакт добавлен!')\n",
        "\n",
        "    elif task==commands[1]:\n",
        "        udalit = input('Введите название контакта: ').title()\n",
        "        while udalit not in d.keys():\n",
        "          udalit=input('''Такой контакт не записан в вашей книге\n",
        "          Введите существующий контакт: ''').title()\n",
        "        else:\n",
        "          del d[udalit]\n",
        "          print('Контакт удалён!')\n",
        "\n",
        "    elif task==commands[2]:\n",
        "        if not d:\n",
        "            print('Список контактов пуст')\n",
        "        else:\n",
        "            print('Список контактов')\n",
        "        for key, value in sorted(d.items()):\n",
        "            print(key, value)\n",
        "\n",
        "    elif task==commands[3]:\n",
        "        izmenit = input('Введите название контакта, у которого хотите изменить номер: ').title()\n",
        "        if izmenit not in d.keys(): print('Контакт не найден')\n",
        "        else:\n",
        "          nomer = input('Введите номер контакта (без +7): ')\n",
        "          nomer_(nomer)\n",
        "          print('Номер контакта изменён!')\n",
        "\n"
      ]
    }
  ]
}