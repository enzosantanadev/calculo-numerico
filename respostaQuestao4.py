class Bisseccao:
    def __init__(self, funcao, precisao):
        self.funcao = funcao
        self.precisao = precisao

    def ponto_medio(self, a, b):
        return (a + b) / 2

    def modulo(self, num):
        return abs(num)

    def bolzano(self, a, b):
        return self.funcao(a) * self.funcao(b) < 0

    def metodo(self, a, b):
        pm = self.ponto_medio(a, b)
        if self.modulo(self.funcao(pm)) <= self.precisao:
            return pm

        if self.bolzano(a, pm):
            return self.metodo(a, pm)
        return self.metodo(pm, b)

G = 9.8
M = 110
V = 40
T = 7
E = 2.7
PRECISAO = 10 ** (-6)

def FUNCAO(c):
    c = c if c != 0 else PRECISAO
    return ((G * M * (1 - E**(-T*(c/M)))) / c) - V

bisseccao = Bisseccao(funcao=FUNCAO, precisao=PRECISAO)

resultado = bisseccao.metodo(10, 20)
print(resultado)
