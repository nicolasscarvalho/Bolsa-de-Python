import unittest


def verbing(s):
    #SEU CODIGO AQUI

    if s == 'do':
      return s
    elif s[len(s)-3::] == 'ing':
      return s + 'ly'
    else:
      return s + 'ing'


# Dado um astring, procurar a primeira ocorrência da substring 'not' e 'bad'
# Se 'bad' vier após o 'not'
# substituir todo o trecho "not ... bad" por 'good'
# Retorne a string resultante.
def not_bad(s):
    if ('not' in s) and ('bad' in s ):
      index_not = s.index('not')
      index_bad = s.index('bad') 

      if index_not < index_bad:
        return s[0:index_not] + 'good' + s[index_bad+3::]
    
    return s

# Considere dividir uma string em duas metades.
# Se o comprimento for par, a parte da frente (front) e a parte de trás (back) são do mesmo tamanho.
# Se o comprimento for ímpar, o caracter extra irá para a parte da frente.
#
# Dado 2 strings, 'a' e 'b', retornar um string na forma
# a front + b front + a back + b back
def front_back(a, b):

  def organiza(s):
    comprimento_metade = len(s)//2
    indice_metade = comprimento_metade-1

    if 2*comprimento_metade == len(s):
      return (s[0:indice_metade+1], s[indice_metade+1::])
    else:
      indice_metade+=1
      return (s[0:indice_metade+1], s[indice_metade+1::])

  a_processado = organiza(a)
  b_processado = organiza(b)

  return a_processado[0] + b_processado[0] + a_processado[1] + b_processado[1]


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