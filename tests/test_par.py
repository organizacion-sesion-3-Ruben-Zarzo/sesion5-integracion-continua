# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import isPar

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_isPar(self):
        assert isPar(1) == False
        assert isPar(2) == True
        assert isPar(23) == False
        assert isPar(42) == True 
