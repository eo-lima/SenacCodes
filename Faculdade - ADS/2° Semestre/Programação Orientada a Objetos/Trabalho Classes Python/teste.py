class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    def calcular_perimetro(self):
        return self.ladoA + self.ladoB + self.ladoC

    def maior_lado(self):
        self.lados = [self.ladoA, self.ladoB, self.ladoC]
        self.maiorlado = self.lados.index(max(self.lados))
        if self.maiorlado == 0:
            return f"É o lado A, {self.lados[0]}"
        elif self.maiorlado == 1:
            return f"É o lado B, {self.lados[1]}"
        else:
            return f"É o lado C, {self.lados[2]}"

ladoA = float(input("Digite o valor do lado A:"))
ladoB = float(input("Digite o valor do lado B:"))
ladoC = float(input("Digite o valor do lado C:"))
triangulo = Triangulo(ladoA, ladoB, ladoC)
print(triangulo.maior_lado())
print(triangulo.calcular_perimetro())