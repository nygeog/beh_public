#BEH Meeting
##20141117

####SPARCS
* We currently don't have a ZIP + 4 dataset. It might be in Business Analyst but will have to rebuild Rundle-008 (machine that Noelle was using when it crashed.)


####CPRC 
* Creating maps for Latino 



##20141111
10 am start. 

Karen Lee talk at 11 am. 

1. Shipped Sean the playgrounds by ZIP.
2. Finished Pollen Sites geoprocessing for NAAS. Next up is the grid. 
3. MSM AIDSVu 13+ age for rate and counts. 

Next meeting show traffic mxd and talk about. 
/Dropbox/GIS/Data/mxd/traffic_data_mxd_nys_esri.mxd



##20141028
####MSM
Shipped the tract dataset for all NYC tracts to them. 10/22

####Neighborhood Asthma and Allergy Study (NYC NAAS)
* Calculates a series of GIS variables for <strong>(a) the pollen sites</strong> (done)  and (b) a grid* (not done) across NYC. These variables are:
	* Complete for 50, 100, 250, 500, 1000 meters
		* Area calcs and land calcs
		* Tree canopy (2010 layer)
		* Elevation
		* Distance to nearest body of water
		
	* Incomplete
		* Building density
		* Traffic density (ask Steve)
	
####Nets
* Nets King County - need to verify UW Census data - some weirdness in their data
* [Nets Animations Updates](https://github.com/nygeog/beh_public/tree/master/nets/201410_animations)

####Rio
[Study Area Map](https://www.dropbox.com/s/ccyxq6pz8dfw3be/rio_study_area.png?dl=0)

I’ll ask a few of the high-res imagery providers for some quotes and what resolution they have available to see if we can do better than the WMS services.

[This is an example of Google’s resolution, which seems to be the best freely available.](https://www.dropbox.com/s/31pu8vy7nghhl7f/rio-geogle.png?dl=0)

###Upcoming Work
* GPS loggers on 200 Kids Children's Center, basically do PATS on children. 
* NYU
* Maps of social, built env., disease factors for their hospital catchment zone. Coming to speak with us on Nov. 11th. 
* NYRR Mighty Milers. Physical educaiton program. Where kids do a marathon 1 mile at a time. School based running program. Interested in evaluating the schools. Couple hundred thousand kids. Finding schools with a homeroom based champion. Will be getting this to Andrew. 
* Time estimates - Hospitalizations from SPARKS.




##20141013

###GIS
####Tree Pollen/New York City Neighborhood Asthma and Allergy Study (NYC NAAS)
* Received addresses from Kate Weinberger last week. 
* Had a conference call about the variables to create for the project. 
* I'm going to begin geocoding in next few weeks.
* Kate will work on solidifying the list of GIS variables I'll be creating. 
	
* #####Kate's Variables for NAAS

	* 1) Danny maps the 45 pollen sites on top of aerial imagery, Kate checks for accuracy (done)

	* 2) Danny calculates a series of GIS variables for (a) the pollen sites and (b) a grid* across NYC. These variables are:
	- Tree canopy (2010 layer)
	- Building density
	- Elevation
	- Distance to nearest body of water
	- Traffic density**

		The buffer sizes we will need for these variables are 0.05, 0.1, 0.25, 0.5, and 1-km radial buffers

	* 3) Kate develops land use regression model and kriged surface using the variables calculated by Danny in #2

	* 4) While Kate is working on the LUR and kriging, Danny geocodes the home and school addresses for NAAS subjects

	* 5) When Kate is done with the LUR and kriging, Danny calculates GIS variables around the NAAS subject addresses. These variables are:
	- Population density (2000 and 2010 census)
	- % poverty (2000 and 2010 census)
	- Median household income (2000 and 2010 census)
	- % park land
	- Traffic volume***
	- Black carbon and PM2.5 two-year averages from NYCCAS (Danny, Gina said you would have this data)

		The buffer sizes we will need are 0.25, 0.5, and 1-km radial buffers plus 1-km network buffers. 

		At this point we will also need to use the surface Kate develops to calculate pollen exposures for the NAAS addresses. 

