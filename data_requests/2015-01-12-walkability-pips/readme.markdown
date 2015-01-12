#Data Request - BEH Walkability, Parks Inspections data

If I recall correctly, you're trying to use ZIP or ZCTA for your neighborhood definition. If that is the case you can use **area weighted apportionment** with these geographies to come up with your ZIP values. If you're not sure how to do this your GIS instructor should be able to help out. 



##BEH Tract Walkability
Link to csv

Link to Data Dictionary

[Link to NYC Department of City Planning - Tracts Shapefile](http://www.nyc.gov/html/dcp/download/bytes/nyct2010_14d.zip)
Note: NYC DCP's Tract file has 2,166 Tracts, our BEH dataset uses 2,164. The two missing tracts are water/piers. Drop them from the Tracts shapefile. 

##Park Inspection data
Our Park inspection data shapefile is only current up to 2006. I could share that with you. But more likely you'd want to use the more current data from NYC Open Data. It's an XML file so you'd have do some data carpentry to get that to join with the actual Parks data. **ParkId** is the field you'd want to use. 


####Park Inspections data
[Park Inspections Data XML](https://data.cityofnewyork.us/Housing-Development/Parks-Inspections-data/t9jy-gfev)

The Parks Inspection Program (PIP) is a comprehensive, outcome-based performance measurement system that generates frequent, random, and detailed inspections of our parks and playgrounds. A team of inspectors conducts nearly 5,000 inspections per year. Each site receives a rating of "Acceptable" or "Unacceptable" based upon the condition of specific park features.

####Parks boundary file
[Parks (Shapefile)](https://data.cityofnewyork.us/City-Government/Parks-Properties/rjaj-zgq7)

Directory of Parks Properties

* [Direct Download of the Parks (Shapefile)](https://data.cityofnewyork.us/api/geospatial/rjaj-zgq7?method=export&format=Shapefile)

---

<!--Daniel,

Thanks so much for getting back to me. Could you give me an idea of what to expect from the dataset-- eg. what variables does it contain, what is the geography involved?

I really appreciate it.

Best,
Melina

On Wed, Jan 7, 2015 at 8:38 AM, Daniel M Sheehan <dms2203@columbia.edu> wrote:
Kathy, James and I had a call yesterday and will be talking again at the end of the week. I have Melina's dataset in my queue. I hope to get it out early next week. 

On Tue, Jan 6, 2015 at 1:25 PM, Kathryn M. Neckerman <k.neckerman@gmail.com> wrote:
Hi Melina,

I'm copying in Danny Sheehan, one of our GIS analysts, who is working on producing a "public use" version of our built environment data.

Danny:  we talked about this request before - Melina is a senior at Barnard who was interested in some neighborhood measures to complement her data on family and household characteristics for kids in Early Head Start. 

We had originally talked about providing some data mid-January, but it sounds like the full-scale public use dataset won't be ready by then. I wonder if there's a fallback response - if there's a way to pull a few variables (walkability, park access and quality) that might be especially relevant for young kids, from existing datasets with measures defined at the zip or tract level? If I have this right, these are background measures and not the focus of Meilna's project, so they could be very simple. What do you think?

Thanks

K

On Tue, Jan 6, 2015 at 1:12 PM, Melina Iacovou <mi2280@barnard.edu> wrote:
Hi Dr. Neckerman,

Happy New Year! I figured I'd check in regarding the data request post-team meeting. 

Thanks so much,
Melina 

On Thu, Dec 18, 2014 at 4:46 PM, Kathryn M. Neckerman <k.neckerman@gmail.com> wrote:
Ok, I've send this schedule info to our GIS person.

K

On Thu, Dec 18, 2014 at 4:44 PM, Melina Iacovou <mi2280@barnard.edu> wrote:
Dr. Neckerman,

Great, thank you so much. I'd say I'll need it latest mid-January. If I could have the data soon after that team meeting, that'd be ideal. That way I can focus on understanding the datasets and manipulating them before other thesis data collection begins at the start of the Spring semester. 

Thanks again,
Melina 

On Thu, Dec 18, 2014 at 4:35 PM, Kathryn M. Neckerman <k.neckerman@gmail.com> wrote:
Hi Melina,

I think we're talking about either zip code level or tract level. We will provide you with the data but with the holidays things have slowed down a bit -- we won't have another team meeting till Jan 6.

What's your timeframe - when do you need the data?

Kathy

On Thu, Dec 18, 2014 at 4:04 PM, Melina Iacovou <mi2280@barnard.edu> wrote:
Hi Dr. Neckerman,

I hope this e-mail finds you well. I've read over the literature you sent with the dataset descriptions- it was really helpful context. 

Park proximity was evaluated by measuring from the addresses of the 13,000 participants, but in terms of datasets for average park area and quality within a zip code-- is there anything that the Built Environment and Health Research group has done/can share? 

As for the article on walkability and poor/non-poor disparities, I see that safety has its own subset of data points. Is there an aggregate metric available for safety? If not, are the 6 variables each separately available on a zip-code level? 

If park area/quality & safety related datasets are available at that geography, that would be wonderful. Please let me know. 

Thanks so much,
Melina 

On Tue, Dec 9, 2014 at 3:23 PM, Kathryn M. Neckerman <k.neckerman@gmail.com> wrote:
Ok, I'll follow up.

On Tue, Dec 9, 2014 at 3:20 PM, Melina Iacovou <mi2280@barnard.edu> wrote:
Hi Dr. Neckerman,

Thank you for the quick reply and the papers. I am hoping to do some GIS analysis over the winter/holiday break before the start of the Spring semester in late-January when I need to begin the other aspects of data collection for my thesis. 

I would just like the datasets if they are available/shareable with Columbia students, so I can compare the indices your group has created to the Early Head Start locations throughout the city, as well as some public health data on obesity and physical activity. 

Thanks so much,
Melina 

On Tue, Dec 9, 2014 at 3:14 PM, Kathryn M. Neckerman <k.neckerman@gmail.com> wrote:
I will check in. Is there a near-term deadline I can give people and if so what do you need by that time?

Documentation for the walkability measure is in the jphp article (attached).

documentation for the park measures is here http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3696994/



On Tue, Dec 9, 2014 at 3:10 PM, Melina Iacovou <mi2280@barnard.edu> wrote:
Hi Dr. Neckerman,

I just wanted to touch base regarding the GIS datasets on walkability, park area/quality and safety. 

Any other insight you can provide to me so I understand what the group has done would be immensely helpful-- is there a handbook or write-up associated with these datasets that goes beyond the brief descriptions on the website? 

Thanks so much,
Melina 

On Wed, Dec 3, 2014 at 1:23 PM, Kathryn M. Neckerman <k.neckerman@gmail.com> wrote:
This is kind of a busy time for our team, so if you don't hear from me in a week, just send a quick reminder and I'll make sure this is moving along,

K

On Wed, Dec 3, 2014 at 1:13 PM, Melina Iacovou <mi2280@barnard.edu> wrote:
Dr Neckerman,

Thank you very much. I look forward to it!

Best,
Melina

On Tue, Dec 2, 2014 at 1:17 PM, Kathryn M. Neckerman <k.neckerman@gmail.com> wrote:
Melina,

We can provide some measures for your project but our GIS analysts need to look at what we already have created. I'll be back in touch about this.

All best,

kathy

On Mon, Dec 1, 2014 at 12:43 PM, Kathryn M. Neckerman <k.neckerman@gmail.com> wrote:
Hi Melina,

I've forwarded your request to others in the group. We meet tomorrow morning and I expect we'll talk about it then.

Kathy

On Mon, Dec 1, 2014 at 12:38 PM, Melina Iacovou <mi2280@barnard.edu> wrote:
Hi Dr. Neckerman,

I just wanted to touch base regarding the data request. Please let me know what you and the rest of the group think.

Thanks so much,
Melina 

On Wed, Nov 26, 2014 at 1:25 PM, Melina Iacovou <mi2280@barnard.edu> wrote:
Hi Dr. Neckerman,

That would be wonderful, and zip codes would be great to work with. While the families are in mainly 2 neighborhoods, I plan to explore all NYC Early Head Start neighborhoods to see what populations the centers serve. I am hoping to look at the median household income of the zip codes in which the centers are located (there are 42 across the 5 boroughs), along with community aspects such as walkability, safety and park area & quality. 

Thank you and Happy Thanksgiving,
Melina 

On Mon, Nov 24, 2014 at 6:34 AM, Kathryn M. Neckerman <k.neckerman@gmail.com> wrote:
Hi Melina,

Let me check with the group - I know we're sharing some of this info but I'm not sure for what geographies. Without a budget for custom work, we would probably share for administrative/census geographies such as community districts or zip code tabulation areas. Are your families clustered in a single neighborhood or are they spread across the city?

KN

On Sun, Nov 23, 2014 at 9:28 PM, Melina Iacovou <mi2280@barnard.edu> wrote:
Hi Dr. Neckerman,

My name is Melina Iacovou, and I am a senior at Barnard College of Columbia University. For my thesis, I am studying a population of families enrolled in an Early Head Start program in the city. My work is part of a larger research effort- a collaboration between Mailman's PopFam department (PI Dr. Helena Duch) and the Teachers College Movement Science department (PI Dr. Carol Garber). 

I am hoping to look at some aspects of the home (affordances given to children, space available to move freely) and the built environment of the neighborhood of the population to relate those variables to the physical activity levels of the parents. 

I know that the Built Environment and Health Research Group has done neighborhood walkability, safety and park area & quality data collection for the city. Is this something that can be shared for research purposes given that I would be building off of it? 
If so, by what geography are such measures broken down? 

Please do let me know. 

Thanks so much,
Melina

-->