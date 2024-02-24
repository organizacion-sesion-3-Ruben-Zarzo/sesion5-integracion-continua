# Librería pytest para ejecutar tests
import pytest

# Importar archivo de ejercicio
from ejercicios.operaciones import isPar

# Clase para crear tests. Las funciones de testeo deberán crearse en esta clase
class TestClass:

    # Test para la operación suma
    def test_isPar(self):
        assert isPar(1) == false
        assert isPar(2) == true
        assert isPar(23) == false
        assert isPar(42) == true 