####MSM
* have all of the vector analysis completed, ran the kernel densities this weekend. 
* complete all the kernel density table operations, just need to run and slightly modify the code to compile all the tables into a master dataset and review the output before sending. 
* I need James to create the vacancy metrics and the updated walkability




####NETS
* created a NETS animation of modified healthy food outlets. 
	* This category includes supermarkets, fruit and veggie markets, natural food stores, and fish markets. This indicator of healthy food access was developed for a BMI analysis, and has been modified slightly to include nut stores and fish markets for a fatty acids focus - if SMK=1 or FVM=1 or NAT=1 or FSH=1 
	
	* Here’s a smaller version. 
[For Download](https://www.dropbox.com/s/7vhcwkfruegp1e4/nets_modified_healthy_half.gif?dl=0)
[For Viewing Online](https://dl.dropboxusercontent.com/u/36281098/beh/nets/animation/nets_modified_healthy_half.gif)
	* And here’s a smaller one with a longer time period for each yearly snapshot. 
[For Download](https://www.dropbox.com/s/a7p09iwibft8sij/nets_modified_healthy_half_longer.gif?dl=0)
[For Viewing Online](https://dl.dropboxusercontent.com/u/36281098/beh/nets/animation/nets_modified_healthy_half_longer.gif)

#####Suggestions

Create just an animation of the kernel densities. 

Maybe try the search radius at 1/2 km instead of 1 km. 

Half households have car use a diff. search radius. 

Try physical.

Try in R. with Shiny. 

Show a new location opening. Colored by date of entry. 

Animated GIF Studio. 

Try scale with all 23 counties. 


####Restaurants
* Review restaurants paper. 

* Tanya shared some links:

	* [State health agency workforce shortages and implications for public health: a case study of restaurant inspections in Louisiana](http://www.ncbi.nlm.nih.gov/pubmed/24437047)
	* [Examination of the association between announced inspections and inspection scores.](http://www.ncbi.nlm.nih.gov/pubmed/24073484)
	* [Impact of internet posting of restaurant inspection scores on critical violations.](http://www.ncbi.nlm.nih.gov/pubmed/23858661)
	* [Public knowledge and attitudes regarding public health inspections of restaurants.](http://www.ncbi.nlm.nih.gov/pubmed/18471587)

##20141007

###GIS
####Tree Pollen
* 1) I should be receiving a set of addresses at 11:30 am today from Kate Weinberger for geocoding. This is in regards to the tree pollen study. This includes additional addresses to the enrollment address, which James geocoded (James total n is 588.), and school addresses.
	 * 350 other addresses. School addresses and post enrollment address. 45 monitoring sites. 
* 2) Kate will be sending out a wish list of variables.
	Tree, Traffic, Census, ask about Walkability, etc. NAAAS
* 3) Will we be getting the Black Carbon dataset (from NYCCAS) by a finer time interval (month/week) or should we just use the 2-year avg? #
	* point nearest to hoem

####MSM
* 4) Called up James yesterday, he created the jittered point shapefile. The jitter is a random point within the bounds of the tract the point fell in. Jamie Eagan did the map, so I’ll fire off a quick map to Bader.  
* 5) Started processing the dataset for MSM. Conservatively, early next week the file will be completed and ready to send out. 

####NETS
* 6) I’m going to also be creating some NETS maps for an animation of kernel densities of healthy food outlets this week. 

####GPS
* 7) Still have 1-2 full days of working on the GPS walks data. 

####Transit

* 8) Downloaded a few census variables about vehicle ownership

	* Since the 1990 data from the US Census is difficult to obtain. The data used in this part of the project was obtained from Social Explorer (access provided by Columbia University). 
	* No auto ownership for 1980 and 1990 and 2000 for Social Explorer (check US Census website). 1970 had 15% tables (not sure what these are).

	* Got Vehicle Ownership data from 2000 Census and 2008-2012 ACS. 

####Walkability Comments
* Rochdale/Locust Manor seems to be the biggest change. 

