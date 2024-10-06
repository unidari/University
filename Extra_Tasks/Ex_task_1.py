{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO+1YgvQZOOWbfKACuZovga",
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
        "<a href=\"https://colab.research.google.com/github/unidari/University/blob/main/Extra_Tasks/Ex_task_1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H5uJQ4l7VvTD",
        "outputId": "e7725321-ab0b-4e19-e11e-71c39cce3c4a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Компьютер загадал число 48\n",
            "Введите число: iegfwf\n",
            "Введите число, пожалуйста\n",
            "Введите число: 67\n",
            "Ваше число больше!\n",
            "Введите число: 100\n",
            "Ваше число больше!\n",
            "Введите число: 76\n",
            "Ваше число больше!\n",
            "Введите число: 48\n",
            "Поздравляем! Вы угадали число за 4 попытки!\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "m=0 # счётчик количества попыток\n",
        "number=random.randint(0,100)\n",
        "print(f'Компьютер загадал число {number}')\n",
        "while True:\n",
        "  d=input('Введите число: ')\n",
        "  if d.lower()=='выход':\n",
        "    break\n",
        "  if not(d.isdigit()):\n",
        "    print('Введите число, пожалуйста')\n",
        "    continue\n",
        "  m+=1\n",
        "  d=int(d)\n",
        "  if d==number:\n",
        "    print(f'Поздравляем! Вы угадали число за {m} попытки!')\n",
        "    break\n",
        "  elif d>number: print('Ваше число больше!')\n",
        "  elif d<number: print('Ваше число меньше!')"
      ]
    }
  ]
}