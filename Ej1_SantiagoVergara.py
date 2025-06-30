#Gracias por la enseñanza de la clase pasada
import math

#Esta es la clase padre todapoderosa

class Figura:
  def __init__(self,nombre,color):
    self.nombre = nombre
    self.color = color

  def imprimirDetalles(self):
    print(f"Figura: {self.nombre}")
    print(f"Color: {self.color}")
  
#Clase hijo Circulo

class Circulo(Figura):
  def __init__(self, color, radio):
    super().__init__("Circulo", color)
    self.radio = radio
  
  def calcularArea(self):
    return math.pi * self.radio

  def calcularPerimetro(self):
        return 2 * self.radio * math.pi
  
  def imprimir_detalles(self):
        super().imprimirDetalles()
        print(f"Radio: {self.radio}")
        print(f"Área: {self.calcularArea():.2f}")
        print(f"Perímetro: {self.calcularPerimetro():.2f}")
        print("-----------------------------")

#prueba del circulo
circuloPaProbar = Circulo(color="Azul" , radio=5)
circuloPaProbar.imprimir_detalles()

#Clase Rectangulo
class Rectangulo(Figura):
    def __init__(self, color, base, altura):
        super().__init__("Rectángulo", color)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

    def imprimir_detalles(self):
        super().imprimirDetalles()
        print(f"Base: {self.base}")
        print(f"Altura: {self.altura}")
        print(f"Área: {self.calcular_area():.2f}")
        print(f"Perímetro: {self.calcular_perimetro():.2f}")
        print("-----------------------------")

rectanguloPaProbar = Rectangulo(color="Rojo" , base= 4 , altura= 6 )
rectanguloPaProbar.imprimir_detalles()
