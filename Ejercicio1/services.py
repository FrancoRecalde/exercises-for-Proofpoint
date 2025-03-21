from collections import defaultdict

def ver_anio(anio):
    '''
    Funcion que verifica que se ingrese un numero valido
    '''
    try:
        anio = int(anio)
        if anio < 0 or anio > 2025:  
            anio = 0
    except ValueError:
        anio = 0
    return anio

def org_lib(libros):
    """
    Organiza los libros por autor. Para los libros con autor desconocido,
    los agrupa y los ordena por año de publicación.
    """
    organizados = defaultdict(list)
    libros_unknown = []  
    for (titulo, autor), anio in libros.items():
        if autor == "Author Unknown":
            
            libros_unknown.append((titulo, anio))
        else:
            
            organizados[autor].append((titulo, anio))
    libros_unknown_ordenados = sorted(libros_unknown, key=lambda x: x[1])
    print(libros_unknown_ordenados)
    organizados["Autor Unknown"] = libros_unknown_ordenados
    return organizados