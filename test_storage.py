import unittest
import storage
from storage import generateId

testData1 = [
    {"itemId": "itemId-PAW6KCL8TD", "name": "banana", "count": 1},
    {"itemId": "itemId-WX0B8MGP36", "name": "ham", "count": 3},
]


class TestStorage(unittest.TestCase):
    def test_generateIdTestLen(self):
        randomId = generateId()
        self.assertEqual(len(randomId), 17)

    def test_generateIdIdPrefix(self):
        randomId = generateId()
        self.assertEqual(randomId[0:7], "itemId-")

    def test_checkDuplicityNameExist(self):
        result = storage.checkDuplicity("ham")
        self.assertEqual(result, "itemId-WX0B8MGP36")

    def test_checkDuplicityNameNonExisting(self):
        result = storage.checkDuplicity("aaaaa")
        self.assertEqual(result, False)
