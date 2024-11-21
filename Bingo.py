import random
import datetime

# Variables globales
bingo_info = {"fecha": "", "hora": "", "costo": 0}
compras = []


# Función para mostrar el menú principal
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Configurar información del Bingo")
    print("2. Comprar Bingos")
    print("3. Visualizar compras")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")
    return opcion


# Función para configurar la información del Bingo
def configurar_informacion():
    global bingo_info
    print("\n--- CONFIGURAR INFORMACIÓN DEL BINGO ---")
    bingo_info["fecha"] = input("Ingrese la fecha (dd/mm/yyyy): ")
    bingo_info["hora"] = input("Ingrese la hora (HH:MM): ")
    bingo_info["costo"] = float(input("Ingrese el costo del Bingo: S/ "))
    print(
        f"\nInformación configurada:\nFecha: {bingo_info['fecha']} - Hora: {bingo_info['hora']} - Costo: S/ {bingo_info['costo']}")


# Función para comprar Bingos
def comprar_bingos():
    global compras, bingo_info
    print("\n--- COMPRAR BINGOS ---")
    nombre = input("Nombre: ")
    dni = input("DNI: ")
    email = input("Email: ")
    cantidad_bingos = int(input("Cantidad de Bingos: "))
    total_costo = cantidad_bingos * bingo_info['costo']
    print(f"Costo total: S/ {total_costo}")

    # Confirmar compra
    confirmar = input("(A)ceptar o (C)ancelar: ").upper()
    if confirmar == 'A':
        bingos_generados = generar_bingos(cantidad_bingos)
        fecha_compra = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        compras.append(
            {"nombre": nombre, "dni": dni, "email": email, "cantidad": cantidad_bingos, "costo_total": total_costo,
             "fecha": fecha_compra, "bingos": bingos_generados})
        print("Compra realizada correctamente!")
        print(f"Fecha de compra: {fecha_compra}")
        for bingo in bingos_generados:
            print(f"Número de serie: {bingo['serie']}")
            imprimir_bingo(bingo["numeros"])
    else:
        print("Compra cancelada")


# Función para generar Bingos
def generar_bingos(cantidad):
    bingos = []
    for _ in range(cantidad):
        bingo = {
            "serie": f"{random.randint(100, 999)}",
            "numeros": generar_numeros_bingo()
        }
        bingos.append(bingo)
    return bingos


# Función para generar los números de una cartilla de Bingo
def generar_numeros_bingo():
    bingo = []
    for i in range(5):
        if i == 0:
            columna = random.sample(range(1, 16), 5)
        elif i == 1:
            columna = random.sample(range(16, 31), 5)
        elif i == 2:
            columna = random.sample(range(31, 46), 5)
        elif i == 3:
            columna = random.sample(range(46, 61), 5)
        elif i == 4:
            columna = random.sample(range(61, 76), 5)
        bingo.append(columna)
    return bingo


# Función para imprimir una cartilla de Bingo
def imprimir_bingo(numeros):
    print("B   I   N   G   O")
    for fila in range(5):
        for columna in range(5):
            if fila == 2 and columna == 2:
                print(" * ", end=" ")  # Espacio del centro del bingo
            else:
                print(f"{numeros[columna][fila]:2}", end="  ")
        print()


# Función para visualizar las compras
def visualizar_compras():
    global compras
    print("\n--- VISUALIZAR COMPRAS ---")
    if len(compras) == 0:
        print("No se han realizado compras aún.")
    else:
        print(f"|{'Nombre':<20}{'Fecha':<20}{'Cantidad':<10}{'Total (S/)':<10}|")
        total_recaudado = 0
        for compra in compras:
            print(f"|{compra['nombre']:<20}{compra['fecha']:<20}{compra['cantidad']:<10}{compra['costo_total']:<10}|")
            total_recaudado += compra['costo_total']
        print(f"\nTotal recaudado: S/ {total_recaudado}")


# Programa principal
def main():
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            configurar_informacion()
        elif opcion == "2":
            if bingo_info["costo"] == 0:
                print("Primero debe configurar la información del Bingo.")
            else:
                comprar_bingos()
        elif opcion == "3":
            visualizar_compras()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


# Ejecutar el programa principal
if __name__ == "__main__":
    main()
