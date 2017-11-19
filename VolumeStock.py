import osgeo.ogr
import gdal
import struct
import statistics
import vertex 
from cliprasterpol import clip_raster

def volume(DEM, Contour):
	src_ds=gdal.Open(DEM)
	gt=src_ds.GetGeoTransform() 
	rb=src_ds.GetRasterBand(1)
	gdal.UseExceptions()
	coords=[(entry[0],entry[1]) for entry in vertex.rings(DEM, Contour)]
	GSD=gt[1]
	volume=0
	med=statistics.median(entry[2] for entry in vertex.rings(DEM, Contour))
	clip=clip_raster(DEM, Contour, gt=None, nodata=-9999)
	print( 'volume', ((clip-med)*GSD*GSD)[clip!=-9999.0].sum(), 'm3')
	
if __name__ == '__main__':
	DEM ='D:\stock_mask\mosa_dsm.tif'
	shapes= 'D:\stock_mask\stock1.shp'
	volume(DEM, shapes)
#1,5s