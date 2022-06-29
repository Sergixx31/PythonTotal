#solo es true si hay dos 0 seguidos
def cero_vecinos(*args):

    contador = 0

    for num in args:

        if contador +1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1

    return False

print(cero_vecinos(0,4,6,4,3,0,0,5,76,4,3,5,67,4,0))