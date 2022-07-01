#from pathlib import Path

#base = Path.home()
#guia = Path(base, "Europa", "España", Path("Barcelona", "SagradaFamilia.txt"))
#guia2 = guia.with_name("La_Pedrera.txt")

##arbol de ancestros
#print(guia.parent.parent)
#print(guia2)



from pathlib import Path

guia = Path(Path("/home/sergi/PycharmProjects/PythonTotal/Dia6"), "Europa")

##todos los txt del directorio EUROPA
#for txt in Path(guia).glob("**/*.txt"):
#    print(txt)



guia = Path("Europa", "España", "Barcelona", "SagradaFamilia.txt")
en_europa = guia.relative_to("Europa")
en_espania = guia.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_espania)
































