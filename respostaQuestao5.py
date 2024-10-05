from math import cos, sin

PRECISAO = 10 ** (-5)

class Newton:
    def MODULO(self, n):
        return abs(n)

    def formula(self, FUNCAO, DERIVADA_FUNCAO, x):
        return x - (FUNCAO(x) / DERIVADA_FUNCAO(x))

    def metodo(self, FUNCAO, DERIVADA_FUNCAO, CHUTE):
        if self.MODULO(FUNCAO(CHUTE)) < PRECISAO:
            return CHUTE
        novo_chute = self.formula(FUNCAO, DERIVADA_FUNCAO, CHUTE)
        return self.metodo(FUNCAO, DERIVADA_FUNCAO, novo_chute)

def FUNCAO(x):
    return x * cos(x) + 4

def DERIVADA_FUNCAO(x):
    return -x * sin(x) + cos(x)

newton = Newton()
raiz1 = newton.metodo(FUNCAO, DERIVADA_FUNCAO, 8)
raiz2 = newton.metodo(FUNCAO, DERIVADA_FUNCAO, 10)

print(raiz1)
print(raiz2)
