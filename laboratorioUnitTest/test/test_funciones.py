import pytest
from src import funciones as f

"""
Una forma para agregar varios casos de prueba en un decorador y finalmente
hacer un test unitario mucho mas agil
"""
@pytest.mark.parametrize(
    "input_a,input_b,resultado",
    [
        (3,2,5),
        (2,3,5),
        (f.suma(3,2),5,10),
        (3,f.suma(2,5),10)
    ]
)
def test_suma(input_a,input_b,resultado):
    suma = f.suma(input_a,input_b)
    assert suma == resultado


"""
En este test unitario pasamos como parametro una ruta temporal
que nos ayudara a validar la funcion escribir y cuando haya finalizado el proceso
la ruta temporal no nos ocupara espacio en memoria.
De esta manera nos evitamos crear una ruta y un archivo real que 
luego no necesitaremos.
"""
def test_escribir(tmpdir):
    ruta_archivo = f"{tmpdir}/test.txt"
    informacion = "Prueba de la funcion escribir"
    f.escribir(ruta_archivo,informacion)

    with open(ruta_archivo) as archivo_procesado:
        informacion_leida = archivo_procesado.read()

    assert informacion == informacion_leida
