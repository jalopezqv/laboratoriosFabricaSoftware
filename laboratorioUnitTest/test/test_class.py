from src.funciones import Calculadora


def test_class_calculadora(monkeypatch):

    """
    Funcion para probar la clase Calculadora
    """

    """
    De esta manera podemos darle un valor por defecto a una
    funcion o proceso que no necesitemos probar directamente
    """
    monkeypatch.setattr(Calculadora, "sumar", lambda x:4)
    obj_calculadora = Calculadora()

    assert obj_calculadora.sumar() == 4