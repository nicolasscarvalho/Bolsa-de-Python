import unittest

# Dado um lista de strings `words`, retornar o total de strings
# se cada palavra for maior ou igual a dois e
# se o primeiro caracter coincidir com o último
def match_ends(words):
    cont = 0

    for word in words:
      if len(word) >= 2 and word[0] == word[-1]:
        cont += 1
    
    return cont

# Dado uma lista de strings, retornar uma lista de string ordenadas,
# exceto todo grupo de strings que comece com "x" virá primeiro.
#
# Dica: isto pode ser feito com 2 listas ordenando cada uma delas e
# depois combinado-as. Veja os testes para maiores detalhes.
def front_x(words):
  ordenacao = sorted(words)

  for indice, word in enumerate(ordenacao):
    if word[0] == 'x':
      return sorted(ordenacao[-1:-indice:-1]) + ordenacao[0:indice]


# Dado uma lista de tuplas não vazias, retornar uma lista ordenada
# pelo último elemento de cada tupla.
#
# Dica: use um função personalizada `last()` para extrair
# o último elemento, ela deve ser passada no segundo parâmetro
# da função sorted()
def last(a):
  return a[-1]

def sort_last(tuples):
  return sorted(tuples, key=last)

class MyTest(unittest.TestCase):
  def test_match_ends(self):
    self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  def test_front_x(self):
    self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

  def test_sort_last(self):
    self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
    self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

if __name__ == '__main__':
  unittest.main()