import re

def limpiar_tx(texto):
    '''
    Funcion encargada de reemplazar cualquier caracter especial del texto y tambien de presenarlo en minuscula para que no sea case sensitive
    '''
    tx_limpio = re.sub(r'[^\w\s]', '', texto)
    tx_limpio = tx_limpio.lower()
    return tx_limpio

def cont_pal(tx):
    '''
    Funcion que se encarga de contar la frecuencia de cada palabra y devolver una lista de tuplas de mayor a menor respecto a la frecuencia de cada palabra.
    '''
    palabras = tx.split()
    dic = {}
    for key in palabras:
        if key not in dic:
            dic[key] = 1
        else:
            dic[key] += 1
            
    dic_sort = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return dic_sort