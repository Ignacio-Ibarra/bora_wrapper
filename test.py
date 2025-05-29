import unittest
from bora.secciones import SegundaSeccion


class TestSegundaSeccion(unittest.TestCase):

    def test_get_result_returns_list(self):
        
        # Este test puede fallar si no hay resultados ese día o si no hay conexión
        instancia = SegundaSeccion(
            rubros=['CONSTITUCION SA'],
            fecha_desde="28/05/2025",
            fecha_hasta="28/05/2025"
        )
        resultado = instancia.get_result()
        
        self.assertIsInstance(resultado, list)
        for item in resultado:
            self.assertIsInstance(item, str)
            self.assertTrue(item.startswith("https://"))
    

if __name__ == "__main__":
    unittest.main()