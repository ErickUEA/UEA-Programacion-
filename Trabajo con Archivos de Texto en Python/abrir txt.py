# palabras que iran en el texto del archivo
nota = "Ver como hay que crear el archivo python \nCrear el archivo python\nComentar el archivo python \nSubir a GitHub el archivo python \nEnviar a revisar el archivo"
# Se guarda el nombre my_notes.txt en crear_nota
crear_nota = "my_notes.txt"
# Se crea el archivo my_notes con el modo de apertura r+ para poder editar y leer el archivo y se guarda en la variable archivo
archivo = open(crear_nota, "r+")
# se escribe en el archivo las palabras que guardamos en la variable nota
archivo.write(nota)
# Se pone en la posicion cero del archivo
archivo.seek(0)
# Imprime cada linea del archivo
for imprimir in archivo.readlines():
    print(imprimir, end="")
# Se cierra el archivo
archivo.close()
