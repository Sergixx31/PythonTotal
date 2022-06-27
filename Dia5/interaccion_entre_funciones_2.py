from random import randint

def lanzar_dados():
    numero1 = randint(1,6)
    numero2 = randint(1,6)
    return numero1, numero2


def evaluar_jugada(numero1, numero2):
    suma_dados = numero1 + numero2
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif suma_dados >= 10:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
    else:
        "pta"


dado1, dado2 = lanzar_dados()
evaluar_jugada(dado1, dado2)
