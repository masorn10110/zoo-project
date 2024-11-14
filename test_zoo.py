import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()
    
    def test_initail(self):
        self.assertEqual(self.zoo.get_ticket_price(5), 50) # valid output
        
    # Add your additional test cases here.
    
    def test_invalid_input(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), None) # valid output

    def test_child_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50) # # invalid output, expect return 150 but actual return None, Now is valid output
        self.assertEqual(self.zoo.get_ticket_price(12), 50) # valid output
        
    def test_teen_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100) # valid output
        self.assertEqual(self.zoo.get_ticket_price(20), 100) # invalid output, expect return 100 but actual return None, Now is valid output
        
    def test_worker_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150) # invalid output, expect return 150 but actual return None, Now is valid output
        self.assertEqual(self.zoo.get_ticket_price(60), 150) # valid output
        
    def test_older_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100) # valid output

if __name__ == '__main__':
    unittest.main()