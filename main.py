import os
from collections import Counter
from colorama import Fore, Style, init

init(autoreset=True)

def guardar_resultados(estadisticas, archivo_salida):
    try:
        with open(archivo_salida, 'w', encoding='utf-8') as file:
            file.write(estadisticas)
        print(Fore.GREEN + f"Resultados guardados en: {archivo_salida}")
    except Exception as e:
        print(Fore.RED + f"Error al guardar el archivo: {e}")

def analizar_patrones(input_data):
    if ',' in input_data:
        elementos = input_data.split(',')
    elif ' ' in input_data:
        elementos = input_data.split()
    else:
        elementos = [input_data]
    
    elementos = [elem.strip() for elem in elementos if elem.strip()]
    
    es_numero = all(elem.replace('.', '', 1).isdigit() for elem in elementos)
    
    if es_numero:
        elementos = list(map(float, elementos)) 
    
    contador = Counter(elementos)
    total_elementos = len(elementos)
    elementos_unicos = len(contador)
    mas_comunes = contador.most_common(5)
    
    estadisticas_txt = "=== Estadísticas ===\n"
    estadisticas_txt += f"Total de elementos: {total_elementos}\n"
    estadisticas_txt += f"Elementos únicos: {elementos_unicos}\n"
    estadisticas_txt += "Frecuencia de elementos:\n"
    for elem, count in contador.items():
        estadisticas_txt += f"  {elem}: {count}\n"
    
    estadisticas_txt += "\nLos 5 elementos más comunes:\n"
    for elem, count in mas_comunes:
        estadisticas_txt += f"  {elem}: {count}\n"
    
    if es_numero:
        promedio = sum(elementos) / total_elementos
        suma_total = sum(elementos)
        estadisticas_txt += "\n=== Estadísticas Numéricas ===\n"
        estadisticas_txt += f"Promedio: {promedio:.2f}\n"
        estadisticas_txt += f"Suma total: {suma_total:.2f}\n"
        estadisticas_txt += f"Valor máximo: {max(elementos)}\n"
        estadisticas_txt += f"Valor mínimo: {min(elementos)}\n"
        estadisticas_txt += f"Rango (max-min): {max(elementos) - min(elementos)}\n"
    else:
        promedio_longitud = sum(len(word) for word in elementos) / total_elementos
        palabra_mas_larga = max(elementos, key=len)
        palabra_mas_corta = min(elementos, key=len)
        estadisticas_txt += "\n=== Estadísticas Textuales ===\n"
        estadisticas_txt += f"Longitud promedio de palabras: {promedio_longitud:.2f}\n"
        estadisticas_txt += f"Palabra más larga: {palabra_mas_larga}\n"
        estadisticas_txt += f"Palabra más corta: {palabra_mas_corta}\n"
    
    print(Fore.YELLOW + Style.BRIGHT + estadisticas_txt)
    
    guardar_resultados(estadisticas_txt, "estadisticas_resultado.txt")

def leer_archivo(archivo):
    if not os.path.exists(archivo):
        print(Fore.RED + "Error: El archivo no existe.")
        return None
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            contenido = f.read()
        return contenido
    except Exception as e:
        print(Fore.RED + f"Error al leer el archivo: {e}")
        return None

if __name__ == "__main__":
    print(Fore.YELLOW + Style.BRIGHT + "=== Análisis de Patrones ===")
    print(Fore.CYAN + "Selecciona el origen de los datos:")
    print(Fore.CYAN + "1. Introducir datos manualmente")
    print(Fore.CYAN + "2. Leer datos desde un archivo .txt")
    
    opcion = input(Fore.CYAN + "Opción (1 o 2): ").strip()
    
    if opcion == '1':
        entrada = input(Fore.CYAN + "Introduce un conjunto de datos (separados por comas, espacios o en lista): ")
        analizar_patrones(entrada)
    elif opcion == '2':
        ruta_archivo = input(Fore.CYAN + "Introduce la ruta del archivo .txt: ").strip()
        contenido = leer_archivo(ruta_archivo)
        if contenido:
            analizar_patrones(contenido)
    else:
        print(Fore.RED + "Opción no válida.")
