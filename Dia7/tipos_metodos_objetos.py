class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")
        self.piar()


    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")

    @staticmethod
    def mirar():
        print("El pajaro mira")

Pajaro.poner_huevos(3)
Pajaro.mirar()
##################################################################



class Mascota():
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

Mascota.respirar()



class Jugador:
    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True


#instancia
class Personaje:
    #atributo de instancia
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    #metodo de instancia
    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1










