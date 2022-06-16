#pedir al usuario un texto
#pedir al usuario 3 letras

#5 analisis:
#cuantas veces aparece cada letra
#cuantas palabras hay en total
#la primera letra del texto y la ultima
#como quedaria el texto invertiendo el orden de las palabras
#si la palabra python se encuentra en el texto

texto = input("Introduce un texto: ")
letras = []

texto = texto.lower()

letras.append(input("Escribe la primera letra: ").lower())
letras.append(input("Escribe la segunda letra: ").lower())
letras.append(input("Escribe la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida '{cantidad_letras1}' veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida '{cantidad_letras2}' veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida '{cantidad_letras3}' veces")

print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")

print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"si ordenamos tu texto al revés va a decir: {texto_invertido}")

print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = "python" in texto
dic = {True:"si", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")








