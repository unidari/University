{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPGYigMVrMgf185F89Us2xi",
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
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dZ6wf4DWyCax",
        "outputId": "a9b5e1cd-9d30-4f9f-91d6-e19904081b12"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1. Добавить контакт\n",
            "2. Удалить контакт\n",
            "3. Показать контакты\n",
            "4. Изменить номер\n",
            "5. Выход\n",
            "\n",
            "Выберите опцию: 1\n",
            "Введите имяДаша\n",
            "Введите телефон9153373501\n",
            "1. Добавить контакт\n",
            "2. Удалить контакт\n",
            "3. Показать контакты\n",
            "4. Изменить номер\n",
            "5. Выход\n",
            "\n",
            "Выберите опцию: 3\n",
            "Даша +79153373501\n",
            "1. Добавить контакт\n",
            "2. Удалить контакт\n",
            "3. Показать контакты\n",
            "4. Изменить номер\n",
            "5. Выход\n",
            "\n",
            "Выберите опцию: 2\n",
            "Введите имяДаша\n",
            "1. Добавить контакт\n",
            "2. Удалить контакт\n",
            "3. Показать контакты\n",
            "4. Изменить номер\n",
            "5. Выход\n",
            "\n",
            "Выберите опцию: 3\n",
            "Контактов нет\n",
            "1. Добавить контакт\n",
            "2. Удалить контакт\n",
            "3. Показать контакты\n",
            "4. Изменить номер\n",
            "5. Выход\n",
            "\n",
            "Выберите опцию: 5\n"
          ]
        }
      ],
      "source": [
        "contact = {}\n",
        "\n",
        "def replace_name(name: str) -> str:\n",
        "    return name.capitalize()\n",
        "\n",
        "def replace_phone(phone: str) -> str:\n",
        "    if len(phone) < 10: return \"Неправильный номер\"\n",
        "\n",
        "    if len(phone) == 11:\n",
        "        return phone.replace(phone[0], '+7', 1)\n",
        "\n",
        "    return '+7' + phone\n",
        "\n",
        "\n",
        "\n",
        "def add(name: str, phone: str):\n",
        "    name = replace_name(name)\n",
        "    phone = replace_phone(phone)\n",
        "    contact[name] = phone\n",
        "\n",
        "def delete_contact(name: str):\n",
        "    del contact[name]\n",
        "\n",
        "def view():\n",
        "    if len(contact) == 0:\n",
        "        print(\"Контактов нет\")\n",
        "        pass\n",
        "\n",
        "    for user in contact.items():\n",
        "        print(' '.join(user))\n",
        "\n",
        "def edit(name: str, phone: str) -> dict:\n",
        "    if name not in contact:\n",
        "      print('Контакта нет')\n",
        "      return contact\n",
        "\n",
        "    sname = replace_name(name)\n",
        "    sphone = replace_phone(phone)\n",
        "\n",
        "    contact[sname] = sphone\n",
        "    return contact\n",
        "\n",
        "\n",
        "while True:\n",
        "    print('\\n'.join([\"1. Добавить контакт\", \"2. Удалить контакт\", \"3. Показать контакты\", \"4. Изменить номер\", \"5. Выход\"]))\n",
        "    option = input(\"\\nВыберите опцию: \")\n",
        "\n",
        "    if not option.isdigit():\n",
        "        continue\n",
        "\n",
        "    if int(option) not in [1, 2, 3, 4, 5]:\n",
        "        continue\n",
        "\n",
        "    if int(option) == 1:\n",
        "      add(input('Введите имя'), input('Введите телефон'))\n",
        "\n",
        "    elif int(option) == 2:\n",
        "      delete_contact(input('Введите имя'))\n",
        "\n",
        "    elif int(option) == 3:\n",
        "      view()\n",
        "\n",
        "    elif int(option) == 4:\n",
        "      edit(input('Введите имя'), input('Введите телефон'))\n",
        "\n",
        "    else:\n",
        "      break\n"
      ]
    }
  ]
}