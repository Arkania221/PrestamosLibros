libros = []
libros_prestados = []
while True:
    print("Selecciona una opcion: Añadir libros = 1, Eliminar libros = 2, Mostrar libros = 3, Prestar libro = 4, devolver prestamos = 5")

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
        for libros in libros:
            print("Nombre:" + libros)
        for libros_prestados in libros_prestados:
            print("Prestamo" + libros_prestados)
    elif Seleccion == 4: #Primero recoge el valor persona, recoge el valor libro, si el libro existe mezcla los dos valores mas ":" y borra el libro de la lista libros
        print("a quien va prestado?")
        persona = input()
        print("Que libro va a ser prestado?")
        libro = input()
        if libro in libros:
            libros_prestados.append(persona + ":" + libro)
            libros.remove(libro)
    elif Seleccion == 5: #Realiza la misma tarea pero a la inversa, agrega el libro en la lista libros y borra el prestamo realizaddo con anteiroridad           libro
        print("A quien fue prestado?")
        persona = input()
        print("Que libro fue prestado?")
        libro = input()
        libro_prestado = (persona + ":" + libro)
        if libro_prestado in libros_prestados:
            libros_prestados.remove(persona + ":" + libro)
            libros.append(libro)
        else:
            print("no esta")
    else:
        print("Opcion invalida")
        
