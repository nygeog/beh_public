#Tree Pollen Sites and Grid Geoprocessing
##To Do
* create building density illustration

* Traffic density - wait for Kate W. to reply 
* Copy Esri Traffic Data
* Copy NYS DOT Data 1
* Copy NYS DOT Data 2



##Done
* Copy input pollen data
* Project input pollen data
* Buffer Pollen Sites
* copy tree canopy data 
* copy elevation data use (DEM) I think thatts from James
* Zonal stats for elevation
* near distance to body water
* calc pct tree canopy
* copy elevation data use (DEM) I think thatts from James
* create a boro boundary clipped neighborhood geography
	* FOR THIS CYLCE THROUGH< ITERATE THROUGH INDIVIDUAL FEATURES ID, Explode, Select only features that intresect with point
* pt level elevation to point pollen points. 
* create building density metric
* find near angle image and documentation for near distance to water

	
	
[NYC Open Data 1 foot LIDAR Derived Elevation Model](https://data.cityofnewyork.us/City-Government/1-foot-Digital-Elevation-Model-DEM-/dpc8-z3jc?category=City-Government&view_name=1-foot-Digital-Elevation-Model-DEM-)	
	
	
###Kate's Notes

2) Danny calculates a series of GIS variables for (a) the pollen sites and (b) a grid* across NYC. These variables are:
	
* Tree canopy (2010 layer)
* Building density
* Elevation
* Distance to nearest body of water
* Traffic density**

The buffer sizes we will need for these variables are 

* 0.05
* 0.1
* 0.25
* 0.5
* 1-km radial buffers


##Variables List

For points (getting elevation data)
Extract Values to Points
Interpolate values at the point locations (optional)Specifies whether or not interpolation will be used.
Checked—The value of the cell will be calculated from the adjacent cells with valid values using bilinear interpolation. NoData values will be ignored in the interpolation unless all adjacent cells are NoData. 

NYC DEM 10ft raster elevation values are in feet. 

######siteid
The pollen site unique identification number. Provided by Kate Weinberger
######longitude
The pollen site longitude value in decimal degrees. 
######latitude
The pollen site latitude value in decimal degrees. 
######pr0050morigsqmtrs
The pollen site neighborhood geography 50 meter buffer original area (including areas over water) in square meters. 
######pr0050mlandsqmtrs
The pollen site neighborhood geography 50 meter buffer land area (water areas removed) in square meters. 
######pr0100morigsqmtrs
######pr0100mlandsqmtrs
######pr0250morigsqmtrs
######pr0250mlandsqmtrs
######pr0500morigsqmtrs
######pr0500mlandsqmtrs
######pr1000morigsqmtrs
######pr1000mlandsqmtrs
######waternearangle
The angle to the nearest water body.

From Esri [Near Analysis](http://resources.arcgis.com/en/help/main/10.1/index.html#//00080000001q000000)

	Specifies whether the near angle values in decimal degrees will be calculated and written to a new field, NEAR_ANGLE. A near angle measures from the x-axis (horizontal axis) to the direction of the line connecting an input feature to its nearest feature at their closest locations, and it is within the range of 0 to 180 or 0 to -180 decimal degrees - 0 to the east, 90 to the north, 180 (-180°) to the west, and -90 to the south.

![img/near.png](img/near.png)
######waternearfeet
The distance to the nearest body of water in feet. 
######waternearmeters
The distance to the nearest body of water in meters. 
######pr0050mtreecsqmtrs
The amount of tree canopy area in the 50 meter buffer geography area in square meters.  
######pr0100mtreecsqmtrs
######pr0250mtreecsqmtrs
######pr0500mtreecsqmtrs
######pr1000mtreecsqmtrs
######pr0050mtreecpctorig
The percent of neighorhood area of the neighborhood geography 50 meter buffer original area (including areas over water) covered by tree canopy.
######pr0050mtreecpctland
The percent of neighorhood area of the neighborhood geography 50 meter buffer land area (water areas removed) covered by tree canopy.
######pr0100mtreecpctorig
The pollen site neighborhood geography 50 meter buffer original area (including areas over water) in square meters. 
######pr0100mtreecpctland
######pr0250mtreecpctorig
######pr0250mtreecpctland
######pr0500mtreecpctorig
######pr0500mtreecpctland
######pr1000mtreecpctorig
######pr1000mtreecpctland

##Elevation metrics
New York City 10 foot elevation as provided by James Quinn. 

Can also add the 1 foot elevation as well. 

Zonal statistics as table for land area.
######pr0050melevcount
The pollen site neighborhood geography 50 meter buffer land area (water areas removed) count of elevation raster grid cells contributing to the zonal statistics. 
######pr0050melevmin
######pr0050melevmax
######pr0050melevmean
######pr0050melevstd
######pr0100melevcount
######pr0100melevmin
######pr0100melevmax
######pr0100melevmean
######pr0100melevstd
######pr0250melevcount
######pr0250melevmin
######pr0250melevmax
######pr0250melevmean
######pr0250melevstd
######pr0500melevcount
######pr0500melevmin
######pr0500melevmax
######pr0500melevmean
######pr0500melevstd
######pr1000melevcount
######pr1000melevmin
######pr1000melevmax
######pr1000melevmean
######pr1000melevstd
######pr0050mbldgvol
######pr0100mbldgvol
######pr0250mbldgvol
######pr0500mbldgvol
######pr1000mbldgvol
##Building Bulk
###Google Earth screenshot
![img/ge.png](img/ge.png)
###Building and neighborhood geography
![img/3dbldg.png](img/3dbldg.png)
###Building Volume Spread over the entire neighborhood
![img/bulk.png](img/bulk.png)
######pr0050mbldgbulkorig
######pr0050mbldgbulkland
######pr0100mbldgbulkorig
######pr0100mbldgbulkland
######pr0250mbldgbulkorig
######pr0250mbldgbulkland
######pr0500mbldgbulkorig
######pr0500mbldgbulkland
######pr1000mbldgbulkorig
######pr1000mbldgbulkland