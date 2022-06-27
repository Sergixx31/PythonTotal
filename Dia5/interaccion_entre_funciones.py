from random import shuffle
#lista inicial palitos
palitos = ["-", "--", "---", "----"]


#funcion mezcla palitos
def mezclar(lista):
    shuffle(lista)
    return lista
#print(mezclar(palitos))


#pedir al usuario elejir numeros
def probar_suerte():
    intento = ""

    while intento not in ["1", "2", "3", "4"]:
        intento = input("elige un numero del 1 al 4: ")
    return int(intento)

#intento1 = probar_suerte()
#print(intento1)


#comprobar el intento si es el 1,2,3,4
def chequear_intento(lista,intento):
    if lista[intento - 1] == "-":
        print("A lavar los platos")
    else:
        print("Esta vez te has salvado")

    print(f"Te ha tocado {lista[intento-1]}")



palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

































