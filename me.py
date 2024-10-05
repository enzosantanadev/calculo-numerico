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
