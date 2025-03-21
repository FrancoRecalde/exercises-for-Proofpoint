from services import limpiar_tx, cont_pal

def cargarArchivo(arch):
    '''
    Funcion que se encarga de leer el archivo de texto
    '''
    try:
        with open(arch, "r", encoding="utf-8") as archivo:
            texto = archivo.read()
        return texto
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{arch}'.")
    except Exception as e:
        print(f"Error inesperado: {e}")
    

def mostrar_frecuencia(frecuencia, n=10):
    '''
    Funcion que se encarga de mostar las 10 palabras con su frecuencia
    '''
    print(f"Las {n} palabras mas frecuentes son: ")
    top_n = frecuencia[:n]
    for i in top_n:
        print(f"La palabra '{i[0]}' tiene {i[1]} apariciones")

def main():
    archivo="./Ejercicio2/archivo.txt"
    texto = cargarArchivo(archivo)
    tx = limpiar_tx(texto)
    frec = cont_pal(tx)
    mostrar_frecuencia(frec, 10)
if __name__ == "__main__":
    main()