####Misc
* [Woods Hole US Biomass] (http://www.arcgis.com/home/webmap/viewer.html?webmap=f7535ebbb05b4eaf8ef019dbeb42be19)
This map represents year 2000 baseline estimate of above ground live dry biomass and standing carbon stock for the lower 48 United States.

* The accompanying dataset was produced as part of a project funded under NASA’s Terrestrial Ecology Program and titled “The National Biomass and Carbon Dataset 2000 (NBCD 2000): A High Spatial Resolution Baseline to Reduce Uncertainty in Carbon Accounting and Flux Modeling.” The main objective of the project was to generate a high-resolution (30 m), year-2000 baseline estimate of basal area-weighted canopy height, aboveground live dry biomass, and standing carbon stock for the conterminous (lower 48) United States. Development of the dataset is based on an empirical modeling approach that combines USDA Forest Service Forest Inventory and Analysis (FIA) data with high-resolution InSAR data acquired from the 2000 Shuttle Radar Topography Mission (SRTM) and optical remote sensing data acquired from the Landsat ETM+ sensor. Three-season Landsat ETM+ data were systematically compiled by the Multi-Resolution Land Characteristics Consortium (MRLC) between 1999 and 2002 for the entire U.S. and were the foundation for development of both the USGS National Land Cover Dataset 2001 (NLCD 2001) and the Landscape Fire and Resource Management Planning Tools Project (LANDFIRE). Products from both the NLCD 2001 (landcover and canopy density) and LANDFIRE (existing vegetation type) projects as well as topographic information from the USGS National Elevation Dataset (NED) are used within the NBCD 2000 project as spatial predictor layers for canopy height and biomass estimation. Forest survey data provided by the USDA Forest Service FIA program were made available to the project under a national Memorandum of Understanding. The response variables (canopy height and biomass) used in model development and validation were derived from the FIA database (FIADB). Production of the NLCD 2001 and LANDFIRE projects was based on a mapping zone approach in which the conterminous U.S. is split into 66 ecoregionally distinct mapping zones. This mapping zone approach was also adopted by the NBCD 2000 project. 

* Biomass 30m resolution. Digital numbers are in megagrams (Mg) of Aboveground Live Woody Biomass per Hectare (Mg/Ha)



---
##20140930

#####Healthy Food Outlets PAA
* That would be really interesting and perhaps with buffers or kernel densities we could answer/investigate whether the lasso subset selection differently identifies significant characteristics/interactions based on the different spatial measures of food access, and verify/measure improvements in model predictive accuracy. David

* On Thu, Sep 25, 2014 at 1:52 PM, Lovasi, Gina S. 
I think that would be great.  Maybe we could even animate a series of kernel density surfaces across the years?  Anyway, fingers crossed.








##20140923

* Geocode addresses Perzonowski

* And School addresses

* Kate will be sending out a wish list of variables.
* 5%
* Tree, Traffic, Census, ask about Walkability, etc. 
* NAAAS

* enrollment addresses have been geocoded. check with James. 

* Ask Andrew about the Black Carbon dataset by week. 

* 5 rounds. Have James send some stuff. 

* James total n is 588. 

* 350 other addresses. School addresses and post enrollment address. 45 monitoring sites. 


##20140916

1) Wrapped up ATN Aidsvu new data incorporation and data dictionary updates

The pre-2014-09 file only had 274 ZIP code to AIDSVu ZIP’s matches (AIDSVu uses ZCTA 2010). 224 new records now have AIDSVu ZIP level data. 498 ATN ZIP Codes matched an AIDSVu ZIP (AIDSVu uses ZCTA 2010).

2) Sent kathy the 2km buffers for transit and the distance variables. 

3) Need to reply to Vijay for MSM

Complicated enough to have access to their data. 

craft email for MSM and then forward to Andrew before sending to Vijay. 

Add in the latest GPS data with older summer data. 

Ask students which phones they have. 



Getting Addresses from Jose Luchsinger and Dana March.
EPA and NIMHD



##20140902

M2M

