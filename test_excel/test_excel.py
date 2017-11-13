import unittest



class TestHello(unittest.TestCase):
    """sample test"""

    def test_world(self):
        """sample test"""
        self.assertEqual('hello world', 'hello world')

    def test_world_unicode(self):
        """sample test with unicode"""
        self.assertEqual(u'hello world', u'hello world')