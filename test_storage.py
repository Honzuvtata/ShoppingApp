import unittest
import storage
from storage import generateId


class TestStorage(unittest.TestCase):
    def test_generateIdTestLen(self):
        randomId = generateId()
        self.assertEqual(len(randomId), 13)

    def test_generateIdIdPrefix(self):
        randomId = generateId()
        self.assertEqual(randomId[0:3], "id-")
