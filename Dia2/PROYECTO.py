nombre_usuario = input("Dime tu nombre: ")
ventas = float(input("Cuantas ventas has obtenido: "))
porcentaje_ventas = round(ventas * 13 / 100,2)

print(f"Ok {nombre_usuario}. Ganas de comision un 13%, te tocan ${porcentaje_ventas}")

