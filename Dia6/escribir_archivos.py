#con la W sobreescribe TODO
#con la a añade al final del todo
#R de solo lectura, por default es la R

archivo = open('Prueba.txt',"a", encoding='cp1252', errors='surrogateescape')
#archivo.write("hola ")
#archivo.write("mundo")

#lsita = ["hola", "mundo", "aqui", "estoy"]

#for p in lsita:
#    archivo.writelines(p + "\n")



archivo.write("Bienvenido")










archivo.close()
