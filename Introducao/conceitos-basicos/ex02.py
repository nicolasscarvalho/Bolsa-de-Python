import unittest


def verbing(s):
    #SEU CODIGO AQUI
    pass


# Dado um astring, procurar a primeira ocorrência da substring 'not' e 'bad'
# Se 'bad' vier após o 'not'
# substituir todo o trecho "not ... bad" por 'good'
# Retorne a string resultante.
def not_bad(s):
    not_index = s.index('not')
    bad_index = s.index('bad')

    if bad_index < not_index:
        return s.replace(s[not_index:bad_index], 'good')

# Considere dividir uma string em duas metades.
# Se o comprimento for par, a parte da frente (front) e a parte de trás (back) são do mesmo tamanho.
# Se o comprimento for ímpar, o caracter extra irá para a parte da frente.
#
# Dado 2 strings, 'a' e 'b', retornar um string na forma
# a front + b front + a back + b back
def front_back(a, b):
    comprimento_a = len(a)//2
    excedente_a = len(a)-(2*comprimento_a)

    comprimento_b = len(b)//2
    excedente_b = len(b)-(2*comprimento_b)

    return a[-1:-comprimento_a-excedente_a:-1] + b[-1:-comprimento_b-excedente_b:-1] + a[0:comprimento_a] + b[0:comprimento_b]


class MyTest(unittest.TestCase):

  def test_verbing(self):
    self.assertEqual(verbing('hail'), 'hailing')
    self.assertEqual(verbing('swiming'), 'swimingly')
    self.assertEqual(verbing('do'), 'do')

  def test_not_bad(self):
    self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good')
    self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
    self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")

  def test_front_back(self):
    self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
    self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
    self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  unittest.main()