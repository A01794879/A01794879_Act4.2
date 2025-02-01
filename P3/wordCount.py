"""
Módulo wordCount.py
"""
import sys
import time

def leer_archivo(nombre_archivo):
    """Función para leer el archivo y extraer las palabras"""    
    palabras = []
    errores = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                palabras.extend(linea.strip().split())
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        sys.exit(1)
    return palabras, errores

def contar_palabras(palabras):
    """Función para contar la frecuencia de palabras    """
    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.lower().strip(".,!?;:")  # Normalizar palabras
        if palabra:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

def main():
    """Función principal"""    
    if len(sys.argv) != 2:
        print("Uso correcto: python wordCount.py archivo.txt")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    inicio_tiempo = time.time()

    palabras, errores = leer_archivo(archivo_entrada)

    if not palabras:
        print("Error: No se encontraron palabras válidas en el archivo.")
        sys.exit(1)

    frecuencia_palabras = contar_palabras(palabras)
    tiempo_transcurrido = time.time() - inicio_tiempo

    # Mostrar resultados en consola
    print("Conteo de Palabras:")
    for palabra, frecuencia in sorted(frecuencia_palabras.items()):
        print(f"{palabra}: {frecuencia}")
    print(f"Tiempo de ejecución: {tiempo_transcurrido:.6f} segundos")

    if errores:
        print("\nErrores encontrados:")
        for error in errores:
            print(error)

    # Guardar resultados en archivo sin sobrescribir contenido
    with open("WordCountResults.txt", "a", encoding='utf-8') as archivo_resultado:
        archivo_resultado.write("Conteo de Palabras:\n")
        archivo_resultado.write(f"Archivo analizado: {archivo_entrada}\n")
        for palabra, frecuencia in sorted(frecuencia_palabras.items()):
            archivo_resultado.write(f"{palabra}: {frecuencia}\n")
        archivo_resultado.write(f"Tiempo de ejecución: {tiempo_transcurrido:.6f} segundos\n")

        if errores:
            archivo_resultado.write("\nErrores encontrados:\n")
            for error in errores:
                archivo_resultado.write(error + "\n")

        archivo_resultado.write("\n\n")

    print("\nLos resultados han sido agregados a 'WordCountResults.txt'")

if __name__ == "__main__":
    main()
