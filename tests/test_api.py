import unittest
from test_config import TestConfig
import requests


class TestApi(TestConfig, unittest.TestCase):

    def test_get_todos(self):
        
        # TODO
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
