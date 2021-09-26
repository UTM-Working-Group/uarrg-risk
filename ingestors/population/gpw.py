from osgeo import gdal

# from geotiff import GeoTiff
import struct
import sys

from ingestors.ingestor import Ingestor

class Gpw(Ingestor):
	def __init__(self, year=2020, filename=""):
		self.year = year
		self.filename = filename

	def read(self, bb):
		self.f = gdal.Open(self.filename, gdal.GA_ReadOnly)
		band = self.f.GetRasterBand(1)

		# Compute x/y resolution in degrees
		resx = 360. / band.XSize
		resy = 180. / band.YSize

		# Define the geotransform used to convert x/y pixel to lon/lat degree
		# [lon_topleft, lon_resolution, lat_skew, lat_topleft, lon_skew, lat_resolution]
		geotransform = [-180, resx, 0.0,  90, 0.0, -1*resy]

		# The inverse geotransform is used to convert lon/lat degrees to x/y pixel index
		inv_geotransform = gdal.InvGeoTransform(geotransform)

		_x0, _y0 = gdal.ApplyGeoTransform(inv_geotransform, bb[0], bb[1])
		_x1, _y1 = gdal.ApplyGeoTransform(inv_geotransform, bb[2], bb[3])
		x0, y0 = min(_x0, _x1), min(_y0, _y1)
		x1, y1 = max(_x0, _x1), max(_y0, _y1)

		# Get subset of the raster as a numpy array
		data = band.ReadAsArray(int(x0), int(y0), int(x1-x0), int(y1-y0))

		return data

