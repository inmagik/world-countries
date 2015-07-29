# world-countries
This repository contains geographic info of countries of the world as static files.

Data comes from the "WORLD BORDERS" dataset provided by Bjorn Sandvik, http://www.thematicmapping.org

The dataset is available under a Creative Commons Attribution-Share Alike License. If you use this dataset, please provide a link to this website.

The original dataset consists of a shapefile with all countries of the world with the following data fields:
*FIPS	String(2)	FIPS 10-4 Country Code
*ISO2	String(2)	ISO 3166-1 Alpha-2 Country Code
*ISO3	String(3)	ISO 3166-1 Alpha-3 Country Code
*UN	Short Integer(3)	ISO 3166-1 Numeric-3 Country Code
*NAME	String(50)	Name of country/area
*AREA	Long Integer(7)	Land area, FAO Statistics (2002)
*POP2005	Double(10,0)	Population, World Population Prospects (2005)
*REGION	Short Integer(3)	Macro geographical (continental region), UN Statistics
*SUBREGION	Short Integer(3)	Geographical sub-region, UN Statistics
*LON	FLOAT (7,3)	Longitude
*LAT	FLOAT (6,3)	Latitude

All the geometry have been preprocessed to calculate some useful information:
- centroid of the geometry
- representative point of the geometry
- bounding box (bbox) containing the geometry

##API
The information for each country has been indexed by the ISO 3166-1 Alpha-3 Country Code and is exposed in various formats:

* json: country info in JSON format (does not includes geometry but includes bbox, centroid and representative_point)
  example: `http://inmagik.github.io/world-countries/countries/ITA.json`
* geojson: GeoJSON file with country info (as a FeatureCollection with one item)
  example: `http://inmagik.github.io/world-countries/countries/ITA.geojson`
* javascript: a file containing the WorldBorders object, populated with the requested country data. Same content as json, but in js context and loadable via `<script>` tag
  example: `http://inmagik.github.io/world-countries/countries/ITA.js`

# Building the files
The files can be built with the python script in the "maker" folder.


## Sources
**world borders**: http://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip
