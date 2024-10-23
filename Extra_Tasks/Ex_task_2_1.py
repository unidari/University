{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/github/unidari/University/blob/main/Extra_Tasks/Ex_task_2_1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### **Дополнительное задание №2.1**"
      ],
      "metadata": {
        "id": "AFKOdzjAKWYc"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "**Пункт 1:**\n",
        "\n",
        "Напишите программу, которая принимает список строк, содержащих числа, и преобраует их в список целых чисел, возведённых в куб. Используйте функции `map()` и `lambda`.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "numbers = ['1', '2', '3', '4', '5']\n",
        "\n",
        "# Ожидаемый результат\n",
        "[1, 8, 27, 64, 125]\n",
        "```"
      ],
      "metadata": {
        "id": "qIQeFXOZKtlE"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numbers = [(lambda x: str(i))(i) for i in input().split()]\n",
        "cube = map(lambda x: int(x) ** 3, numbers)\n",
        "print(list(cube))"
      ],
      "metadata": {
        "id": "g4gpq3TwKus0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "a9e0b886-bdee-4df4-e590-24c8425f217a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 4 5\n",
            "[1, 8, 27, 64, 125]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "**Пункт 2:**\n",
        "\n",
        "Используя `filter()` и `lambda`, из списка слов отфильтруйте только те, которые начинаются и заканчиваются на одну и ту же букву.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "words = ['level', 'python', 'radar', 'world', 'rotor']\n",
        "\n",
        "# Ожидаемый результат\n",
        "['level', 'radar', 'rotor']\n",
        "```"
      ],
      "metadata": {
        "id": "L86Zyn5OK0FW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "words = numbers = [(lambda x: str(i))(i) for i in input().split()]\n",
        "first_last = filter(lambda x: x[0]==x[-1], words)\n",
        "print(list(first_last))"
      ],
      "metadata": {
        "id": "k0-9uu2iK45z",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6b6e8f02-7c26-4680-90b4-12baebc70719"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "level python radar world rotor\n",
            "['level', 'radar', 'rotor']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "**Пункт 3:**\n",
        "\n",
        "С помощью `reduce()` и `lambda` найдите наибольшее число в списке чисел.\n",
        "\n",
        "**Подсказка:** Функция `reduce()` находится в модуле `functools`.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "numbers = [47, 11, 42, 102, 13]\n",
        "\n",
        "# Ожидаемый результат\n",
        "102\n",
        "```"
      ],
      "metadata": {
        "id": "ppIY_xrQK5ZT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from functools import reduce\n",
        "numbers = numbers = [(lambda x: int(i))(i) for i in input().split()]\n",
        "maximum = reduce(lambda x, y: y if (x<y) else x, numbers)\n",
        "print(maximum)"
      ],
      "metadata": {
        "id": "Gl9iHqHuK6Gp",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "60ea3ee1-1bb7-40b9-f7c7-7ec8ce10a17e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "47 11 42 102 13\n",
            "102\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "**Пункт 4:**\n",
        "\n",
        "Объедините два списка чисел в один список кортежей, где каждый кортеж состоит из элементов исходных списков, возведённых в квадрат и куб соответственно. Используйте функции `map()`, `lambda` и `zip()`.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "list1 = [1, 2, 3]\n",
        "list2 = [4, 5, 6]\n",
        "\n",
        "# Ожидаемый результат\n",
        "[(1, 64), (4, 125), (9, 216)]\n",
        "```"
      ],
      "metadata": {
        "id": "J_wCDrsHK8Rr"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "list1 = [(lambda x: int(i))(i) for i in input().split()]\n",
        "list2 = [(lambda x: int(i))(i) for i in input().split()]\n",
        "union = zip(list(map(lambda x: x**2, list1)), list(map(lambda x: x**3, list2)))\n",
        "print(list(union))"
      ],
      "metadata": {
        "id": "D9mval4GK9PB",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "93da50ee-9edf-4924-cfd5-b68557f120bf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3\n",
            "4 5 6\n",
            "[(1, 64), (4, 125), (9, 216)]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "**Пункт 5:**\n",
        "\n",
        "Напишите программу, которая принимает строку с целыми числами, разделёнными запятыми, и вычисляет сумму чётных чисел из этой строки. Используйте функции `map()`, `filter()`, `lambda` и `reduce()`.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "numbers = '1,2,3,4,5,6,7,8,9,10'\n",
        "\n",
        "# Ожидаемый результат\n",
        "30  # (2 + 4 + 6 + 8 + 10)\n",
        "```"
      ],
      "metadata": {
        "id": "6S0zCchALAAc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numbers = [(lambda x: str(i))(i) for i in input().split(',')]\n",
        "summa=reduce(lambda x,y: x+y, list(filter(lambda x: x if x%2==0 else None, list(map(lambda x: int(x), numbers)))))\n",
        "print(summa)"
      ],
      "metadata": {
        "id": "GSxOpO5CLDN2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "56ed810a-56a9-42ff-e1a9-18cb3da9b0bf"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1,2,3,4,5,6,7,8,9,10\n",
            "30\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "---\n",
        "\n",
        "**Пункт 6:**\n",
        "\n",
        "Используя `map()` и `lambda`, преобрауйте список температур в граусах ельсия в список температур в граусах Фаренгейта. Формула преобраования: F = C * 9/5 + 32.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "celsius = [0, 15, 30, 100]\n",
        "\n",
        "# Ожидаемый результат\n",
        "[32.0, 59.0, 86.0, 212.0]\n",
        "```"
      ],
      "metadata": {
        "id": "XnZG4q22LCSU"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "celsius =[(lambda x: int(i))(i) for i in input().split()]\n",
        "farg= map(lambda x: (x*9)/5+32, celsius)\n",
        "print(list(farg))"
      ],
      "metadata": {
        "id": "A03mTrhNLC06",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ce92061d-e2c2-4183-8f94-f6e360387c44"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0 15 30 100\n",
            "[32.0, 59.0, 86.0, 212.0]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "**Пункт 7:**\n",
        "\n",
        "У вас есть список чисел. Используя комбинацию функций `filter()`, `map()` и `lambda`, получите новый список, содержащий квадраты нечётных чисел из исходного списка.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]\n",
        "\n",
        "# Ожидаемый результат\n",
        "[1, 9, 25, 49, 81]\n",
        "```\n",
        "\n"
      ],
      "metadata": {
        "id": "r-fsnwuhLFXg"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numbers = [(lambda x: int(i))(i) for i in input().split()]\n",
        "squa= map(lambda x: x**2, list(filter(lambda x: x if x%2!=0 else None, numbers)))\n",
        "print(list(squa))"
      ],
      "metadata": {
        "id": "ZV0oNPqlLose",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d246dc6d-57df-4dba-f5a1-224c0b4807e0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 4 5 6 7 8 9\n",
            "[1, 9, 25, 49, 81]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "**Пункт 8:**\n",
        "\n",
        "С помощью функции `reduce()` и `lambda` вычислите произведение всех чисел в списке.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "numbers = [1, 2, 3, 4, 5]\n",
        "\n",
        "# Ожидаемый результат\n",
        "120  # (1 * 2 * 3 * 4 * 5)\n",
        "```"
      ],
      "metadata": {
        "id": "Rvn8FWnmLHOP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "numbers = [(lambda x: int(i))(i) for i in input().split()]\n",
        "proiz = reduce(lambda x,y: x*y, numbers)\n",
        "print(proiz)"
      ],
      "metadata": {
        "id": "_J-9EEJwLJk-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "10628724-affa-4f03-8278-54d790e8fa13"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 4 5\n",
            "120\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "**Пункт 9:**\n",
        "\n",
        "Дан список строковых представлений чисел. Используя `map()`, `lambda` и метод строки `isdigit()`, преобрауйте список, заменив нечисловые строки на число 0.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "strings = ['10', '20', 'abc', '30', 'def']\n",
        "\n",
        "# Ожидаемый результат\n",
        "[10, 20, 0, 30, 0]\n",
        "```"
      ],
      "metadata": {
        "id": "_BXHdCrfLJtd"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "strings = [(lambda x: str(i))(i) for i in input().split()]\n",
        "otvet = map(lambda x: int(x) if x.isdigit() else 0, strings)\n",
        "print(list(otvet))"
      ],
      "metadata": {
        "id": "uOLoUIMmLLwG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6aba5a0b-ba65-40ee-86ff-bc5b8ccdd23a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 20 abs 30 def\n",
            "[10, 20, 0, 30, 0]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "**Пункт 10:**\n",
        "\n",
        "Есть два списка координат X и Y одинаковой длины. Используя `zip()` и `lambda`, объедините их в список точек — кортежей `(x, y)`.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "x_coords = [1, 2, 3]\n",
        "y_coords = [4, 5, 6]\n",
        "\n",
        "# Ожидаемый результат\n",
        "[(1, 4), (2, 5), (3, 6)]\n",
        "```"
      ],
      "metadata": {
        "id": "DovAPjnhLL3i"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x_coords = [(lambda x: int(x))(i) for i in input().split()]\n",
        "y_coords = [(lambda x: int(x))(i) for i in input().split()]\n",
        "coords = zip(x_coords, y_coords)\n",
        "print(list(coords))"
      ],
      "metadata": {
        "id": "BhyGHMK4LPey",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "335646a4-c0ca-4cfd-8a0b-d2f4b3093235"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3\n",
            "4 5 6\n",
            "[(1, 4), (2, 5), (3, 6)]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "**Пункт 11:**\n",
        "\n",
        "Напишите программу, которая принимает список слов и возвращает словарь, где ключами являются слова, а значениями — длины этих слов. Используйте `map()` и `lambda`.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "words = ['apple', 'banana', 'cherry']\n",
        "\n",
        "# Ожидаемый результат\n",
        "{'apple': 5, 'banana': 6, 'cherry': 6}\n",
        "```"
      ],
      "metadata": {
        "id": "56GJYuVCLOrF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "d={}\n",
        "words = [(lambda x: str(i))(i) for i in input().split()]\n",
        "values=list(map(lambda x: len(x), words))\n",
        "for word in words:\n",
        "  if len(word) in values:\n",
        "    d[word]=len(word)\n",
        "    continue\n",
        "print(d)"
      ],
      "metadata": {
        "id": "8dSc6w2DLS72",
        "outputId": "de557c93-8d22-42e0-be28-485a3f047e39",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "apple banana cherry\n",
            "{'apple': 5, 'banana': 6, 'cherry': 6}\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "**Пункт 12:**\n",
        "\n",
        "Используя `filter()` и `lambda`, из списка чисел оставьте только простые числа.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]\n",
        "\n",
        "# Ожидаемый результат\n",
        "[2, 3, 5, 7]\n",
        "```\n",
        "\n",
        "*Подсказка:* Для проверки числа на простоту может понадобиться дополнительная функция.\n"
      ],
      "metadata": {
        "id": "HJ3Yi_p1LRvV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def f(n):\n",
        "  c=0\n",
        "  for i in range (2, int(n**0.5)+1):\n",
        "    if n%i==0: c+=1\n",
        "  if c==0: return 1\n",
        "  else: return 0\n",
        "numbers = [(lambda x: int(i))(i) for i in input().split()]\n",
        "otvet = filter(lambda x: x if f(x)==1 else None, numbers)\n",
        "print(list(otvet))"
      ],
      "metadata": {
        "id": "EiXmhVh0LSks",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "6b0d3d00-e0d2-4931-ea8d-466b5c55fcb3"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2 3 4 5 6 7 8 9 10\n",
            "[2, 3, 5, 7]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "**Пункт 13:**\n",
        "\n",
        "Объедините три списка чисел в один список сумм соответствующих элементов. Используйте `map()`, `lambda` и `zip()`.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "list1 = [1, 2, 3]\n",
        "list2 = [4, 5, 6]\n",
        "list3 = [7, 8, 9]\n",
        "\n",
        "# Ожидаемый результат\n",
        "[12, 15, 18]  # (1+4+7, 2+5+8, 3+6+9)\n",
        "```"
      ],
      "metadata": {
        "id": "3ypTpW-hLWCv"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "list1 = [(lambda x: int(i))(i) for i in input().split()]\n",
        "list2 = [(lambda x: int(i))(i) for i in input().split()]\n",
        "list3 = [(lambda x: int(i))(i) for i in input().split()]\n",
        "otvet = map(lambda x: sum(x), list(map(lambda x: list(x), zip(list1, list2, list3))))\n",
        "print(list(otvet))"
      ],
      "metadata": {
        "id": "QK69qMn-LYig",
        "outputId": "4d8a39aa-adc7-429a-9588-f72bbe5ce079",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 \n",
            "4 5 6\n",
            "7 8 9\n",
            "[12, 15, 18]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "**Пункт 14:**\n",
        "\n",
        "С помощью `reduce()` и `lambda` подсчитайте количество появлений каждого символа в строке (без учета регистра), и выведите символ, который встречается чаще всего.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "text = 'Functional programming with lambda functions'\n",
        "\n",
        "# Ожидаемый результат\n",
        "' '  # пробел встречается чаще всего\n",
        "```\n",
        "\n",
        "*Подсказка:* Возможно, понадобится преобразовать строку в список символов и использовать словарь для подсчета."
      ],
      "metadata": {
        "id": "ux8lk6DULYrL"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from functools import reduce\n",
        "text=[str(i) for i in input()]\n",
        "d={x:0 for x in set(text)}\n",
        "for symbol in text:\n",
        "  d[symbol]+=1\n",
        "value_=reduce(lambda x, y: x if x>y else y, d.values())\n",
        "for key, value in d.items():\n",
        "  if value==value_:\n",
        "    print(key)\n",
        "    break"
      ],
      "metadata": {
        "id": "H5775c9vLlwh",
        "outputId": "3f5aca8c-ecaa-4010-e7de-c1203436b99c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Functional programming with lambda functions\n",
            "n\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---\n",
        "\n",
        "**Пункт 15:**\n",
        "\n",
        "Используя `map()`, `filter()`, `reduce()` и `lambda`, из заданного списка слов найдите общее количество гласных букв.\n",
        "\n",
        "**Пример:**\n",
        "\n",
        "```python\n",
        "# Входные данные\n",
        "words = ['python', 'lambda', 'functions', 'map', 'filter', 'reduce']\n",
        "\n",
        "# Ожидаемый результат\n",
        "15\n",
        "```\n",
        "\n",
        "*Подсказка:* Гласные буквы — 'a', 'e', 'i', 'o', 'u'."
      ],
      "metadata": {
        "id": "VFm4NoORKNEV"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from functools import reduce\n",
        "words = [(lambda x: str(i))(i) for i in input().split()]\n",
        "otvet = len(reduce(lambda x, y: x+y, list(filter(lambda x: x if x in ['y', 'a', 'e', 'i', 'o', 'u'] else None, (sum(list(map(lambda x: [i for i in x], words)), []))))))\n",
        "print(otvet)"
      ],
      "metadata": {
        "id": "QGrZe4tWLiYW",
        "outputId": "20c3a99e-9756-4846-a029-f947d99b4805",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "phyton lambda functions map filter reduce\n",
            "13\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "---"
      ],
      "metadata": {
        "id": "9xSbH7rdM4MS"
      }
    }
  ]
}
