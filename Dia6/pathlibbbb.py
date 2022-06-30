from pathlib import Path, PureWindowsPath

##con esto no hace falta el open de antes
carpeta = Path("/home/sergi/PycharmProjects/PythonTotal/Dia6/Prueba.txt")
#print(carpeta.read_text())

##para que se adapta a windows
ruta_windows = PureWindowsPath(carpeta)
print(ruta_windows)


##nombre del archivo
#print(carpeta.name)

##terminacion del archivo
#print(carpeta.suffix)

##nombre sin terminacion
#print(carpeta.stem)

##true o false
#if not carpeta.exists():
#    print("Este archivo no existe")
#else:
#    print("Genial")

