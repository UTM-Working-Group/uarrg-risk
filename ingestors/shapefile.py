import fiona
from ingestors.ingestor import Ingestor

class ShapefileIngestor(Ingestor):
	def __init__(self, filename=""):
		self.filename = filename

	def read(self, bb):
        # Open a file for reading. We'll call this the "source."
        with fiona.open(self.filename) as src:
        
            # The file we'll write to, the "destination", must be initialized
            # with a coordinate system, a format driver name, and
            # a record schema.  We can get initial values from the open
            # collection's ``meta`` property and then modify them as
            # desired.
        
            meta = src.meta
            meta['schema']['geometry'] = 'Point'
        
            # Open an output file, using the same format driver and
            # coordinate reference system as the source. The ``meta``
            # mapping fills in the keyword parameters of fiona.open().
        
            # Process only the records intersecting a box.
            return src.filter(bbox=(bb[0], bb[1], bb[2], bb[3]))
