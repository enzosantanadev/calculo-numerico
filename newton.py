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