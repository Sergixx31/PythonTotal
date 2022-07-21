'''def suma():
    n1 = int(input("numero 1; "))
    n2 = int(input("Numero 2; "))
    print(n1 + n2)
    print("Gracias por sumar" + n1)



try:
    #codigo que queremos probar
    suma()
except TypeError:
    #codigo a ejecutar si hay error
    print("Estas intentado concatenar tipos distintos")
except ValueError:
    print("Ese no es un numero")
else:
    #codigo a ejecutar si no hay un error
    print("Hiciste ")
finally:
    #codigo que se va a ejecutar de todos modos
    print("Eso fue ")'''



'''def pedir_numero():

    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break #solo saldrá del programa cuando sea un numero, por eso el break, para que pare
    #hasta que no sale del bucle no imprime gracias
    print("Gracias")

pedir_numero()'''


'''def suma(num1, num2):

    try:
        print(num1 + num2)
    except:
        print("Error inesperado")'''

'''def cociente(num1,num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")'''



'''def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución"'''









