#BEH Review Meeting 20150502 Items

* ###1) Scoping & Estimating projects and Work Queue 
	* I'd like to have a better handle on projects and tasks. As discussed in the past, having a solid time estimate and scope of work is very useful in managing time and effort and completing tasks in a timely fashion. 
	* A few examples where this has broken down;
		* Fragile Families Neighborhood Disorder - March 2013
		* NETS - 2013
		* NAAS - pollen sites, grid variables - Fall 2014
		* SPARCS - ZIP code vs. ZIP+4 - time spent developing ZIP+4 for certain time periods. 
			* not sure where this project stands. 
		* RdP - 2015
			* going forward I think all tasks should be scoped out and estimated for this project.  

* ###2) Continuing Education/Training/Conferences/Teaching 
	* a) I’d like to continue data science courses this fall and possibly some short courses when possible.
		* 1) Mobile Dev Bootcamp at General Assembly $65, 
			* possibly Mobile Development track in 2016 after Data Science Cert., see Mobile Dev below, 
		
	* b) Conferences
		* 1) [PyData](http://seattle.pydata.org/)
			* July 24-26, 2015, Seattle
			* [$150 as student or $250 - 300 as individual](http://www.eventbrite.com/e/pydata-seattle-2015-tickets-16360608019?ref=ebtnebregn) 
			* Plus airfare ($300-500)
		* 2) I’d like to consider [FOSS4G or FOSS4G - North America](http://foss4g.org/) in 2016. 	

	* c) Teaching	
		* 1) I've had offers to instruct at Pratt SAVI and may do so after completing the Data Science certificate so long as there are not any conflicts.  
		* 2) Reached out to Gina two weeks ago about what I need to do to set up a GIS workshop in Brazil around June, July, August.
		

* ###3) Salary and Professional Development 
	* Unless any catastrophes with the Algorithms course or Machine Learning, I’m dedicated to completing the Data Science Certificate program thru May 2016. During or after that I would like to keep growing skills and my toolbox while maintaining a match of salary to skill set and work/life balance. 
	* I think the time I spend helping graduate students and other unfunded work that exceeds the standard work week might be better well spent doing more paid outside work, instruction, professional development and freelance work. 
		* A GIS Librarian at NYU wanted to put me in touch with someone at NYU about doing some contract GIS work. It sounded fairly lucrative but a possible conflict with BEH's aims. For whom and what work can I do outside of BEH? Do I have to disclose all my work outside of Columbia? 
	* If Columbia cannot meet my salary/benefits requirements, we should discuss hiring/training a replacement and best ways for me to wrap. 

* ###4) Specific Projects and Requests
	* #####a) Developing a GPS cleaning/snapping/standardization python module
		* This would align with a few projects and think could contribute this to the open source stack as only a .NET solution exists that snap/clean with OSM data. 
		* Best Guess: 2-3 weeks.  

	* #####b) Getting the BEH GIS NYC Data portal up and running
		* I think this would benefit to be scheduled in as a small project, its not a crazy amount of work, but it demands time for full-on attention. 
		* [Latest prototype](http://beh-gis.github.io/pages/cartodb/) - could be done w/ D3 if we think D3 is more elegant. Could call CartoDB database and map the geojson w/ D3. 
		* Best Guess: 2 weeks. More time cleaning up/BEH reviews of interface.  

	* #####c) Variable-name Standardization
		* For getting further along with the data portal and just to standardize things across the board at BEH, I’d like to set aside some time where James and I can spend a few days really hammering down a BEH standard variable naming convention. We’ve talked about this on the phone for a bit a few weeks ago and both agree it would be worthwhile. This is something we could have/should have done a year or two ago. Now that we’ve developed a better handle on all these new ACS releases, we might even be better equipped to take this on. 
		* I’m not sure when James can be in NY or will have the time to Google Hangout or whatever, but I think 8-12 hours or so would get us to a really great place for standardizing variable names (at least for demographic data to start). 
		* We’d also generate some code to make it easier to crosswalk pre-standard variable names to BEH standardized (this last bit is required for the BEH GIS NYC Data portal anyway). 
		* Best Guess: 8-12 hours for commonly used built and Census Variables

	* #####d) Setting up a PostGIS back-end environment
		* For these larger data projects, it would be useful to set aside some time for developing a PostGIS backend production environment for geoprocessing. NAAS grid (84,000 100m grid points buffered at 5 distances with crazy overlap), NETS, GPS projects, could all greatly benefit from PostGIS. I’ve been integrating more and more GDAL/OGR and other open-source stuff into my workflow and its returns on processing data quicker are really worthwhile. This could also be a lead-in to developing a tool that would allow users to create PostGIS tables of x,y's and then run geoprocessing scripts w/ SQL in a more automated fashion. 
		* Best Guess: 2-3 weeks or build in the hours here and there into some projects.
		* Alternative Options - CartoDB
		* If we weren’t concerned about data security or could set up a secure cloud instance, this would much easier to do on CartoDB. So another, maybe preferable, option is to chat with the folks at CartoDB about setting up a HIPAA/IRB compliant CartoDB stack for BEH. 

	* #####e) Hardware 
		* I’ve accumulated a lot of large data files and project directories working on a few projects since adding a few new drives last year and archiving older projects. I’m not totally sure about backing everything up on the server (not all BEH folder members having IRB clearance for all projects on my drives, and general concern about its reliability and ability to retrieve backups). 
		* I think 2 4-TB drives would be good for 2015-2016, especially if we plan on working on any more NETS or big data projects. 
			* ~$300 

	* #####f) Software
		* My 4 CartoDB accounts (dif. emails) were at full capacity in March so I purchased an higher Academic account (next one up from the free tier). I’ve been paying $42.47 per month (have paid so far ~$117 with $10 credit for March) since March. If its possible I’d like to get some support for this cost. 
			* [CartoDB pricing](https://cartodb.com/pricing/)
			* $1649 year for Coronelli plan - $3299 for Mercator plan, likely able to get an academic discount. 
			* Enterprise $7000 year commercial - could likely get academic discount. It may be possible to build HIPAA/IRB compliant tools and services with this. 1 TB. Could process national nets or other projects on this, using CartoDB's PostGIS. 
	* #####g) Secure FTP Server
		* We need something to be able to send data that is approved by CUIT.
		* Cost: ? 

	* #####h) [Census API Tool](https://github.com/nygeog/census_api)
		* Would like to build some better Census API scripting tools for scraping and share with the open source community. 
		* Best Guess: 1 week
	
	* #####i) Mobile Dev
		* More long term (2-3 years, if staying with BEH can work out), would like to think about developing for mobile devices for data collection and Apple’s [ResearchKit](https://www.apple.com/researchkit/) specifically. 

* ###5) Feedback
	* I’d also like to hear more from you both about what James and I could be doing to help better facilitate getting more projects and completing projects efficiently. Perhaps it could also be useful to establish specific milestones over the next year.

