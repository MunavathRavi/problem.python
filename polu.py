{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNVxYP/3vLhODjwGXr0kz9E",
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
        "<a href=\"https://colab.research.google.com/github/MunavathRavi/otp_arryas/blob/main/polu.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
      "execution_count": 33,
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
      "execution_count": 37,
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
      "execution_count": 46,
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
      "execution_count": 47,
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
      "execution_count": 55,
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
    }
  ]
}