class CocaCola:
    calories    = 140
    sodium      = 45
    total_carb  = 39
    caffeine    = 34
    ingredients =  [     
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
        'Caffeine' 
    ]

    def __init__(self,logo_name):
        self.local_logo = logo_name    

    def drink(self):
        return self.calories

class CaffeineFree(CocaCola):
    caffeine = 0
    ingredients =  [
        'High Fructose Corn Syrup',
        'Carbonated Water',
        'Phosphoric Acid',
        'Natural Flavors',
        'Caramel Color',
    ]

coke_a = CaffeineFree('Cocacola-FREE')

coke_a.drink()

import unittest

class CaloriesTestCase(unittest.TestCase):
    
    def test_colarious(self):
        result = coke_a.drink()
        self.assertEqual(result, 140)


suite = unittest.TestLoader().loadTestsFromTestCase(CaloriesTestCase)
unittest.TextTestRunner().run(suite)
