class Animal:
    #atributo
    def __init__(self, edad, color):
       self.edad = edad
       self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")


class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):

        #otra manera de hacer el self, asiccnaciones hereredadas
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo


    # heredado pero modificado
    def hablar(self):
        print("pio")
    def volar(self, metros):
        print(f"El pajaro vuela {metros} metros")



piolin = Pajaro(3, "amarillo", 60)
mi_animal = Animal(5, "negro")
piolin.volar(100)


#herencia multiple
class Padre:
    def hablar(self):
        print("hola")

class Madre:
    def reir(self):
        print("haha")
    #no imprime pk primero pasa el parametro de padre, el primero que pongas
    def hablar(self):
        print("que tal")
class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

#orden de recolucion de metodos, va de abajo a arriba
print(Nieto.__mro__)



class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")


class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")

class Hija(Madre, Padre):
    pass





class Vertebrado():
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True

    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")

    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")

    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    pass





class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"

class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"








































