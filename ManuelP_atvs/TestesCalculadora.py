import unittest


class Calculadora:
    def soma(self, n1, n2):

        return float(n1) + float(n2)

    def mult(self, n1, n2):
        return float(n1) * float(n2)

    def div(self, n1, n2):
        return float(n1) / float(n2)

    def sub(self , n1, n2):
        return float(n1) - float(n2)


class TestStringMethods(unittest.TestCase):
    def test_calcula_soma(self):
        obj = Calculadora()
        reajuste = obj.soma(1, 2)
        self.assertEqual(reajuste, 3)

    def test_calcula_multi(self):
        obj = Calculadora()
        reajuste = obj.mult(1, 2)
        self.assertEqual(reajuste, 2)

    def test_calcula_div(self):
        obj = Calculadora()
        reajuste = obj.div(1, 2)
        self.assertEqual(reajuste, 0.5)

    def test_calcula_sub(self):
        obj = Calculadora()
        reajuste = obj.sub(1, 2)
        self.assertEqual(reajuste, -1)







if __name__ == '__main__':
    unittest.main()



'''
v1 = input("digite o numero")
v2 = input("digite o numero")
print(calculadora.soma(v1,v2))
'''