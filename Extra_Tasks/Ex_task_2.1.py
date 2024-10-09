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
        "<a href=\"https://colab.research.google.com/github/unidari/University/blob/main/Extra_Tasks/Ex_task_2.1.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
        "numbers = [(lambda x: str(x))(x) for x in input().split()]\n",
        "cube = map(lambda x: int(x) ** 3, numbers)\n",
        "print(list(cube))"
      ],
      "metadata": {
        "id": "g4gpq3TwKus0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ed27caec-e59d-4d78-dbcf-cece2e8d5053"
      },
      "execution_count": 8,
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
        "words = [(lambda x: str(x))(x) for x in input().split()]\n",
        "first_last = filter(lambda x: x[0]==x[-1], words)\n",
        "print(list(first_last))"
      ],
      "metadata": {
        "id": "k0-9uu2iK45z",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2fdcb1de-40c3-4289-9992-2d7ea976e935"
      },
      "execution_count": 9,
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
        "numbers = [(lambda x: int(x))(x) for x in input().split()]\n",
        "maximum = reduce(lambda x, y: y if (x<y) else x, numbers)\n",
        "print(maximum)"
      ],
      "metadata": {
        "id": "Gl9iHqHuK6Gp",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "70eb2ab8-3ae3-4899-dddc-37d62f497c07"
      },
      "execution_count": 11,
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
        "list1 = [(lambda x: int(x))(x) for x in input().split()]\n",
        "list2 = [(lambda x: int(x))(x) for x in input().split()]\n",
        "union = zip(list(map(lambda x: x**2, list1)), list(map(lambda x: x**3, list2)))\n",
        "print(list(union))"
      ],
      "metadata": {
        "id": "D9mval4GK9PB",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "f46567c2-7ea7-41a4-d7df-7cc3748fb095"
      },
      "execution_count": 12,
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
        "numbers = [(lambda x: str(x))(x) for x in input().split(',')]\n",
        "summa=reduce(lambda x,y: x+y, list(filter(lambda x: x if x%2==0 else None, list(map(lambda x: int(x), numbers)))))\n",
        "print(summa)"
      ],
      "metadata": {
        "id": "GSxOpO5CLDN2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e889537a-44bd-41a5-d22c-0096dc21a88d"
      },
      "execution_count": 13,
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
        "celsius = [(lambda x: int(x))(x) for x in input().split()]\n",
        "farg= map(lambda x: (x*9)/5+32, celsius)\n",
        "print(list(farg))"
      ],
      "metadata": {
        "id": "A03mTrhNLC06",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "da22b0f6-b7b6-406b-dd61-4c1d812ab914"
      },
      "execution_count": 14,
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
        "numbers = [(lambda x: int(x))(x) for x in input().split()]\n",
        "squa= map(lambda x: x**2, list(filter(lambda x: x if x%2!=0 else None, numbers)))\n",
        "print(list(squa))"
      ],
      "metadata": {
        "id": "ZV0oNPqlLose",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "87270159-89aa-4fd8-8f7e-7546d6d0fc2a"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 2 3 4 5 6 7 8 9 10\n",
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
        "numbers = [(lambda x: int(x))(x) for x in input().split()]\n",
        "proiz = reduce(lambda x,y: x*y, numbers)\n",
        "print(proiz)"
      ],
      "metadata": {
        "id": "_J-9EEJwLJk-",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "15f35631-dbf9-4f3d-e81a-cfdae2ea04ab"
      },
      "execution_count": 16,
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
        "strings = [(lambda x: str(x))(x) for x in input().split()]\n",
        "otvet = map(lambda x: int(x) if x.isdigit() else 0, strings)\n",
        "print(list(otvet))"
      ],
      "metadata": {
        "id": "uOLoUIMmLLwG",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d5a2ccea-dd11-476f-f2de-8ed34194dacc"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 20 abc 30 def\n",
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
        "list1 = [(lambda x: int(x))(x) for x in input().split()]\n",
        "list2 = [(lambda x: int(x))(x) for x in input().split()]\n",
        "tochki = zip(list1, list2)\n",
        "print(list(tochki))"
      ],
      "metadata": {
        "id": "BhyGHMK4LPey",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "e6c15314-dd7e-4684-bb88-75d717cd1cc1"
      },
      "execution_count": 5,
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
        "words = [(lambda x: str(x))(x) for x in input().split()]\n",
        "values=list(map(lambda x: len(x), words))\n",
        "for word in words:\n",
        "  if len(word) in values:\n",
        "    d[word]=len(word)\n",
        "    continue\n",
        "print(d)"
      ],
      "metadata": {
        "id": "8dSc6w2DLS72",
        "outputId": "87dc863c-cd76-4ee6-a987-19619d169799",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 18,
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
        "numbers = [(lambda x: int(x))(x) for x in input().split()]\n",
        "otvet = filter(lambda x: x if f(x)==1 else None, numbers)\n",
        "print(list(otvet))"
      ],
      "metadata": {
        "id": "EiXmhVh0LSks",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "2bf89ba0-5ff9-44b3-edaf-5257dd7ffbc6"
      },
      "execution_count": 19,
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
        "list1 = [(lambda x: int(x))(x) for x in input().split()]\n",
        "list2 = [(lambda x: int(x))(x) for x in input().split()]\n",
        "list3 = [(lambda x: int(x))(x) for x in input().split()]\n",
        "otvet = map(lambda x: sum(x), list(map(lambda x: list(x), zip(list1, list2, list3))))\n",
        "print(list(otvet))"
      ],
      "metadata": {
        "id": "QK69qMn-LYig",
        "outputId": "de5b3d5d-6f45-43ee-9901-a1474311f495",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 20,
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
        "text = [(lambda x: str(x))(x) for x in input()]\n",
        "d = {x:0 for x in sorted(list(set(text)))}\n",
        "for i in text:\n",
        "  if i in d:\n",
        "    d[i]+=1\n",
        "value = reduce(lambda x, y: x if x>y else y, d.values())\n",
        "for key in d.keys():\n",
        "  if d[key]==value:\n",
        "    print(key)\n",
        "    break"
      ],
      "metadata": {
        "id": "H5775c9vLlwh",
        "outputId": "dd8370df-9492-43e9-b10d-b183c5408b26",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 28,
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
        "words = [(lambda x: str(x))(x) for x in input().split()]\n",
        "otvet = len(reduce(lambda x, y: x+y, list(filter(lambda x: x if x in ['y', 'a', 'e', 'i', 'o', 'u'] else None, (sum(list(map(lambda x: [i for i in x], words)), []))))))\n",
        "print(otvet)"
      ],
      "metadata": {
        "id": "QGrZe4tWLiYW",
        "outputId": "22f35b7b-9b6d-4030-e1d3-24961fa6275c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 22,
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