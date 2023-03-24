#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    vowels = "aeuioy"

    with open("fileInd.txt", "r") as fileInd:
        content = list(fileInd.read())

    for i, v in enumerate(content):
        if content[i-1] == " " and (content[i] in vowels):
            content[i] = v.upper()
    print("".join(content))
