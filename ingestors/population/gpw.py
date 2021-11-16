from osgeo import gdal

# from geotiff import GeoTiff
import struct
import sys

from ingestors.geotiff import GeotiffIngestor

class Gpw(GeotiffIngestor):
	def __init__(self, year=2020, filename=None):
        self.year = year
        super.__init__(self, filename)
