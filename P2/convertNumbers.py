"""
Módulo convertNumbers.py
"""
import sys
import time

def leer_archivo(nombre_archivo):
    """Función para leer el archivo y extraer los números"""    
    numeros = []
    errores = []
    try:
        with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
            for linea in archivo:
                try:
                    numero = int(linea.strip())
                    numeros.append(numero)
                except ValueError:
                    errores.append(f"Error: '{linea.strip()}' no es un número válido.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        sys.exit(1)
    return numeros, errores

def convertir_a_binario(numero):
    """Función para convertir un número a binario"""    
    binario = ""
    if numero == 0:
        return "0"
    while numero > 0:
        binario = str(numero % 2) + binario
        numero //= 2
    return binario

def convertir_a_hexadecimal(numero):
    """ Función para convertir un número a hexadecimal"""
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    if numero == 0:
        return "0"
    while numero > 0:
        hexadecimal = hex_chars[numero % 16] + hexadecimal
        numero //= 16
    return hexadecimal


def main():
    """Función principal"""
    if len(sys.argv) != 2:
        print("Uso correcto: python convertNumbers.py archivo.txt")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    inicio_tiempo = time.time()

    numeros, errores = leer_archivo(archivo_entrada)

    if not numeros:
        print("Error: No se encontraron números válidos en el archivo.")
        sys.exit(1)

    resultados = []
    for numero in numeros:
        binario = convertir_a_binario(numero)
        hexadecimal = convertir_a_hexadecimal(numero)
        resultados.append((numero, binario, hexadecimal))

    tiempo_transcurrido = time.time() - inicio_tiempo

    # Mostrar resultados en consola
    print("Resultados de Conversión:")
    for numero, binario, hexadecimal in resultados:
        print(f"Número: {numero}, Binario: {binario}, Hexadecimal: {hexadecimal}")
    print(f"Tiempo de ejecución: {tiempo_transcurrido:.6f} segundos")

    if errores:
        print("\nErrores encontrados:")
        for error in errores:
            print(error)

    # Guardar resultados en archivo sin sobrescribir contenido
    with open("ConvertionResults.txt", "a",encoding="utf-8") as archivo_resultado:
        archivo_resultado.write("Resultados de Conversión:\n")
        archivo_resultado.write(f"Archivo analizado: {archivo_entrada}\n")
        for numero, binario, hexadecimal in resultados:
            archivo_resultado.write(
                f"Número: {numero}, Binario: {binario}, Hexadecimal: {hexadecimal}\n"
            )
        archivo_resultado.write(f"Tiempo de ejecución: {tiempo_transcurrido:.6f} segundos\n")

        if errores:
            archivo_resultado.write("\nErrores encontrados:\n")
            for error in errores:
                archivo_resultado.write(error + "\n")

        archivo_resultado.write("\n\n")

    print("\nLos resultados han sido agregados a 'ConvertionResults.txt'")

if __name__ == "__main__":
    main()
