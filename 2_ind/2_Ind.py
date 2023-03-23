#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == "__main__":

    count = 0
    slovar = ["unreal", "cringe", "look", "at", "this"]

    if len(sys.argv) != 2:
        print("Can`t get file name", file=sys.stderr)
        sys.exit(1)

    file_name = (sys.argv[1])

    with open(file_name, "r") as fileInd:
        content = fileInd.read().split(" ")
        for i, v in enumerate(content):
            if content[i].lower() not in slovar:
                count += 1
                print(f"Неправильное слово: {v}")
        print(f"Количество неправильно написанных слов: {count}")


