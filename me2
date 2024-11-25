import math


def funcao(x):
    return (
        (math.exp(x) * math.sin(x)) 
        / 
        (1 + x ** 2)
    )


class Metodos:
    def __init__(self, funcao):
        self.funcao = funcao


    def trapezio(self, lim_a, lim_b, num):
        h = (lim_b - lim_a) / num
        soma = self.funcao(lim_a) + self.funcao(lim_b)
        
        for i in range(1, num):
            soma += 2 * self.funcao(lim_a + i * h)
            
        return (h / 2) * soma
    
    
    def simpson_composto(self, lim_a, lim_b, num):
        if num % 2 != 0: return "A quantidade de subintervalos não é par."
            
        h = (lim_b - lim_a) / num
        soma = self.funcao(lim_a) + self.funcao(lim_b)
        
        for i in range(1, num, 2):
            soma += 4 * self.funcao(lim_a + i * h)
            
        for i in range(2, num, 2):
            soma += 2 * self.funcao(lim_a + i * h)
            
        return (h / 3) * soma



metodos = Metodos(funcao)

lim_a = 0
lim_b = 2

intervalo_1 = 1
intervalo_2 = 5
intervalo_3 = 20


print("=-" * 10, " Trapézio Composto ", "=-" * 10)
print(f"Intervalo 1 -> {metodos.trapezio(lim_a, lim_b, intervalo_1)}")
print(f"Intervalo 2 -> {metodos.trapezio(lim_a, lim_b, intervalo_2)}")
print(f"Intervalo 3 -> {metodos.trapezio(lim_a, lim_b, intervalo_3)}")
print("=-" * 10, " Simpson Composto ", "=-" * 10)
print(f"Intervalo 1 -> {metodos.simpson_composto(lim_a, lim_b, intervalo_1)}")
print(f"Intervalo 2 -> {metodos.simpson_composto(lim_a, lim_b, intervalo_2)}")
print(f"Intervalo 3 -> {metodos.simpson_composto(lim_a, lim_b, intervalo_3)}")
print("=-" * 30)
