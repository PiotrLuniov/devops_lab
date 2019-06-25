from unittest import TestCase

import task60


class TestTask(TestCase):

    def setUp(self):
        """Init"""

    def test_del_func(self):
        self.assertEqual(task60.del_func(3, 6), 3)
        self.assertEqual(task60.del_func(5, 6), 1)
        self.assertEqual(task60.del_func(2, 4), 2)

    def tearDown(self):
        """Finish"""
