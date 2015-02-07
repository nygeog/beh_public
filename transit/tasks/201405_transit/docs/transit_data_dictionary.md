#Transit Stations Project Data Dictionary
This project includes transit stations across the United States from 1970 - 2010 at ten year increments. 
##Sections
###[Transit Tract Data](#transit_tract_data)
* [Percent of Tract Area within Radial buffer of Station](#pct_tract_area)

###[Station Distances](#station_distances)
###[Station Clusters](#station_clusters)
###[Tract City Distances](#tract_city_distances)
* [Tract City Distances Variables](#tract_city_distances_variables)

###[Census Data](#census_data)
* [Social Explorer](#social_explorer)
	* [Total Population](#se_tot_pop)
	* [Means Of Transportation To Work](#sse_transpo)


###[Project Projection Information](#project_projection_information)

#####Count of Station Data by Year
	1970 - 3,484
	1980 - 3,370
	1990 - 3,290
	2000 - 3,447
	2010 - 4,031

Tracts 2010 - input GDB n = 74,002

LTDB 2010 Population counts were verified to equal 2010 Census P0010001 data from demographic profile tract downloads. 

</br>
***
#<a name="transit_tract_data"></a>Transit Tract Data
***
####Filename: transit_tract_data.csv
#####[Sample of data](https://github.com/nygeog/sample_data/blob/master/transit/tasks/201405_transit/data/transit_tract_data.csv)
#####n = 74,002
***
####GEOID10
Census Tract 2010 unique identifier

####ALAND10
area of land in tract - (us census bureau generated)

####AWATER10
area of water in tract - (us census bureau generated)

####origtractarea
original tract area in meters (projected USA Contiguous Albers Equal Area Conic)

####csa_geoid
CSA (Combined Statistical Area) id - [CSA US Census Bureau](http://www.census.gov/geo/reference/gtc/gtc_cbsa.html); [CSA - Wikipedia](http://en.wikipedia.org/wiki/Combined_Statistical_Area)

Following text from US Census website - [Geographic Terms and Concepts - Core Based Statistical Areas and Related Statistical Areas](http://www.census.gov/geo/reference/gtc/gtc_cbsa.html)

Combined Statistical Areas (CSAs) consist of two or more adjacent CBSAs that have substantial employment interchange.  The CBSAs that combine to create a CSA retain separate identities within the larger CSA.  Because CSAs represent groupings of metropolitan and/or micropolitan statistical areas, they should not be ranked or compared with individual metropolitan and micropolitan statistical areas.

Core Based Statistical Areas (CBSAs) consist of the county or counties or equivalent entities associated with at least one core (urbanized area or urban cluster) of at least 10,000 population, plus adjacent counties having a high degree of social and economic integration with the core as measured through commuting ties with the counties associated with the core.  The general concept of a CBSA is that of a core area containing a substantial population nucleus, together with adjacent communities having a high degree of economic and social integration with that core.  The term "core based statistical area" became effective in 2003 and refers collectively to metropolitan statistical areas and micropolitan statistical areas.  The U.S. Office of Management and Budget (OMB) defines CBSAs to provide a nationally consistent set of geographic entities for the United States and Puerto Rico for use in tabulating and presenting statistical data.  Current CBSAs are based on application of the 2000 standards (published in the Federal Register of December 27, 2000) with Census 2000 data.  The first set of areas defined based on the 2000 standards were announced on June 6, 2003; subsequent updates have been made to the universe of CBSAs and related statistical areas.  No CBSAs are defined in the Island Areas.  Statistical areas related to CBSAs include metropolitan divisions, combined statistical areas (CSAs), New England city and town areas (NECTAs), NECTA divisions, and combined NECTAs.


####places_geoid
Places unique id

####places_name
Following text from US Census website - [Geographic Terms and Concepts - Place](https://www.census.gov/geo/reference/gtc/gtc_place.html):

Incorporated Places are those reported to the Census Bureau as legally in existence as of January 1, 2010, as reported in the latest Boundary and Annexation Survey (BAS), under the laws of their respective states.   An incorporated place is established to provide governmental functions for a concentration of people as opposed to a minor civil division, which generally is created to provide services or administer an area without regard, necessarily, to population.   Places always are within a single state or equivalent entity, but may extend across county and county subdivision boundaries.   An incorporated place usually is a city, town, village, or borough, but can have other legal descriptions.   For Census Bureau data tabulation and presentation purposes, incorporated places exclude:

* Boroughs in Alaska (treated as statistical equivalents of counties).
* Towns in the New England states, New York, and Wisconsin (treated as MCDs).
* Boroughs in New York (treated as MCDs).

####places_namelsad
Current name and the translated legal/statistical area description for place. Refer to the name in the 'NAME' (places_name) field and the translated legal/statistical area description code for place.
List of values:

* 00 - Blank* 21 - borough (suffix)* 25 - city (suffix)* 37 - municipality (suffix)* 43 - town (suffix)* 47 - village (suffix)* 53 - city and borough (suffix)* 55 - comunidad (suffix)
* 57 - census designated place (CDP) (suffix)* 62 - zona urbana (suffix)* CN - coporation (suffix)* MG - metropolitan government (suffix)* UC - urban county (suffix)* UG - unified government (suffix)
####places_lsad
Current legal/statistical area description code for place. 
####places_classfp
Current Federal Information Processing Series (FIPS) class code. List of values:
* C1 - An active incorporated place that does not serve as a county subdivision* C2 - An active incorporated place that is legally coextensive with a county subdivision but treated as independent of any county subdivision* C5 - An incorporated place that is independent of any county subdivision and serves as a county subdivision equivalent
* C6 - An active incorporated place that is coextensive with or approximates an Alaska Native village statistical area* C7 - An incorporated place that is independent of any county* C8 - The balance of a consolidated city excluding the separately incorporated place(s) within that consolidated government* C9 - An inactive or nonfunctioning incorporated place* M2 - A military or other defense installation entirely within a place* U1 -A census designated place with an official federally recognized name* U2 - A census designated place without an official federally recognized name* U5 - A census designated place that is coextensive with a county subdivision* U9 - A census designated place that is coextensive with or approximates an Alaska Native village statistical area


####places_pcicbsa
Current metropolitan or micropolitan statistical area principal city indicator
List of values:  
* N - Geographic entity is not a principal city of a CBSAEnumerated domain value definition source U.S. Census Bureau* Y - Geographic entity is a principal city of a CBSAEnumerated domain value definition source U.S. Census Bureau
####places_pcinecta
Current New England city and town area principal city indicatorList of values:  * N - Geographic entity is not a principal city of a NECTAEnumerated domain value definition source U.S. Census Bureau* Y - Geographic entity is a principal city of a NECTAEnumerated domain value definition source U.S. Census Bureau
####places_mtfccMAF/TIGER feature class codeList of values:  
* G4110 - Incorporated place* G4210 - Census designated place
####places_funcstat
Current functional statusDescription sourceU.S. Census BureauList of values  * A - Active government providing primary general-purpose functions* B - Active government that is partially consolidated with another government but with separate officials providing primary general-purpose functions* D - Defunct Entity* F - Fictitious entity created to fill the Census Bureau geographic hierachy* I - Inactive governemental unit that has the power to provide primary special-purpose functions* N - Nonfunctioning legal entity* S - Statistical entity

###Years of Transit stations
The years used in this study were 1970, 1980, 1990, 2000 & 2010. 

	YYYY = yearList = ['1970','1980','1990','2000','2010']

######When reading the variables please look for the variable <strong>YYYY</strong> wildcard and substitute with the appropriate year from the yearList.


###Modes of Transit station Types
The modes of transit each station has is represented by the following variable wildcard. 

The following subtypes were constructed: All types of transit, Commuter rail service, Heavy rail service, Light rail service, Streetcar service & Other kind of rail/fixed guideway service (includes people movers, aerial trams, and other miscellaneous types of transit that operate on their own right of way)

	** = typesList = ['al','cr','hr','lr','sc','ot']

####al
All types of transit 
####cr
Commuter rail service
####hr
Heavy rail service
#####lr
Light rail service
#####sc
Streetcar service
#####ot
Other kind of rail/fixed guideway service (includes people movers, aerial trams, and other miscellaneous types of transit that operate on their own right of way)


######When reading the variables please look for the variable <strong>**</strong> wildcard and substitute with the appropriate year from the typesList.


###Buffer Variables


###Count of Stations in Tracts

INSERT IMAGE OF COOUNT OF STATIONS IN TRACTS

####n_**YYYY_r
Raw count of transit station types (**) by Census Tract (2010) - no collapsing on whether stations are shared in location by year (YYYY)


###<a name="pct_tract_area"></a>Percent of Tract Area within Radial buffer of Station

<!--INSERT IMAGE OF TRACT AREA WITHIN 1 KM BUFFER OF STATION-->





####p_**YYYYb1
Percent of Census Tract (2010) within 1 km buffer of transit stations by type (**) and year (YYYY)

####p_**YYYYb2
Percent of Census Tract (2010) within 2 km buffer of transit stations by type (**) and year (YYYY)

###Zonal statistics of Tract Area from Station Kernel Density Grid
The Kernel Densities for each transit type were also done with different cell sizes and search radiuses (radii). Those variable prefixes are described below. These settings for cell sizes and search radius are in meters. 

	c%%% = cellSizes      = ['1000' ,'500' ,'250' ,'500' ,'250' ]
	s@@@ = searchRadiuses = ['10000','2000','2000','5000','5000']  

####d_YYYY**c%%%s@@@cnt
Count of raster grid cells for transit type (**) in the Census Tract (2010)
####d_YYYY**c%%%s@@@are
Area of grid cell valuesfor transit type (**) in the Census Tract (2010)
####d_YYYY**c%%%s@@@min
Minimum value of grid cell values for transit type (**) in the Census Tract (2010)
####d_YYYY**c%%%s@@@max
Maximum value of grid cell values for transit type (**) in the Census Tract (2010)
####d_YYYY**c%%%s@@@rng
Range of grid cell values for transit type (**) in the Census Tract (2010)
####d_YYYY**c%%%s@@@avg
Average (Mean) of grid cell values for transit type (**) in the Census Tract (2010)
####d_YYYY**c%%%s@@@std
Standard Deviation of grid cell values for transit type (**) in the Census Tract (2010)
####d_YYYY**c%%%s@@@sum
Sum of grid cell values for transit type (**) in the Census Tract (2010)

 <br />
***
#<a name="station_distances"></a>Station Distances
***
####Filename: transit_tract_data.csv
#####[Sample of data](https://github.com/nygeog/sample_data/blob/master/transit/tasks/201405_transit/data/station_distances_sample.csv) 
#####n = 62,432,404
***
####inputid
Station id for input station location
####nearid
Station id for near (calculated distance) station location
####dist_meters
Distance in meters (USA Contiguous Albers Equal Area Conic)
####year
Year of yearList = ['1970','1980','1990','2000','2010']

 <br />
***
#<a name="station_clusters"></a>Station Clusters
***
####Filename: 1970_all_stations_clusters.csv, 1980_all_stations_clusters.csv, 1990_all_stations_clusters.csv, 2000_all_stations_clusters.csv, 2010_all_stations_clusters.csv
#####[Sample of data](https://github.com/nygeog/sample_data/blob/master/transit/tasks/201405_transit/data/station_distances_sample.csv) 
#####n = ~4,000 depending on year.
***

####id
Station identifier
####year
Year of yearList = ['1970','1980','1990','2000','2010']
####agency
Station operating agency
####line
Line 
####name
Name
####latitude
Station latitude
####longitude
Station longitude
####msaregion
MSA region
####open
Open (1 yes, 0 no)
####cr_open
Open Commuter rail service (1 yes, 0 no)
####hr_open
Open Heavy rail service (1 yes, 0 no)
####lr_open
Open Light rail service (1 yes, 0 no)
####sc_open
Open Streetcar service (1 yes, 0 no)
####ot_open
Open Other kind or rail/fixed guideway service (1 yes, 0 no)
####sum_mode
Total count of modes (check with Kathy)

##Clusters
###Years of Transit stations
The years used in this study were 1970, 1980, 1990, 2000 & 2010. 

	YYYY = yearList = ['1970','1980','1990','2000','2010']

######When reading the variables please look for the variable <strong>YYYY</strong> wildcard and substitute with the appropriate year from the yearList.


###Modes of Transit station Types
The modes of transit each station has is represented by the following variable wildcard. 

The following subtypes were constructed: All types of transit, Commuter rail service, Heavy rail service, Light rail service, Streetcar service & Other kind of rail/fixed guideway service (includes people movers, aerial trams, and other miscellaneous types of transit that operate on their own right of way)

	** = typesList = ['al','cr','hr','lr','sc','ot']

###Distances of cluster tolerance

	DIST = distList = ['0050','0100','0250','0500']	
	
####uidYYYY**DIST
A unique cluster id for year (YEAR), modes of transit station type (**) and buffer distance (DIST).



INSERT IMAGE OF CLUSTER EXAMPLES


***






***
#<a name="tract_city_distances"></a>Tract City Distances
***
All data for these calculations were projected to USA Contiguous Albers Equal Area Conic (meters)

Since there is no clear City Center layer BEH-GIS compiled a few different point layers for calculating distance from Tract to city center. 
***
##A) Esri Detailed (cityesridtl)
###Metadata
######SummaryU.S. National Atlas Cities provides information about the locations, names, and populations of cities and towns for conducting geographic analysis on national and large regional scales.######DescriptionU.S. National Atlas Cities represents cities and towns in the United States. : Title U.S. National Atlas Cities : Creation date 2005-03-20 : Publication date 2012-03-01 : Edition 2012 : Edition date 2012-03-01 : Name Data & Maps for ArcGIS® : Issue 2012 - World, Europe, and United States

##B) Esri Detailed (cityesrimjr)
###Metadata
######SummaryU.S. and Canada Major Cities provides locations and attributes for the major cities.######DescriptionU.S. and Canada Major Cities represents major cities of United States and Canada including national, state, and provincial capitals. : Title U.S. and Canada Major Cities : Creation date 2005-05-25 : Publication date 2012-03-01 : Edition 2012 : Edition date 2012-03-01 : Series : Name Data & Maps for ArcGIS® : Issue 2012 - StreetMap™ North America



##C) CBSA for both 1) Centroid and 2) Population-weighted Centroid
###Metadata
######Summary
In order for others to use the information in the Census MAF/TIGER database in a geographic information system (GIS) or for other geographic applications, the Census Bureau releases to the public extracts of the database in the form of TIGER/Line Shapefiles.######DescriptionThe TIGER/Line shapefiles and related database files (.dbf) are an extract of selected geographic and cartographic information from the U.S. Census Bureau's Master Address File / Topologically Integrated Geographic Encoding and Referencing (MAF/TIGER) Database (MTDB). The MTDB represents a seamless national file with no overlaps or gaps between parts, however, each TIGER/Line shapefile is designed to stand alone as an independent data set, or they can be combined to cover the entire nation. Metropolitan and Micropolitan Statistical Areas are together termed Core Based Statistical Areas (CBSAs) and are defined by the Office of Management and Budget (OMB) and consist of the county or counties or equivalent entities associated with at least one urban core (urbanized area or urban cluster) of at least 10,000 population, plus adjacent counties having a high degree of social and economic integration with the core as measured through commuting ties with the counties containing the core. Categories of CBSAs are: Metropolitan Statistical Areas, based on urbanized areas of 50,000 or more population; and Micropolitan Statistical Areas, based on urban clusters of at least 10,000 population but less than 50,000 population. The CBSAs boundaries are those defined by OMB based on the 2010 Census and published in February 2013.
##D) CSA for both 1) Centroid and 2) Population-weighted Centroid
###Metadata
######SummaryIn order for others to use the information in the Census MAF/TIGER database in a geographic information system (GIS) or for other geographic applications, the Census Bureau releases to the public extracts of the database in the form of TIGER/Line Shapefiles.######DescriptionThe TIGER/Line shapefiles and related database files (.dbf) are an extract of selected geographic and cartographic information from the U.S. Census Bureau's Master Address File / Topologically Integrated Geographic Encoding and Referencing (MAF/TIGER) Database (MTDB). The MTDB represents a seamless national file with no overlaps or gaps between parts, however, each TIGER/Line shapefile is designed to stand alone as an independent data set, or they can be combined to cover the entire nation. Combined Statistical Areas (CSAs) are defined by the Office of Management and Budget (OMB) and consist of two or more adjacent Core Based Statistical Areas (CBSAs) that have significant employment interchanges. The CBSAs that combine to create a CSA retain separate identities within the larger CSA. Because CSAs represent groupings of CBSAs, they should not be ranked or compared with individual CBSAs. The CSA boundaries are those defined by OMB based on the 2010 Census and published in 2013.

####<a name="tract_city_distances_variables"></a>Tract City Distances Variables

####GEOID10	
Census Tract 2010 unique identifier
####distcityesridtl	
Distance (in meters) to nearest Esri Detailed city layer. 
####namecityesridtl
Name of nearest Esri Detailed city layer. 
####distcityesrimaj	
Distance (in meters) to nearest Esri Major city layer. 
####namecityesrimaj	
Name of nearest Esri Major city layer. 
	
####distcbsaflatcen	
Distance (in meters) to nearest CBSA Centroid. 
####namecbsaflatcen
Name of nearest CBSA Centroid. 	
####distcsa_flatcen
Distance (in meters) to nearest CSA Centroid. 	
####namecsa_flatcen
Name of nearest CSA Centroid. 	
####distcbsapopwcen
Distance (in meters) to nearest Population-weighted CBSA Centroid. 
####namecbsapopwcen
Name of nearest	Population-weighted CBSA Centroid
####distcsa_popwcen
Distance (in meters) to nearest Population-weighted CSA Centroid.
####namecsa_popwcen
Name of nearest	Population-weighted CSA Centroid

 <br />
 
 ***
#<a name="census_data"></a>Census Data
***



##vehicles in the household by tract would be good. I'll probably want to come back and get income data
Also grabbed travel time. 


No auto ownership for 1980 and 1990 and 2000 for Social Explorer (check US Census website). 1970 had 15% tables (not sure what these are).


Check US Census for 1990,2000,2010 (2008-2012 ACS) car ownership data

##<a name="social_explorer"></a>Social Explorer
Since the 1990 data from the US Census is difficult to obtain. The data used in this part of the project was obtained from Social Explorer (access provided by Columbia University). 

######[How do I cite information on Social Explorer?](http://www.socialexplorer.com/help/3067)


###<a name="se_totpop"></a>Total Population

###<a name="se_transpo"></a>Means Of Transportation To Work




<br />


***
#<a name="project_projection_information"></a>Project Projection Information
***
All data in this project is projected to USA Contiguous Albers Equal Area Conic (meters)

From Esri ArcGIS 10.1 Current Coordinate System Information:

	USA_Contiguous_Albers_Equal_Area_Conic	WKID: 102003 Authority: ESRI	Projection: Albers	False_Easting: 0.0	False_Northing: 0.0	Central_Meridian: -96.0	Standard_Parallel_1: 29.5	Standard_Parallel_2: 45.5	Latitude_Of_Origin: 37.5	Linear Unit: Meter (1.0)	Geographic Coordinate System: GCS_North_American_1983	Angular Unit: Degree (0.0174532925199433)	Prime Meridian: Greenwich (0.0)	Datum: D_North_American_1983  		Spheroid: GRS_1980    	Semimajor Axis: 6378137.0    	Semiminor Axis: 6356752.314140356    	Inverse Flattening: 298.257222101




<!---Hi Danny,

The attached spreadsheets include about 40% of the station data I have. The rest of the station data is mostly ready, but I held back any metro areas with incomplete data, which includes NYC, Phila, Boston, San Francisco, Pittsburgh, and the NJ Transit system. Each spreadsheet below includes a record for each station that was open in the relevant year. Ns are 638 for 1970, 650 for 1980, 911 for 1990, 1285 for 2000, and 1707 for 2010. 

The spreadsheets include the following variables for each station:

id - a new ID variable
year - the year the record is for
agency - the agency managing the transit line(s) stopping at that station
line - name of the line(s0 stopping at that station
name - name of the station (is not unique)
latitude and longitude
msaregion - I didn't use census boundaries to assign this -- it includes some stations that may fall outside of the relevant MSA. I grouped Baltimore and washington together as "Balt-Wash" because their transit systems overlap spatially and institutionally. You don't need to use this variable for anything but it's there in case it's useful for cleaning.
open - 1/0 variable indicating whether the station had any rail transit service in the relevant year
cr_open - whether the station had commuter rail service
hr_open - whether the station had heavy rail service
lr_open - whether the station had light rail service
sc_open - whether the station had streetcar service
ot_open - whether the station had some other kind of rail/fixed guideway service (includes people movers, aerial trams, and other miscellaneous types of transit that operate on their own right of way)
sum_mode - count of the number of modes (cr, hr, lr, etc) serving that station in the relevant year

Let me know if you have questions. I think the first thing we need to do is identify stations that are so close to each other that they are effectively one station and should be combined. I know there are at least a few of these in this data. If you can generate a list of stations that might potentially be collasped, we can talk about how to proceed.

Let me know if you have questions or need the datasets reformatted in some way. I exported these from stata and could send the stata dataset if that's preferable.

thanks,

Kathy
--->