##pascal  pacheco 24/06/2025
entradas = {
    "viernes": 150,
    "sabado": 180
}
cliente = []

def compra():
    nombre = input("*** ingrese nombre del comprador*** ")
    print("***funciones disponibles***")
    print("1.Cats dia Viernes", entradas["viernes"], "entradas")
    print("2.Cats dia Sabado", entradas["sabado"], "entradas")
    op = int(input("Seleccione una opción (1 o 2): "))
    if op == 1:
        entradas["viernes"] > 0
        entradas["viernes"] -= 1
        cliente.append((nombre, "viernes"))
        print("compra con exito. 1 entrada para el viernes.")
    elif op == 2:
        entradas["sabado"] > 0
        entradas["sabado"] -= 1
        cliente.append((nombre, "sabado"))
        print("compra con exito. 1 entrada para el sabado.")
    else:
        print("ingrese una opcion valida")
    print("***stock restante***")
    print("1.Cats dia Viernes", entradas["viernes"], "entradas")
    print("2.Cats dia Sabado", entradas["sabado"], "entradas")

def cambio_funcion():
    print("***cambio de funcion***")
    nc = input("nombre del comprador: ")
    for i, (nombre, funcion) in enumerate(cliente):
        if nombre == nc:
            if funcion == "viernes" and entradas["sabado"] > 0:
                resp = input("¿confirme para cambiar su entrada de viernes a sabado? (s/n): ").lower()
                if resp == "s":
                    cliente[i] = (nombre, "sabado")
                    entradas["viernes"] += 1
                    entradas["sabado"] -= 1
                    print("Cambio realizado")
                else:
                    print("No se realizó el cambio.")
            elif funcion == "sabado" and entradas["viernes"] > 0:
                resp = input("¿confirme para cambiar su entrada de sabado a viernes? (s/n): ").lower()
                if resp == "s":
                    cliente[i] = (nombre, "viernes")
                    entradas["sabado"] += 1
                    entradas["viernes"] -= 1
                    print("Cambio realizado")
                else:
                    print("No se realizó el cambio.")
            else:
                print("No hay stock disponible para el cambio.")
            return
    print("comprador no encontrado")

def stock():
    print("***stock actual***")
    print("1.Cats dia Viernes", entradas["viernes"], "entradas")
    print("2.Cats dia Sabado", entradas["sabado"], "entradas")

def menu():
    while True:
        print("TOTEM AUTOATENCIÓN CAFECONLECHE")
        print("1.- Comprar entrada a Cats.")
        print("2.- Cambio de función.")
        print("3.- Mostrar stock de funciones.")
        print("4.- Salir.")
        try:
            mn = int(input("elija una opcion(1-4): "))
            if mn == 1:
                compra()
            elif mn == 2:
                cambio_funcion()
            elif mn == 3:
                stock()
            elif mn == 4:
                print("Salir")
                break
            else:
                print("Ingrese una opción válida.")
        except ValueError:
            print("Ingrese un número válido.")

if __name__ == "__main__":
    menu()