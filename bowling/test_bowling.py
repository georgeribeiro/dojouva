import unittest
from bowling import bowling

class TestBrowling(unittest.TestCase):
    
    def test_0000000000_0(self):
        """
        Todos as jogadas com o zero retorna 0 como pontuacao
        """
        self.assertEquals(bowling([
        (0,0),
        (0,0),
        (0,0),
        (0,0),
        (0,0)
        ])
        , 0)
    
    def test_3152412553_31(self):
        """
        Nenhum spare ou strike, somente soma os elementos
        """
        self.assertEquals(bowling([
        (3,1),
        (5,2),
        (4,1),
        (2,5),
        (5,3)
        ])
        , 31)
        
    def test_3752412553_42(self):
        """
        Ocorre spare na primeira jogada
        """
        self.assertEquals(bowling([
        (3,7),
        (5,2),
        (4,1),
        (2,5),
        (5,3)
        ])
        , 42)

    def test_dois_spares_seguidos_49(self):
        """
        Ocorre spare em 2 rodadas seguidas
        """
        self.assertEquals(bowling([
        (3,7),
        (5,5),
        (4,1),
        (2,5),
        (5,3)
        ])
        , 49)
    
    def test_ultimo_spare_espera_uma_jogada_extra_55(self):
        """
        Ocorre spare em 2 rodadas seguidas
        """
        self.assertEquals(bowling([
        (3,7),
        (5,5),
        (4,1),
        (2,5),
        (5,5,4)
        ])
        , 55)
        
    
    
    


if __name__ == '__main__':
    unittest.main()
