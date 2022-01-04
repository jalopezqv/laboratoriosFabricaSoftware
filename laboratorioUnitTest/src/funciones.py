
def suma(input_a, input_b):
    """
    Funcion que toma 2 argumentos y devuelve la suma de los mismos
    Args :
        input_a (int/float): Primer valor a sumar
        input_b (int/float): Segundo valor a sumar
    
    return : input_a + input_b
    """
    resultado = input_a + input_b
    return resultado


def escribir(ruta_archivo, informacion):
    """
    Funcion que escribe en un archivo
    Args:
        ruta_archivo: Ruta absoluta del archivo
        informacion: Informacion a escribir
    """
    with open(ruta_archivo, "w") as archivo:
        archivo.write(informacion)


class Calculadora:
    """
    Clase calculadora
    """

    def sumar(valor_a,valor_b):
        """
        Funcion que toma 2 argumentos y ejecuta la funcion suma
        Args:
            valor_a (int/float): Primero valor a sumar
            valor_b (int/float): Segundo valor a sumar
        
        return suma(valor_a,valor_b)
        """
        
        return suma(valor_a,valor_b)