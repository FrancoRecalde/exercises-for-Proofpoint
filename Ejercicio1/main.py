import csv
from services import ver_anio, org_lib



def leer_csv(arch):
    '''
    Funcion que se encarga de leer el archivo csv
    '''
    try:
        with open(arch, mode='r', newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            return list(reader)
    except FileNotFoundError:
        print(f"Error: El archivo '{arch}' no se encontró.")
        return []
    except Exception as e:
        print(f"Error inesperado al abrir el archivo: {e}")
        return []

def proc_lib(datos):
    '''Funcion hecha para procesar los libros, uso un diccionario para que no se repitan las keys (titulo, autor)
    reemplazo los libros que faltan y verifico el año llamando a su funcion service.'''
    libros = {}
    for fila in datos:
        if len(fila) != 3:
            print(f"Advertencia: Fila ignorada por formato incorrecto: {fila}")
            continue  
        titulo, autor, anio = fila
        if not autor:
            autor = "Author Unknown"
        anio = ver_anio(anio)
        key = (titulo, autor)
        if key not in libros: 
            libros[key] = anio
    return libros


def mostrar_lib(libros):
    '''
    Funcion encargada de mostrar los libros indicando su autor, año y titulo
    '''
    for key, valores in libros.items():
        
        print(f"Autor:{key}")
        for titulo, anio in valores:
            print(f"Titulo: {titulo}, Año:{anio}")    
            
    
def escribir_csv(archivo_salida, organizados):
    """
    Escribo los libros organizados en un archivo CSV.
    """
    with open(archivo_salida, mode='w', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        writer.writerow(["Título", "Autor", "Año"])
       
        for autor, libros_autor in organizados.items():
            for titulo, anio in libros_autor:
                writer.writerow([titulo, autor, anio])

def main():
    archivo_en = './Ejercicio1/archivo.csv'
    archivo_sa = './Ejercicio1/archivo_salida.csv'
    datos = leer_csv(archivo_en)
    libros = proc_lib(datos)
    organizados = org_lib(libros)
    
    mostrar_lib(organizados)
    escribir_csv(archivo_sa, organizados)

if __name__== "__main__":
    main()