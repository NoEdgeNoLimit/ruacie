#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

baseList = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


def changeBase(n, b):
    x, y = divmod(n, b)
    if x > 0:
        return changeBase(x, b) + baseList[y]
    else:
        return baseList[y]


def changeToTenBase(s, b):
    sL = list(s)
    sL.reverse()
    result = 0
    for x in range(len(sL)):
        result = result + baseList.index(sL[x]) * (b ** x)
    return result


def is_polydivisible(s, b):
    for x in range(len(s)):
        if changeToTenBase(s[:x + 1], b) % (x + 1) != 0:
            return False
    return True


def get_polydivisible(n, b):
    count = 0
    result = 0
    while count < n:
        baseResult = changeBase(result, b)
        if is_polydivisible(baseResult, b):
            count = count + 1
            result = result + 1
    return baseResult


if __name__ == '__main__':
    print(changeBase(5634472569470976, 62))
    print(changeToTenBase('Pny33UYL2', 62))
    print(changeBase(15, 2))
    print(changeBase(15, 7))
    print(changeBase(6, 8))
    print(changeBase(32, 30))
