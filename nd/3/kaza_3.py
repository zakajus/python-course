import doctest
import unittest

# 8. patikrinti ar skaičius yra tobulas


def yra_tobulas(skaicius):
    """
    Patikrina ar skaičius yra tobulas (daliklių suma yra lygi skaičiui).

    >>> yra_tobulas(6)
    True

    >>> yra_tobulas(33550336)
    True

    >>> yra_tobulas(10)
    False

    >>> yra_tobulas(2987238)
    False

    >>> yra_tobulas(-4)
    False

    >>> yra_tobulas(0)
    False

    >>> yra_tobulas(6.7)
    False
    """

    if skaicius <= 1 or (int(skaicius) != skaicius):
        return False
    dalikliu_suma = sum(i for i in range(1, skaicius) if skaicius % i == 0)
    return dalikliu_suma == skaicius


class test_yra_tobulas(unittest.TestCase):
    def test_sveikieji(self):
        self.assertTrue(yra_tobulas(6))
        self.assertTrue(yra_tobulas(33550336))
        self.assertFalse(yra_tobulas(10))
        self.assertFalse(yra_tobulas(2987238))

    def test_neigiami(self):
        self.assertFalse(yra_tobulas(-4))

    def test_nulis(self):
        self.assertFalse(yra_tobulas(0))

    def test_realieji(self):
        self.assertFalse(yra_tobulas(6.7))


if __name__ == "__main__":
    # pass
    doctest.testmod()
    unittest.main()
