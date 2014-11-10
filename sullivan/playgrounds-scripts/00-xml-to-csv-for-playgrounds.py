import xml.etree.ElementTree as ET
import csv
import pandas as pd

wd = ''

in_file = wd+ "DPR_Playgrounds_001.xml"


tree = ET.parse(in_file)
root = tree.getroot()

pidList = []
pldList = []
schList = []
staList = []
namList = []
locList = []
accList = []
levList = []
adaList = []
latList = []
lonList = []

j=0
for i in root:
	pid = root[j][0].text
	pld = root[j][1].text
	sch = root[j][2].text
	sta = root[j][3].text
	nam = root[j][4].text.encode('utf8')
	loc = root[j][5].text
	acc = root[j][6].text
	lev = root[j][7].text
	ada = root[j][8].text
	lat = root[j][9].text
	lon = root[j][10].text
	
	pidList.append(pid)
	pldList.append(pld)
	schList.append(sch)
	staList.append(sta)
	namList.append(nam)
	locList.append(loc)
	accList.append(acc)
	levList.append(lev)
	adaList.append(ada)
	lonList.append(lon)
	latList.append(lat)

	j = j+1

rows = zip(pidList,pldList,schList,staList,namList,locList,accList,levList,adaList,latList,lonList)

inCSV = wd+'dpr_playgrounds_working.csv'
ouCSV = wd+'dpr_playgrounds.csv'

with open(inCSV, 'wb') as f:
    writer = csv.writer(f)
    for row in rows:
    	#print row
    	writer.writerow(row)


df = pd.read_csv(inCSV, header=None)

df.columns = ['prop_id','playground_id','school_id','status','name','location','accessible','level','adaptive_swing','lat','lon']

df.to_csv(ouCSV, index=False)
