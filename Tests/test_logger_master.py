import unittest
from Classes.logger_master import Logger_master
"""
[summary] 
*TDD implementation testing of our master_logger class
"""


class Test_logger_master(unittest.TestCase):
    """
    [summary]
    * setUp activates before each test method
    * tearDown activates after each test method (good for things that use a DB conn that needs closing etc.)
    """

    def setUp(self):
        test_loggerObj = Logger_master()

    def tearDown(self) -> None:
        # return super().tearDown()
        pass

    def test_i2c_addresses(self):
        self.assertEqual(True, False)

    def test_temp(self):
        self.assertEqual(True, False)

    def test_humidity(self):
        self.assertEqual(True, False)

    def test_co2(self):
        self.assertEqual(True, False)

    def test_TVOC(self):
        self.assertEqual(True, False)

    def test_moisture(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
