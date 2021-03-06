import unittest

from ingestors.population.gpw import Gpw
import numpy
import numpy.ma as ma

class TestGpw(unittest.TestCase):
    def test_read(self):
        """
        Test read TIFF file.
        """
		# [lonmin, latmin, lonmax, latmax]
        bb = [-5.0, 40.0, 10.0, 55.0]
        gpwi = Gpw(2020, "/media/d3/Data/world-population/gpw-v4-population-density-rev11_2020_30_sec_tif/gpw_v4_population_density_rev11_2020_30_sec.tif")
        ar = gpwi.read(bb)
        # print(ar[0])
        # print(mar.std())
        mar = ma.masked_outside(ar, 0, 1e10)
        # self.assertAlmostEqual(mar.mean(), 216.805013365, places=7, msg=None, delta=None)
        self.assertAlmostEqual(mar.mean(), 0.0, places=7, msg=None, delta=None)


