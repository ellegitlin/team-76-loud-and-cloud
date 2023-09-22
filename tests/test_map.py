from unittest import TestCase
#from unittest.mock import MagicMock, create_autospec
from levelup.map import Map

class TestMap(TestCase):

    ##confirm map initialized
    def test_init(self):
        testMap = Map ()
        assert testMap.xMin == 0
        assert testMap.xMax == 9
        assert testMap.yMin == 0
        assert testMap.yMax == 9