how many respondents per tract? 

or how many respondents per UHF?

Tell M2M that bader is going to look at the distribution of the data.

The initial idea is to creat a krigged surface of self reported safety (a surface for each subject minus their actual point)

figure out how clustered the sample. 

get James' status maps. by neighborhood tabulation areas. 




WIC document. 


Transit
Station buffer - what would be the buffers. 









##20140812

Earth Institute - fracking 3 counties - PA, 3 counties - NY - non fracking area

Hopkins - Fracking - Brian Schwartz



NETS biz count total - bring them into the NETS tract database as 0.

*********
send andrew the dataset with the zero's added in and add Kathy's pop density data.
*********

flagged - flagged as potentially health relevant. 

flagged column all the businesses. that were flagged. 


email. 


Send Joe's GPS data to Andrew.






last meeting:

Sally Finley WIC kids

characterize n'hood around WIC centers and WIC participants (NY statewide).

2010. Walk score(? upstate). All State ZIP codes. Daycare. licensure for daycare facilities. 


Community Needs Assessment, Health care, Built Environment.

*******Check time of crash accident from Crash Stat data.*********

Also, here is an updated Tree Canopy (pct of roadbed/sidewalk covered in tree canopy in census block (shared street boundary) of at least 1000 feet) Walk map. I’ll need to remove islands (particularly Rikers :) and perhaps places X distance from any Subway Station before the final selection.
http://cdb.io/1zYHBWd

Some things to consider for discussion tomorrow for Tree and Building walks. 

1) Do we want the students to walk down each segment once or twice? (Joe did two of each).

2) Do we want to randomly select across all boroughs or select within proximity of Columbia/Univ.?
Trees and Manhattan and the Bronx. 

3) How many walks? 
20
4) Include/Remove parks? (we discussed removing parks for high/low building walks but not for tree canopy).
Remove streets adjacent to parks. 

Lastly, I was contacted by a Geography major senior at New Paltz (Roz from ISERP’s younger brother-in-law) about possibly working for BEH. He might be able to be leveraged for some GPS work and possibly some GIS work. I spoke with him on the phone before my vacation. Attached is his resume.

GIS Plate
1) Any update with the COHD data I was supposed to receive from Luchsinger and March? 
2) Planning on getting data from Kathy at the end of this week. 
3) I'll be out on vacation on Friday - wedding in Kansas City. Heard to test out the wifi and the BBQ. 
4) Intern from SUNY New Paltz


Horizon
1) Estimating traffic across NYC, not sure if this is falling in James' queue or mine or where we stand on it. 
2) Registering for Probability and Stats in the fall (teacher: John Cunningham from Stats)


CartoDB.

I have 3 accounts with at least 20 tables. May be violating academic account privelege. 

John Snow
$429 yearly 
20 tables
200 MB of data

Mercator
$1299 yearly
Unlimited tables
500 MB of data



From 
##20140702


Make animation of Joe's Battery gps

1-26 flags nets

1990, 2000, 2010 cuts

collapsed

summed for each 2010 tract. for each 26 business categories.

economic census by county 1992.

Perzonowski
Geocoding, residential history



To Do: 

a) Take a look to limit the 35 MB file that Tanya sent. 
b) Take a look at PIPS data - XML (James).

-------
-------

1) Roz former ISERP younger brother looking for GIS internship/work for this summer

2) Einsten NETS food environment NYC 2010 Food Env.
Is this done?: sent Tanya the pop dens. tract vars for the 23 counties

3) I’m off 4 of the next 9 days so I’ll be a little touch and go.

4) This week - started refining the building and tree canopy based walks from the maps I sent out. Have to re-write some tree based stuff b/c intersects not working. Shouldn’t be a problem, just threw too much at ArcGIS.

5) Other stuff on my plate includes; Kathy’s Transit projects, revisiting some of the kernel density metrics

6) Review Tanya’s NETS methods paper.

7) Stuff on the horizon, Steve’s traffic counts for NYC. 

8) Any update with the COHD data I was supposed to receive from Luchsinger and March? 
