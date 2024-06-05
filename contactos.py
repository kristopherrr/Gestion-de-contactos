# Contactos iniciales
contactos = {
    "Juan": "1234567890",
    "María": "9876543210",
    "Pedro": "5555555555",
    "Ana": "1111111111"
}

def agregar_contacto(contactos):
    nombre = input("Ingresa el nombre del contacto: ")
    numero = input("Ingresa el número de teléfono: ")
    contactos[nombre] = numero
    print("El contacto ha sido agregado correctamente.")

def buscar_contacto(contactos):
    nombre = input("Ingresa el nombre del contacto: ")
    if nombre in contactos:
        print(f"El número de teléfono de {nombre} es: {contactos[nombre]}")
    else:
        print(f"No se encontró el contacto {nombre}.")

def mostrar_contactos(contactos):
    if contactos:
        print("Contactos:")
        for nombre, numero in contactos.items():
            print(f"- {nombre}: {numero}")
    else:
        print("No hay contactos para mostrar.")

def actualizar_contacto(contactos):
    nombre = input("Ingresa el nombre del contacto a actualizar: ")
    if nombre in contactos:
        numero = input("Ingresa el nuevo número de teléfono: ")
        contactos[nombre] = numero
        print(f"El número de teléfono de {nombre} ha sido actualizado correctamente.")
    else:
        print(f"No se encontró el contacto {nombre}.")

def eliminar_contacto(contactos):
    nombre = input("Ingresa el nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"El contacto {nombre} ha sido eliminado correctamente.")
    else:
        print(f"No se encontró el contacto {nombre}.")

def main():
    while True:
        print("\nBienvenido a la gestión de contactos.")
        print("Opciones:")
        print("1. Agregar un contacto.")
        print("2. Buscar un contacto.")
        print("3. Mostrar todos los contactos.")
        print("4. Actualizar número de teléfono.")
        print("5. Eliminar un contacto.")
        print("6. Salir.")

        opcion = input("Ingresa tu opción: ")

        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            buscar_contacto(contactos)
        elif opcion == "3":
            mostrar_contactos(contactos)
        elif opcion == "4":
            actualizar_contacto(contactos)
        elif opcion == "5":
            eliminar_contacto(contactos)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, ingresa un número del 1 al 6.")

if __name__ == "__main__":
    main()
