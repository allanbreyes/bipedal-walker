import unittest
import numpy as np

from agent import Agent


class MemoryTest(unittest.TestCase):
    def testValidateExperience(self):
        agent = Agent('test', None)
        self.assertTrue(agent.validate_experience(np.array([0, 1, 2, 3, 4])))
