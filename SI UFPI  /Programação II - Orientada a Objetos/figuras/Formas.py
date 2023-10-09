# Quadrado.py

from FormasGeometricas import FormasGeometricas
from Desenhavel import Desenhavel

class Quadrado(FormasGeometricas, Desenhavel):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

    def calcular_perimetro(self):
        return 4 * self.lado

    def desenha(self):
        for _ in range(self.lado):
            print('#' * self.lado)

# Retangulo.py

from FormasGeometricas import FormasGeometricas
from Desenhavel import Desenhavel

class Retangulo(FormasGeometricas, Desenhavel):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def desenha(self):
        for _ in range(self.altura):
            print('#' * self.base)

# Circulo.py

from FormasGeometricas import FormasGeometricas

class Circulo(FormasGeometricas):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        return 3.14 * (self.raio ** 2)

    def calcular_perimetro(self):
        return 2 * 3.14 * self.raio

# Exemplos de uso:
# Criar um quadrado de lado 3
quadrado = Quadrado(lado=3)
# Desenhar o quadrado
print("\nDesenho do quadrado:")
quadrado.desenha()
# Calcular e imprimir área e perímetro do quadrado
print(f"Área do quadrado: {quadrado.calcular_area()}")
print(f"Perímetro do quadrado: {quadrado.calcular_perimetro()}")

# Criar um retângulo com base 4 e altura 2
retangulo = Retangulo(base=4, altura=2)
# Desenhar o retângulo
print("\nDesenho do retângulo:")
retangulo.desenha()
# Calcular e imprimir área e perímetro do retângulo
print(f"Área do retângulo: {retangulo.calcular_area()}")
print(f"Perímetro do retângulo: {retangulo.calcular_perimetro()}")
