def cargar_datos(nombre_archivo):
    lista_pokemon = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            archivo.readline()
            for i in range(50):
                linea = archivo.readline()
                if not linea:
                    break
                datos = linea.strip().split(',')
                pokemon = [
                    datos[1], 
                    datos[2], 
                    int(datos[5]), 
                    int(datos[6]), 
                    int(datos[7]), 
                    int(datos[10])
                ]
                lista_pokemon.append(pokemon)
        return lista_pokemon
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        return []

def buscar_por_termino(lista):
    termino = input("Ingrese el nombre o tipo a buscar: ").lower()
    encontrados = 0
    print("--- Resultados de Búsqueda ---")
    for p in lista:
        if termino in p[0].lower() or termino in p[1].lower():
            print(f"Nombre: {p[0]} | Tipo: {p[1]} | HP: {p[2]}")
            encontrados += 1
    print(f"Se encontraron {encontrados} registros.")

def calcular_estadisticas_ataque(lista):
    if not lista: return
    suma_atk = 0
    max_atk = lista[0][3]
    min_atk = lista[0][3]
    for p in lista:
        valor = p[3]
        suma_atk += valor
        if valor > max_atk: max_atk = valor
        if valor < min_atk: min_atk = valor
    promedio = suma_atk / len(lista)
    print("--- Estadísticas de Ataque ---")
    print(f"Máximo: {max_atk} | Mínimo: {min_atk} | Promedio: {promedio:.2f}")

def filtrar_por_defensa(lista):
    try:
        limite = int(input("Mostrar pokemon con Defensa mayor a: "))
        print(f"--- pokemon con Defensa > {limite} ---")
        conteo = 0
        for p in lista:
            if p[4] > limite:
                print(f"- {p[0]} (Defensa: {p[4]})")
                conteo += 1
        print(f"Total: {conteo} pokemon encontrados.")
    except ValueError:
        print("Error: Ingrese un número entero.")

def mostrar_todos(lista):
    print(f"{'NOMBRE':<20} | {'TIPO':<12} | {'VELOCIDAD':<10}")
    print("-" * 45)
    for p in lista:
        print(f"{p[0]:<20} | {p[1]:<12} | {p[5]:<10}")

def ejecutar_programa():
    datos = cargar_datos('Pokemon.csv')
    if not datos: return

    while True:
        print("================================")
        print("      EXPLORADOR POKEMON")
        print("================================")
        print("1. Buscar por término (Nombre/Tipo)")
        print("2. Ver estadísticas de Ataque")
        print("3. Filtrar por nivel de Defensa")
        print("4. Listar todos los registros")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            buscar_por_termino(datos)
        elif opcion == '2':
            calcular_estadisticas_ataque(datos)
        elif opcion == '3':
            filtrar_por_defensa(datos)
        elif opcion == '4':
            mostrar_todos(datos)
        elif opcion == '5':
            print("Cerrando sistema...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar_programa()
