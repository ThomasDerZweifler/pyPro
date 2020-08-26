import unittest

# https://docs.python.org/3/library/unittest.html

class TestPlugin(unittest.TestCase):
    
    
    def test_plugin(self):

        module = __import__("plugin.moduleA", fromlist=[''])
        c = getattr(module,"Plugin")
        self.assertEqual(c().version(),"1.0.0")

        module = __import__("plugin.moduleB", fromlist=[''])
        c = getattr(module,"Plugin")
        self.assertFalse(c().version() == "1.0.0")

if __name__ == '__main__':
    unittest.main()