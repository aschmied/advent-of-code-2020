import unittest

from main import LastN

class TestLastN(unittest.TestCase):
    def test_add(self):
        last_n = LastN(2)
        self.assertEqual(len(last_n), 0)
        
        last_n.add(1)
        last_n.add(1)
        last_n.add(1)
        self.assertEqual(len(last_n), 2)

    def test_count(self):
        last_n = LastN(2)
        self.assertEqual(last_n.count(1), 0)

        last_n.add(1)
        self.assertEqual(last_n.count(1), 1)

        last_n.add(1)
        self.assertEqual(last_n.count(1), 2)

        last_n.add(1)
        self.assertEqual(last_n.count(1), 2)

    def test_in(self):
        last_n = LastN(2)
        self.assertFalse(0 in last_n)

        last_n.add(0)
        self.assertTrue(0 in last_n)

        last_n.add(1)
        self.assertTrue(0 in last_n)

        last_n.add(1)
        self.assertFalse(0 in last_n)
