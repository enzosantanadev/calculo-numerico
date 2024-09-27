from math import log

V = 750
U = 1800
M0 = 160000
Q = 2600
G = 9.81


PRECISAO = 10 ** (-10)


def ponto_medio(a, b):
    return (a+b)/2


def modulo(num):
    if num < 0:
        return num * -1
    return num


def bolzano(FUNCAO, a, b):
    return FUNCAO(a) * FUNCAO(b) < 0


def bisseccao(FUNCAO, a, b):
    pm = ponto_medio(a, b)
    print(pm)
    if modulo(FUNCAO(pm)) <= PRECISAO:
        return pm

    if bolzano(FUNCAO, a, pm):
        return bisseccao(FUNCAO, a, pm)
    return bisseccao(FUNCAO, pm, b)


def FUNCAO(t):
    if t <= 0 or 160000 - 2600 * t <= 0:
        return float('inf')
    return -750 / (1800 * log(160000 / (160000 - 2600 * t))) / (9.81 * t)


print(bisseccao(FUNCAO, 0.1, 100))




