import unittest
from unittest.mock import patch

from calculatrice import calculer, division, lire_nombre


class TestCalculer(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculer(2, "+", 3), 5)

    def test_soustraction(self):
        self.assertEqual(calculer(10, "-", 4), 6)

    def test_multiplication(self):
        self.assertEqual(calculer(3, "*", 4), 12)

    def test_division(self):
        self.assertEqual(calculer(8, "/", 2), 4)

    def test_division_par_zero(self):
        with self.assertRaises(ZeroDivisionError):
            division(1, 0)

    def test_operateur_inconnu(self):
        with self.assertRaises(ValueError):
            calculer(1, "%", 2)

    def test_nombres_negatifs_et_decimaux(self):
        self.assertEqual(calculer(-1.5, "+", 0.5), -1)
        self.assertEqual(calculer(-6, "/", 2), -3)


class TestLireNombre(unittest.TestCase):
    @patch("builtins.input", return_value="3,5")
    def test_accepte_la_virgule(self, _input):
        self.assertEqual(lire_nombre("Nombre : "), 3.5)

    @patch("builtins.input", side_effect=["abc", "4"])
    @patch("builtins.print")
    def test_redemande_si_saisie_invalide(self, _print, _input):
        self.assertEqual(lire_nombre("Nombre : "), 4)


if __name__ == "__main__":
    unittest.main()
