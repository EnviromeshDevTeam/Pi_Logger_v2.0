from Classes.enviromesh_logger import Enviromesh_logger
import unittest
import sys
sys.path.append("..")


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

    # Test temp recording in normal range
    def test_temp(self):
        self.assertTrue(self.test_loggerObj.getTemp() in range(0, 50))

    # Test humidity recording in normal range
    def test_humidity(self):
        self.assertTrue(self.test_loggerObj.getHumidity() in range(0, 100))

    # Test co2 recording in normal range
    def test_co2(self):
        self.assertTrue(0 <= self.test_loggerObj.getCO2() <= 8192)

    # Test Contaminant levels recording in normal range
    def test_TVOC(self):
        self.assertTrue(0 <= self.test_loggerObj.getTVOC() <= 1187)

    # Test Moisture levels recording in normal range
    def test_moisture(self):
        _moistValue, _moistVoltage = self.test_loggerObj.getMoisture()
        self.assertTrue(0 < _moistValue <= 1000)
        self.assertTrue(0 < _moistVoltage <= 5)


if __name__ == '__main__':
    unittest.main()
