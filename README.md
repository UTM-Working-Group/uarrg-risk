# UARRG Risk

This repository is for risk analysis for the UA Risk Research Working Group.

## Requirements

sudo add-apt-repository ppa:ubuntugis/ppa
sudo apt-get install gdal-bin libgdal-dev
```

### Creating a `virtualenv`

```
python3 -m virtualenv --system-site-packages --python=python3 .env
```

### Using the `virtualenv`

```
source .env/bin/activate
```

## Testing

```
python -m unittest tests.population.test_gpw
```

## Risk metrics

### Wind

See references:

* [GDAL and GFS Wind speed](https://geoexamples.blogspot.com/2012/12/raster-calculations-with-gdal-and-numpy.html)

