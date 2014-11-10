import pandas as pd

inCSV = '/Users/danielmsheehan/Dropbox/GIS/Projects/Sullivan/data/tables/zip_playgrounds_int_dis.csv'
ouCSV = '/Users/danielmsheehan/Dropbox/GIS/Projects/Sullivan/data/tables/playgrounds_in_zip_nyc.csv'
ghCSV = '/Users/danielmsheehan/GitHub/beh/sullivan/data/playgrounds_in_zip_nyc.csv'

df = pd.read_csv(inCSV)

df['playgrounds'] = df['COUNT_ZIPCODE']

df = df[['ZIPCODE','playgrounds']]

df.to_csv(ouCSV, index=False)
df.to_csv(ghCSV, index=False)


