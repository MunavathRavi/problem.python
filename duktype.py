{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOfCpZ3UsqJwV7p5H3C1WXo",
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
        "<a href=\"https://colab.research.google.com/github/MunavathRavi/problem.python/blob/main/duktype.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class ravi:\n",
        "  def __init__(self,name,age,rank):\n",
        "    self.name = name\n",
        "    self._age = age\n",
        "    self.__rank = rank\n",
        "\n",
        "  def __ravi1(self,new_rank):\n",
        "    self.__rank = new_rank\n",
        "obj4=ravi(\"munavath\",23,\"10th\")\n",
        "print(obj4.name)\n",
        "print(obj4._age)\n",
        "obj4._ravi__ravi1(\"11th\")\n",
        "print(obj4._ravi__rank)\n",
        "obj4._ravi__rank =\"12th\"\n",
        "print(obj4._ravi__rank)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EeLPGuNakIVO",
        "outputId": "09f1497d-4916-446e-8335-b6df0849dd03"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "munavath\n",
            "23\n",
            "11th\n",
            "12th\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class ravi:\n",
        "  def __init__(self,name,age,rank):\n",
        "    self.name = name\n",
        "    self._age = age\n",
        "    self.__rank = rank\n",
        "\n",
        "  @property\n",
        "  def rank(self):\n",
        "    return self.__rank\n",
        "obj5=ravi(\"munavath\",23,\"11th\")\n",
        "print(obj5.name)\n",
        "print(obj5.rank)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hEm2Ds-3uOnT",
        "outputId": "64bd3c9f-404c-47ae-b236-8b8b6982ba91"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "munavath\n",
            "11th\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class ravi:\n",
        "  def __init__(self,name,age,rank):\n",
        "    self.name = name\n",
        "    self._age = age\n",
        "    self.__rank = rank\n",
        "\n",
        "  def __ran(self,new_rank):\n",
        "    self.__rank = new_rank\n",
        "obj6=ravi(\"munavath\",23,\"11th\")\n",
        "print(obj6.name)\n",
        "print(obj6._ravi__rank)\n",
        "obj6._ravi__ran(\"12th\")\n",
        "print(obj6._ravi__rank)\n",
        "obj6._ravi__rank = \"13th\"\n",
        "print(obj6._ravi__rank)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vrl_5uPpvBcP",
        "outputId": "02a9e4c6-56da-4a25-dd15-49cb21f12551"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "munavath\n",
            "11th\n",
            "12th\n",
            "13th\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class ravi:\n",
        "  def __init__(self,name,age,rank):\n",
        "    self.name = name\n",
        "    self._age = age\n",
        "    self.__rank = rank\n",
        "  @property\n",
        "  def rank(self):\n",
        "    return self.__rank\n",
        "  @rank.setter\n",
        "  def rank(self,new_rank):\n",
        "    self.__rank = new_rank\n",
        "obj=ravi(\"munavth\",12,\"10th\")\n",
        "print(obj.name)\n",
        "print(obj.rank)\n",
        "print(obj._age)\n",
        "obj.rank = \"12th\"\n",
        "print(obj.rank)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "y9jq1xWYv_BK",
        "outputId": "6e1bcc27-13b2-495b-b53f-93003e6b0d7c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "munavth\n",
            "10th\n",
            "12\n",
            "12th\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class parent:\n",
        "  def __init__(self,name):\n",
        "    self.name = name\n",
        "  def ravi(self):\n",
        "    return(f\"hello {self.name}\")\n",
        "class chield(parent):\n",
        "  def ravi(self):\n",
        "    return(f\"good moring {self.name}\")\n",
        "obj=parent(\"munavth ravi\")\n",
        "obj.ravi()\n",
        "obj1=chield(\"munavath ravi\")\n",
        "obj1.ravi()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "TjM-3wYk0vLR",
        "outputId": "73a8c6cd-2ee8-4432-e498-9e8edee12876"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'good moring munavath ravi'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 55
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#operator overloding"
      ],
      "metadata": {
        "id": "-y65FwFX5wOJ"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class aditions:\n",
        "  def __init__(self,number):\n",
        "    self.number = number\n",
        "  def __add__(self,number2):\n",
        "    return aditions(self.number+number2.number)\n",
        "obj1= aditions(10)\n",
        "obj2= aditions(500)\n",
        "r = obj2+obj1\n",
        "print(r.number)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qrossdvh65rD",
        "outputId": "3be5eef5-5d56-415d-a805-5dd5e18349da"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "510\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class equal:\n",
        "  def __init__(self,mark):\n",
        "    self.mark = mark\n",
        "  def __eq__(self, value):\n",
        "    return self.mark == value.mark\n",
        "obj1 = equal(10)\n",
        "obj2 = equal(10)\n",
        "obj1 == obj2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5H0Zup5P9vnh",
        "outputId": "e1990cef-5415-4061-f7e5-43b4e43a06ce"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 9
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class mutipications:\n",
        "  def __init__(self,one):\n",
        "    self.one = one\n",
        "  def __mul__(self,values):\n",
        "    return mutipications(self.one * values.one)\n",
        "o = mutipications(3)\n",
        "o2 = mutipications(6)\n",
        "r = o*o2\n",
        "print(r.one)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ph8nQtSsP5ib",
        "outputId": "a172c4d9-53ed-4a2f-f311-57b398e0039a"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "18\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "class grat:\n",
        "  def __init__(self,value):\n",
        "    self.value = value\n",
        "  def __lt__(self,number):\n",
        "    return grat(self.value < number.value)\n",
        "obj1 = grat(45)\n",
        "obj2 = grat(55)\n",
        "r = obj1<obj2\n",
        "print(r.value)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4APhbbEllAK_",
        "outputId": "ecde6502-d903-4511-f9a6-aebd3cb5d3b6"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#duktype"
      ],
      "metadata": {
        "id": "7tUkj__YnXJ0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "class duk :\n",
        "  def sound(self):\n",
        "    print(\"duk duk duk duk\")\n",
        "class dof:\n",
        "  def sound(self):\n",
        "    print(\"bhuu bhuu bhuu\")\n",
        "def animal_soun(animal):\n",
        "    animal.sound()\n",
        "obj = duk()\n",
        "obj1 = dof()\n",
        "\n",
        "animal_soun(obj)\n",
        "animal_soun(obj1)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ubcBDA7a2cpN",
        "outputId": "2b31cbe2-d1cf-425c-efcc-9f0dc1431dc0"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "duk duk duk duk\n",
            "bhuu bhuu bhuu\n"
          ]
        }
      ]
    }
  ]
}