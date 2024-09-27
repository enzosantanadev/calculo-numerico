from math import log

V = 750
U = 1800
M0 = 160000
Q = 2600
G = 9.81


PRECISAO = 10 ** (-10)



def FUNCAO(t):
    if t <= 0 or 160000 - 2600 * t <= 0:
        return float('inf')
    return -750 / (1800 * log(160000 / (160000 - 2600 * t))) / (9.81 * t)


def DERIVADA_FUNCAO(t):
    if t <= 0 or 160000 - 2600 * t <= 0:
        return float('inf')

    C = -750 / (1800 * 9.81)

    log_term = log(160000 / (160000 - 2600 * t))
    d_log_term = (2600 / (160000 - 2600 * t)) / (160000 / (160000 - 2600 * t))

    v = t * log_term
    v_derivada = log_term + t * d_log_term

    return C * (-v_derivada / (v ** 2))


class Newton:
    def MODULO(self, n):
        if n < 0:
            return n * -1
        return n

    def formula(self, FUNCAO, DERIVADA_FUNCAO, x):
        return x - (FUNCAO(x) / DERIVADA_FUNCAO(x))

    def metodo(self, FUNCAO, DERIVADA_FUNCAO, CHUTE):
        if self.MODULO(FUNCAO(CHUTE)) < PRECISAO:
            return CHUTE

        return self.metodo(FUNCAO, self.formula(FUNCAO, DERIVADA_FUNCAO, CHUTE))


class Bisseccao:
    def ponto_medio(a, b):
        return (a + b) / 2

    def modulo(self, num):
        if num < 0:
            return num * -1
        return num

    def bolzano(self, FUNCAO, a, b):
        return FUNCAO(a) * FUNCAO(b) < 0

    def metodo(self, FUNCAO, a, b):
        pm = self.ponto_medio(a, b)
        if self.modulo(FUNCAO(pm)) <= PRECISAO:
            return pm

        if self.bolzano(FUNCAO, a, pm):
            return self.metodo(FUNCAO, a, pm)
        return self.metodo(FUNCAO, pm, b)



