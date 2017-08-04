import unittest
from incarnation2 import MathMethod, Incarnation2

class TestIncarnation2(unittest.TestCase):
    
    def test_find_pi(self):
        pi_value = str(MathMethod().get_pi())
        self.assertEqual(pi_value, "3.1416")
     
        
    def test_find_alpha(self):
        alpha = Incarnation2().find_alpha()
        self.assertEqual(alpha, 2.31)
     
        
    def test_get_length_of_segment(self):
        seg_length = Incarnation2().get_length_of_segment(4)
        self.assertIsNotNone(seg_length)
      
        
    def test_get_none_length_of_segment(self):
        seg_length = Incarnation2().get_length_of_segment('4b')
        self.assertIsNone(seg_length)
        
        
if __name__ == '__main__':
    unittest.main()
        
