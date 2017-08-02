import unittest
import numpy as np

from memory import Memory


class MemoryTest(unittest.TestCase):
    def testStore(self):
        validator = lambda x: x == 'foo'
        memory = Memory(validator=validator)
        self.assertTrue(memory.store('foo'))
        with self.assertRaises(ValueError):
            memory.store('bar')

    def testGetBatch(self):
        np.random.seed(0)
        memory = Memory(minlen=2)
        with self.assertRaises(ValueError):
            memory.get_batch(1)

        memory.store('foo')
        with self.assertRaises(ValueError):
            memory.get_batch(1)

        memory.store('bar')
        self.assertEqual(memory.get_batch(1), ['foo'])
