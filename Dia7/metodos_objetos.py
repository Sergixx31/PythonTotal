class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio, mi color es {}".format(self.color))

    def volar(self, metros):
        print(f"El pajaro ha volado {metros} metros")


piolin = Pajaro("amarillo", "Canario")
piolin.piar()



##########################################
class Perro:

    def ladrar(self):
        print("Guau!")

pluto = Perro()
pluto.ladrar()

class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

telefono = Alarma()
telefono.postergar(50)







