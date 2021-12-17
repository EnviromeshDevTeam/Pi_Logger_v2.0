import unittest
from Classes.enviromesh_logger import Enviromesh_logger
"""
[summary] 
*TDD implementation testing of our master_logger class
"""


class test_enviromesh_logger(unittest.TestCase):
    """
    [summary]
    * setUp activates before each test method
    * tearDown activates after each test method (good for things that use a DB conn that needs closing etc.)
    """

    def setUp(self):
        self.test_loggerObj = Enviromesh_logger()

    def tearDown(self) -> None:
        pass
        # return super().tearDown()

    def test_temp(self):
        self.assertTrue(0 <= self.test_loggerObj.getTemp() >= 40)

    def test_humidity(self):
        self.assertTrue(0 <= self.test_loggerObj.getHumidity() >= 100)

    def test_co2(self):
        self.assertTrue(400 <= self.test_loggerObj.getCO2() >= 8192)

    def test_TVOC(self):
        self.assertTrue(0 <= self.test_loggerObj.getTVOC() >= 8192)

    # TODO: Once you find return values of this Analog sensor then implement test on the typle of ints
    def test_moisture(self):
        pass
        # self.assertTrue(True, False)


if __name__ == '__main__':
    unittest.main()
