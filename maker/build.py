# -*- coding: utf-8 -*-
import os
import json
import shapefile
from shapely.geometry import shape, mapping

if __name__ == '__main__':

    countries_list = []

    sf = shapefile.Reader("../datasource/TM_WORLD_BORDERS-0.3.shp")
    shape_recs = sf.shapeRecords()
    fields = [x[0] for x in sf.fields[1:]]
    char_fields = [x[0] for x in sf.fields[1:] if x[1].lower()=='c'] 

    base_api = os.path.abspath("../")
    if not os.path.isdir(base_api):
        os.mkdir(base_api)

    extents_path = os.path.join(base_api, "countries")
    if not os.path.isdir(extents_path):
        os.mkdir(extents_path)

    for s in shape_recs:
        d = {}
        for i,f in enumerate(fields):
            d[f] = s.record[i]
            if f in char_fields:
                d[f] = d[f].decode('cp1252')

            
        name = s.record[4]
        clean_name = name.lower().replace(" ", "-")
        iso3 = s.record[2]

        countries_list.append(iso3)
        shapely_shape = shape(s.shape)
        d['centroid'] = list(shapely_shape.centroid.coords)[0]
        d['representative_point'] = list(shapely_shape.representative_point().coords)[0]
        d['bbox'] = list(s.shape.bbox)
        
        geometry_dict =mapping(shapely_shape)
        geojson_feature = {
            "type" : "Feature",
            "geometry" : geometry_dict,
            "properties" : d
        }
        geojson_dict = {
            "type": "FeatureCollection",
            "features": [geojson_feature]
        }

        
        dict_dump = json.dumps(d)
        filename = os.path.join(extents_path, "%s.json" % iso3)
        with open(filename, "wb") as fs:
            fs.write(dict_dump)
            
        geo_dict_dump =  json.dumps(geojson_dict)
        geofilename = os.path.join(extents_path, "%s.geojson" % iso3)
        with open(geofilename, "wb") as fs:
            fs.write(geo_dict_dump)

        js_template = """
(function(){
     window.WorldBorders = window.WorldBorders || {};
     window.WorldBorders.%s = %s;
})();

        """
        js_code = js_template % (iso3, geo_dict_dump)
        jsfilename = os.path.join(extents_path, "%s.js" % iso3)
        with open(jsfilename, "wb") as fs:
            fs.write(js_code)
            
         
    filename = os.path.join(base_api, "countrycodes.json")
    countries_list.sort()
    
    with open(filename, "wb") as fs:
        text = json.dumps(countries_list)
        fs.write(text)
        