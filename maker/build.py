import shapefile
import os
import json


if __name__ == '__main__':

    sf = shapefile.Reader("../datasource/TM_WORLD_BORDERS-0.3.shp")
    shape_recs = sf.shapeRecords()
    print sf.fields

    fields = [x[0] for x in sf.fields[1:]]
    char_fields = [x[0] for x in sf.fields[1:] if x[1]=='c'] 

    base_api = os.path.join("../", "api")
    if not os.path.isdir(base_api):
        os.mkdir(base_api)

    extents_path = os.path.join(base_api, "extents")
    if not os.path.isdir(extents_path):
        os.mkdir(extents_path)

    for s in shape_recs:
        d = {}
        for i,f in enumerate(fields):
            d[f] = s.record[i]
            if f in char_fields:
                d[f] = d[f].decode('ascii', 'ignore')

            
        name = s.record[4]
        clean_name = name.lower().replace(" ", "-")
        iso3 = s.record[2]

        bbox = list(s.shape.bbox)
        d['bbox'] = list(bbox)
        filename = os.path.join(extents_path, "%s.json" % iso3)
        print filename
        
        with open(filename, "wb") as fs:
            try:
                text = json.dumps(bbox)
                #text.encode('latin-1', "ignore")
                fs.write(text)
            except Exception, e:
                print e, d
                pass
