import unittest
from Calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(Calculadora.suma(2,3),5)

    def test_resta(self):
        self.assertEqual(Calculadora.resta(5,3),2)

    def test_multiplicar(self):
        self.assertEqual(Calculadora.multiplicar(4,3),12)

    def test_dividir(self):
        self.assertEqual(Calculadora.dividir(10,2),5)    

    def test_division_cero(self):
        with self.asserRaises(ValueError):
            Calculadora.dividir(5,0)

    def test_raiz(self):
        self.assertAlmostEqual(Calculadora.raiz(9),3,places=3)

    def test_exp(self):
        self.assertAlmostEqual(Calculadora.exp(1),2.718,places=3)

    if __name__=="__main__":
        unittest.main()