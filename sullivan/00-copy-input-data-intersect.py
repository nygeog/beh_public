import arcpy

list_of_zips = ['10027','10029','10030','10031','10032','10033','10034','10037','10039','10040','10451','10452','10453','10463','10468']

# for i in list_of_zips:
# 	print '"ZIPCODE" = ' + "'" + i + "' OR "


inZIP = 'W:/GIS/Data/Municipal/USA/New_York/New_York_City/ZIP_CODE_040114/ZIP_CODE_040114.shp'
ouZIP = "W:/GIS/Projects/Sullivan/data/input/input.gdb/zip"

exp = """"ZIPCODE" = '10027' OR "ZIPCODE" = '10029' OR "ZIPCODE" = '10030' OR "ZIPCODE" = '10031' OR "ZIPCODE" = '10032' OR "ZIPCODE" = '10033' OR "ZIPCODE" = '10034' OR "ZIPCODE" = '10037' OR "ZIPCODE" = '10039' OR "ZIPCODE" = '10040' OR "ZIPCODE" = '10451' OR "ZIPCODE" = '10452' OR "ZIPCODE" = '10453' OR "ZIPCODE" = '10463' OR "ZIPCODE" = '10468'"""

arcpy.Select_analysis(inZIP,ouZIP,exp)

arcpy.Dissolve_management("W:/GIS/Projects/Sullivan/data/input/input.gdb/zip","W:/GIS/Projects/Sullivan/data/input/input.gdb/zip_dis","ZIPCODE","#","MULTI_PART","DISSOLVE_LINES")

arcpy.Intersect_analysis("W:/GIS/Projects/Sullivan/data/input/input.gdb/zip_dis #;W:/GIS/Data/Municipal/USA/New_York/New_York_City/Playgrounds/dpr_playgrounds.shp #","W:/GIS/Projects/Sullivan/data/processing/processing.gdb/zip_playgrounds_int","ALL","#","INPUT")

arcpy.Dissolve_management("W:/GIS/Projects/Sullivan/data/processing/processing.gdb/zip_playgrounds_int","W:/GIS/Projects/Sullivan/data/processing/processing.gdb/zip_playgrounds_int_dis","ZIPCODE","ZIPCODE COUNT","MULTI_PART","DISSOLVE_LINES")

arcpy.ExportXYv_stats("W:/GIS/Projects/Sullivan/data/processing/processing.gdb/zip_playgrounds_int_dis","ZIPCODE;COUNT_ZIPCODE","COMMA","W:/GIS/Projects/Sullivan/data/tables/zip_playgrounds_int_dis.csv","ADD_FIELD_NAMES")
