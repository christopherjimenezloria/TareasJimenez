"""
Solución para las funciones
filtrar_vocales y encontrar_extremos.
Los códigos de retorno siguen exactamente
lo especificado en el archivo de pruebas.
"""

# Códigos de éxito y error según el archivo de pruebas
CODIGO_EXITO = 0

ERROR_NO_STRING = -100
ERROR_NO_ALFABETICO = -200
ERROR_VACIO = -300
ERROR_DEMASIADO_LARGO = -400
ERROR_BANDERA_NO_BOOL = -500

ERROR_NO_LISTA = -600
ERROR_ELEMENTO_NO_NUMERO = -700
ERROR_LISTA_VACIA = -800
ERROR_LISTA_DEMASIADO_LARGA = -900


def filtrar_vocales(cadena, bandera):
    """
    Filtra vocales o consonantes de una
    cadena según una bandera.

    Parámetros:
        cadena (str): Cadena a procesar.
        bandera (bool): True para extraer
        vocales, False para consonantes.

    Retorna:
        tuple: (código, resultado) donde
        resultado es el string filtrado o None.
    """
    # Validar tipo string
    if not isinstance(cadena, str):
        return (ERROR_NO_STRING, None)

    # Validar no vacía
    if len(cadena) == 0:
        return (ERROR_VACIO, None)

    # Validar solo letras (alfabéticas)
    if not cadena.isalpha():
        return (ERROR_NO_ALFABETICO, None)

    # Validar longitud máxima
    if len(cadena) > 30:
        return (ERROR_DEMASIADO_LARGO, None)

    # Validar bandera booleana
    if not isinstance(bandera, bool):
        return (ERROR_BANDERA_NO_BOOL, None)

    vocales = set('aeiouAEIOU')
    if bandera:
        # Extraer vocales
        resultado = ''.join(c for c in cadena if c in vocales)
    else:
        # Extraer consonantes (letras que no son vocales)
        resultado = ''.join(c for c in cadena if c not in vocales)

    return (CODIGO_EXITO, resultado)


def encontrar_extremos(lista_numeros):
    """
    Encuentra el valor mínimo y
    máximo de una lista de números.

    Parámetros:
        lista_numeros (list): Lista de números (int o float).

    Retorna:
        tuple: (código, mínimo, máximo)
        o (código_error, None, None).
    """
    # Validar que sea lista
    if not isinstance(lista_numeros, list):
        return (ERROR_NO_LISTA, None, None)

    # Validar no vacía
    if len(lista_numeros) == 0:
        return (ERROR_LISTA_VACIA, None, None)

    # Validar longitud máxima
    if len(lista_numeros) > 15:
        return (ERROR_LISTA_DEMASIADO_LARGA, None, None)

    # Validar que todos los elementos sean números (int o float) y no booleanos
    # (bool es subclase de int, por lo que debemos excluirlo explícitamente)
    if not all(
        isinstance(x, (int, float)) and not isinstance(x, bool)
        for x in lista_numeros
    ):
        return (ERROR_ELEMENTO_NO_NUMERO, None, None)

    minimo = min(lista_numeros)
    maximo = max(lista_numeros)
    return (CODIGO_EXITO, minimo, maximo)
