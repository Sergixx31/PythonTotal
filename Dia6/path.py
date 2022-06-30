from pathlib import Path

base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "SagradaFamilia.txt"))
#guia2 = guia.with_name("La_Pedrera.txt")
print(guia.parent.parent)
#print(guia2)
