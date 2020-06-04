import unittest
from algo_experts import my_module_1
from algo_experts import my_module_2


class TestMe(unittest.TestCase):
    def test_stuff(self):
       assert my_module_1.my_string == 'whoa, this is so kewl'
    def test_other_stuff(self):
      assert my_module_2.my_new_string == 'carl said: whoa, this is so kewl'

if __name__ == '__main__':
    unittest.main()