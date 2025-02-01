"""
Módulo compute_statistics
"""

import sys
import time

def leer_archivo(nombre_archivo):
    """Funcion para leer archivos y extraer los números"""
    numeros = []
    errores = []
    try:
        with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
            for linea in archivo:
                try:
                    numero = float(linea.strip())
                    numeros.append(numero)
                except ValueError:
                    errores.append(f"Error: '{linea.strip()}' no es un número válido.")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        sys.exit(1)
    return numeros, errores

def calcular_media(numeros):
    """Función para calcular la media"""
    suma = sum(numeros)
    return suma / len(numeros) if numeros else 0

def calcular_mediana(numeros):
    """Función para calcular la mediana"""
    numeros_ordenados = sorted(numeros)
    cantidad_numeros = len(numeros_ordenados)
    mitad = cantidad_numeros // 2
    if cantidad_numeros % 2 == 0:
        return (numeros_ordenados[mitad - 1] + numeros_ordenados[mitad]) / 2
    return numeros_ordenados[mitad]

def calcular_moda(numeros):
    """Función para calcular la moda"""    
    frecuencias = {}
    for numero in numeros:
        frecuencias[numero] = frecuencias.get(numero, 0) + 1
    moda = max(frecuencias, key=frecuencias.get)
    return moda

def calcular_varianza(numeros, media):
    """Función para calcular la varianza"""        
    suma_cuadrados = sum((x - media) ** 2 for x in numeros)
    return suma_cuadrados / len(numeros) if numeros else 0

def calcular_desviacion_estandar(varianza):
    """Función para calcular la desviación estándar"""         
    return varianza ** 0.5

def main():
    """Función principal"""          
    if len(sys.argv) != 2:
        print("Uso correcto: python computeStatistics.py archivo.txt")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    inicio_tiempo = time.time()

    numeros, errores = leer_archivo(archivo_entrada)

    if not numeros:
        print("Error: No se encontraron números válidos en el archivo.")
        sys.exit(1)

    media = calcular_media(numeros)
    mediana = calcular_mediana(numeros)
    moda = calcular_moda(numeros)
    varianza = calcular_varianza(numeros, media)
    desviacion_estandar = calcular_desviacion_estandar(varianza)
    tiempo_transcurrido = time.time() - inicio_tiempo

    # Mostrar resultados en consola
    print("Resultados Estadísticos:")
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")
    print(f"Varianza: {varianza}")
    print(f"Desviación estándar: {desviacion_estandar}")
    print(f"Tiempo de ejecución: {tiempo_transcurrido:.6f} segundos")

    if errores:
        print("\nErrores encontrados:")
        for error in errores:
            print(error)

    # Guardar resultados en archivo sin sobrescribir contenido
    with open("StatisticsResults.txt", "a", encoding="utf-8") as archivo_resultado:
        archivo_resultado.write("Resultados Estadísticos:\n")
        archivo_resultado.write(f"Archivo analizado: {archivo_entrada}\n")
        archivo_resultado.write(f"Media: {media}\n")
        archivo_resultado.write(f"Mediana: {mediana}\n")
        archivo_resultado.write(f"Moda: {moda}\n")
        archivo_resultado.write(f"Varianza: {varianza}\n")
        archivo_resultado.write(f"Desviación estándar: {desviacion_estandar}\n")
        archivo_resultado.write(f"Tiempo de ejecución: {tiempo_transcurrido:.6f} segundos\n")

        if errores:
            archivo_resultado.write("\nErrores encontrados:\n")
            for error in errores:
                archivo_resultado.write(error + "\n")

        archivo_resultado.write("\n\n")

    print("\nLos resultados han sido guardados en 'StatisticsResults.txt'")

if __name__ == "__main__":
    main()
