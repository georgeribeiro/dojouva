import unittest
from convertion import convert

class TestConversao_numeric_unfield(unittest.TestCase):
    def test_passar_1_de_numerico_para_unrfield_retorna_1_barra(self):
        self.assertEquals(convert("1", "numerico", "unrfield"), "/")
        
    def test_passar_3_de_numerico_para_unrfield_retorna_3_barras(self):
        self.assertEquals(convert("3", "numerico", "unrfield"), "///")
    
    def test_passar_5_de_numerico_para_unrfield_retorna_1_barra_invertida(self):
        self.assertEquals(convert("5", "numerico", "unrfield"), '\\')
    
    def test_passar_7_de_numerico_para_unrfield_retorna_1_barra_invertida_2_normal(self):
        self.assertEquals(convert("7", "numerico", "unrfield"), '//\\')
        
    def test_passar_12_de_numerico_para_unrfield_retorna_2_barra_invertida_2_normal(self):
        self.assertEquals(convert("12", "numerico", "unrfield"), '//\\\\')
        
class TestConversao_unfield_numeric(unittest.TestCase):
    
    def test_passar_b_de_unrfield_para_numerico_retorna_1(self):
        self.assertEquals(convert("/", "unrfield", "numerico"), "1")
        
    def test_passar_3b_de_unrfield_para_numerico_retorna_3(self):
        self.assertEquals(convert("///", "unrfield", "numerico"), "3")
    
    def test_passar_1bi_de_unrfield_para_numerico_retorna_5(self):
        self.assertEquals(convert("\\", "unrfield", "numerico"), "5")
   
    def test_passar_1bi_e_2b_de_unrfield_para_numerico_retorna_7(self):
        self.assertEquals(convert("//\\", "unrfield", "numerico"), "7")
    
   
unittest.main()
      
