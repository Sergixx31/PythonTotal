import os
from pathlib import Path
from os import system


mi_ruta = Path("/home/sergi/PycharmProjects/PythonTotal/Dia6/proyecto", "recetas")

def contar_recetas(ruta):
    contador = 0
    #cada vez que encuentra un txt aumenta
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

def inicio():
    system("clear")
    print("*" * 50)
    print("*" * 5 + "Bienvenido al administrador de recetas" + "*" * 5)
    print("*" * 50)
    print("\n")
    print(f"Las recetas se encuentran en {mi_ruta}")
    print(f"Total recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = "x"
    #verifica si no es numerico
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print("Elige una opcion:")
        print("""
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoria nueva
        [4] - Eliminar receta
        [5] - Eliminar categoria
        [6] - Salir del programa""")
        eleccion_menu = input()
    return (eleccion_menu)

def mostrar_categorias(ruta):
    print("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    #iterar dentro del directorio
    for carpeta in ruta_categorias.iterdir():
        #guarda solo el nombre de la carpeta en string
        carpeta_str = str(carpeta.name)
        print(f"[{contador}] - {carpeta_str}")
        #construye la ruta a mostrar
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias

def elegir_categoria(lista):
    eleccion_correcta = "x"

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input("\nElije una categoria: ")
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("Estas son las recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    #por cada receta que encuentres en la lista ruta_recetas que acabe en .txt, lo añades a la lista_recetas
    for receta in ruta_recetas.glob("*.txt"):
        #solo guardas el name
        receta_str = str(receta.name)
        print(f"[{contador} - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

def elegir_recetas(lista):
    eleccion_recetas = "x"

    while not eleccion_recetas.isnumeric() or int(eleccion_recetas) not in range(1, len(lista) + 1):
        eleccion_recetas = input("\nElije una receta: ")

    return lista[int(eleccion_recetas) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + ".txt"
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta {nombre_receta} ha sido creada")
            existe = True
        else:
            print("Lo siento, esta receta ya existe")

def crear_categoria(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoria {nombre_categoria} ha sido creada")
            existe = True
        else:
            print("Lo siento, esta categoria ya existe")

def eliminar_receta(receta):
    #metodo para eliminar un archivo
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_categoria(categoria):
    #eliminar directorio
    Path(categoria).rmdir()
    print(f"La categotia {categoria.name} ha sido eliminada")

def volver_al_inicio():




















menu = 0

if menu == 1:
    mis_categorias = mostrar_categorias(mi_ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    mis_recetas = mostrar_recetas(mi_ruta)
    mi_receta = elegir_recetas(mis_recetas)
    leer_receta(mi_receta)
    #volver al inicio
    pass
elif menu == 2:
    mis_categorias = mostrar_categorias(mi_ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    crear_receta(mi_categoria)
    # volver inicio
    pass
elif menu == 3:
    crear_categoria(mi_ruta)
    #volver al inicio
    pass
elif menu == 4:
    mis_categorias = mostrar_categorias(mi_ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    mis_recetas = mostrar_recetas(mi_ruta)
    mi_receta = elegir_recetas(mis_recetas)
    eliminar_receta(mi_receta)
    # volver al inicio
    pass
elif menu == 5:
    mis_categorias = mostrar_categorias(mi_ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    eliminar_categoria(mi_categoria)
    #volver al inicio
    pass
elif menu == 6:
    #finalizar programa
    pass


inicio()