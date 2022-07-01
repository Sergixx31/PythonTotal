
def abrir_leer(texto):
    archivo = open('ejemplo.txt', encoding='cp1252', errors='surrogateescape')
    return archivo.read()


def sobrescribir(texto):
    archivo_sobrescribir = open('ejemplo.txt', "w",encoding='cp1252', errors='surrogateescape')
    archivo_sobrescribir.write("contenido eliminado")



def registro_error(archivo):
    mi_archivo = open('ejemplo.txt', "a",encoding='cp1252', errors='surrogateescape')
    mi_archivo.write("se ha registrado un error de ejecución")
    mi_archivo.close()