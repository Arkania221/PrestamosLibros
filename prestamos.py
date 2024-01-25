libros = []
libros_prestados = []
while True:
    print("Selecciona una opcion: Añadir libros = 1, Eliminar libros = 2, Mostrar libros = 3, Prestar libro = 4")

    Seleccion = int(input())

    if Seleccion == 1: #En esta seleccion se agrega un libro pidiendo al user que agregue un valor, este sera tomado como str y se agregara a la lista con un .append
        print("Escribe el nombre del libro")
        libro = str(input())
        libros.append(libro)
    elif Seleccion == 2: #Tiene el mismo funcionamiento que la primera parte pero cambiando el .append por un .remove y agregando una comprobacion
        print("Escribe el nombre del libro")
        libro = input()
        if libro in libros:
            libros.remove(libro)
        else:
            print("libro no encontrado")
    elif Seleccion == 3: #Solo printea la lista de libros
        print(libros)
    elif Seleccion = 4:
        print("a quien va prestado?")
        persona = input()
        print("Que libro va a ser prestado?")
        if libro in
    else:
        print("Opcion invalida")
        
