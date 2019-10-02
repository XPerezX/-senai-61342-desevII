import unittest


class CalmelCase:

    def __init__(self):
        self.palavras_resultado = []

    def __adicionar_palavras_resultado(self, palavra):
        self.palavras_resultado.append(palavra.lower())

    def __quebrar_palavra_posicao(self, palavra, caracter):
        palavras = []
        posicao = palavra.rfind(caracter)

        palavras.append(palavra[:posicao])
        palavras.append(palavra[posicao:])

        return palavras

    def __primeiro_caracter(self, palavra):
        return palavra[0]

    def __percorre_palavra(self,palavra):
        specials = ["#", "!", "º", "%", "$"]
        for caracter in palavra:
            if caracter in specials:
                return "yes"



    def __quebra_camel_case(self, palavra):
        for caracter in palavra:
            if caracter.isupper() and palavra.rfind(caracter) != 0:
                palavras = self.__quebrar_palavra_posicao(palavra, caracter)

                for palavra in palavras:
                    self.__adicionar_palavras_resultado(palavra)

    def split(self, palavra):
        numeros = ["0","1","2","3","4","5","6","7","8","9"]

        if self.__primeiro_caracter(palavra) not in numeros :
            if self.__percorre_palavra(palavra) is not "yes":



                if palavra.islower():
                    self.__adicionar_palavras_resultado(palavra)

                elif len(palavra) <= 8 and palavra.isupper():
                    self.palavras_resultado.append(palavra.upper())

                else:
                    if self.__primeiro_caracter(palavra).isupper():
                        self.__adicionar_palavras_resultado(palavra)

                    else:
                        self.__quebra_camel_case(palavra)
                return self.palavras_resultado
            else:
                return "invalido"
        else:
            return "invalido"



class TestCamelCase(unittest.TestCase):

    def test_split_palavra_minuscula(self):
        camel_case = CalmelCase()
        lista_palavras = camel_case.split("nome")

        self.assertEqual(lista_palavras, ["nome"])

    def test_split_palavra_maiuscula(self):
        camel_case = CalmelCase()
        lista_palavras = camel_case.split("Nome")

        self.assertEqual(lista_palavras, ["nome"])

    def test_split_palavra_manoel(self):
        camel_case = CalmelCase()
        lista_palavras = camel_case.split("manoel")

        self.assertEqual(lista_palavras, ["manoel"])

    def test_split_palavra_camel_case(self):
        camel_case = CalmelCase()
        lista_palavras = camel_case.split("nomeComposto")

        self.assertEqual(lista_palavras, ["nome", "composto"])

    def test_split_palavra_numero_inicio(self):
        camel_case = CalmelCase()
        lista_palavras = camel_case.split("12nome")

        self.assertEqual(lista_palavras, "invalido")

    def test_split_palavra_caracter_special(self):
        camel_case = CalmelCase()
        lista_palavras = camel_case.split("nom%e#")

        self.assertEqual(lista_palavras, "invalido")

    def test_split_palavra_siglas(self):
        camel_case = CalmelCase()
        lista_palavras = camel_case.split("CPF")

        self.assertEqual(lista_palavras, ["CPF"])

    def test_split_palavra_siglas2(self):
        camel_case = CalmelCase()
        lista_palavras = camel_case.split("TEC")

        self.assertEqual(lista_palavras, ["TEC"])

    def test_split_palavra_teste_composto(self):
        camel_case = CalmelCase()
        lista_palavras = camel_case.split("jorgeLeao")

        self.assertEqual(lista_palavras, ["jorge", "leao"])

    def test_split_palavra_teste_composto_numero_comeco(self):
        camel_case = CalmelCase()
        lista_palavras = camel_case.split("123jorgeLeao")

        self.assertEqual(lista_palavras, "invalido")

    def test_split_palavra_teste_composto_caracter_special(self):
        camel_case = CalmelCase()
        lista_palavras = camel_case.split("jor#geLeao")

        self.assertEqual(lista_palavras, "invalido")

if __name__ == '__main__':
    unittest.main()
