{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMGZ70PGhDtpxHhR0NWikiT",
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
      "execution_count": 7,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X_zrJCWaAE5-",
        "outputId": "8e4175a3-32a1-46fa-c1b6-b9897de33c5f"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Введите число: 45\n",
            "Ваше число меньше!\n",
            "Введите число: 85\n",
            "Ваше число больше!\n",
            "Введите число: Выход\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "number=random.randint(0,100)\n",
        "print('Компьютер загадал число %s', number)\n",
        "m=0 # счётчик количества попыток\n",
        "while True:\n",
        "  d=input('Введите число: ')\n",
        "  m+=1\n",
        "  if d=='Выход' or not(int(number).isdigit()): break\n",
        "  elif int(d)==number:\n",
        "    print('Поздравляем! Вы угадали число за %s попытки!' % m)\n",
        "    break\n",
        "  elif int(d)>number: print('Ваше число больше!')\n",
        "  elif int(d)<number: print('Ваше число меньше!')\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "UYLYurJmC0wX"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
