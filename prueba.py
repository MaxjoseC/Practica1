libros = []

def agregar_libro(libro):
    codigo = input ("Ingrese el código del libro: ")
    for libro in libros:
        if libro['Código del libro'] == codigo:
            print("El libro ya existe.")
            return
        
    titulo = input("Ingrese el título del libro: ")
    apellido_autor = input("Ingrese el apellido del autor: ")
    nombre_autor = input("Ingrese el nombre del autor: ")
    area_de_conocimiento = input("Ingrese el área de conocimiento: ")
    editorial = input("Ingrese la editorial del libro: ")
    tramo = input("Ingrese el tramo del libro: ")

    nuevo_libro = {
        'Código del libro': codigo,
        'Título': titulo,
        'Apellido del autor': apellido_autor,
        'Nombre del autor': nombre_autor,
        'Área de conocimiento': area_de_conocimiento,
        'Editorial': editorial,
        'Tramo': tramo,
        'estado': 'En sala'
    }

    libros.append(nuevo_libro)
    print("Libro agregado exitosamente.")

def modificar_libro():
    codigo = input("Ingrese el código del libro a modificar: ")
    for libro in libros:
        if libro['Código del libro'] == codigo:
            print("Libro encontrado.")
            print("Datos actuales del libro:")
            print(libro)
            nuevo_titulo = input("Ingrese el nuevo título del libro (deje en blanco para no modificar): ")
            nuevo_apellido_autor = input("Ingrese el nuevo apellido del autor (deje en blanco para no modificar): ")
            nuevo_nombre_autor = input("Ingrese el nuevo nombre del autor (deje en blanco para no modificar): ")
            nuevo_area_de_conocimiento = input("Ingrese el nuevo área de conocimiento (deje en blanco para no modificar): ")
            nueva_editorial = input("Ingrese la nueva editorial del libro (deje en blanco para no modificar): ")
            nuevo_tramo = input("Ingrese el nuevo tramo del libro (deje en blanco para no modificar): ")

            if nuevo_titulo:
                libro['Título'] = nuevo_titulo
            if nuevo_apellido_autor:
                libro['Apellido del autor'] = nuevo_apellido_autor
            if nuevo_nombre_autor:
                libro['Nombre del autor'] = nuevo_nombre_autor
            if nuevo_area_de_conocimiento:
                libro['Área de conocimiento'] = nuevo_area_de_conocimiento
            if nueva_editorial:
                libro['Editorial'] = nueva_editorial
            if nuevo_tramo:
                libro['Tramo'] = nuevo_tramo

            print("Libro modificado exitosamente.")
            return
    
    print("El código ingresado no corresponde a ningún libro.")

def mostrar_libros():
    if not libros:
        print("No hay libros registrados.")
        return
    print("Lista de libros registrados:")
    for i, libro in enumerate(libros, 1):
        print(f"{i}. Código: {libro['Código del libro']}, Título: {libro['Título']}, Autor: {libro['Nombre del autor']} {libro['Apellido del autor']}\n")
        
def buscar_libro():
    codigo = input("Ingrese el código del libro a buscar: ")
    for libro in libros:
        if libro['Código del libro'] == codigo:
            print("Libro encontrado.")
            print(libro)
            return
    
    print("El código ingresado no corresponde a ningún libro.")


def eliminar_libro():
    codigo = input("Ingrese el código del libro a eliminar: ")
    for libro in libros:
        if libro['Código del libro'] == codigo:
            libros.remove(libro)
            print("Libro eliminado exitosamente.")
            return
    
    print("El código ingresado no corresponde a ningún libro.")


def menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar libro")
        print("2. Modificar libro")
        print("3. Mostrar libros")
        print("4. Buscar libro")
        print("5. Eliminar libro")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_libro({})
        elif opcion == '2':
            modificar_libro()
        elif opcion == '3':
            mostrar_libros()
        elif opcion == '4':
            buscar_libro()
        elif opcion == '5':
            eliminar_libro()
        elif opcion == '6':
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
# Este script permite gestionar una biblioteca de libros, permitiendo agregar, modificar, mostrar, buscar y eliminar libros.