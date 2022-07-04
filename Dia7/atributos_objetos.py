#class Pajaro:
#    def __init__(self, color):
#        self.color = color
#mi_pajaro = Pajaro("negro")
#print(mi_pajaro.color)


class Pajaro:
    #atributo de clase para todos
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro("negro", "Tucan")
print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")
#no hace falta llamar a la variable de clase
print(Pajaro.alas)





class Casa:
    def  __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos

casa_blanca = Casa("blanco", 4)



class Cubo:

    caras = 6
    def __init__(self, color):
        self.color = color

cubo_rojo = Cubo("rojo")







class Personaje:
    real = False
    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje("Humano", "magico", 17)







































