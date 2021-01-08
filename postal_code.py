#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import io
import csv
filename = 'codigos_postales_municipios.csv'

jsonfile = 'codigos_postales_municipios.json'

# codigo_postal,municipio_id,municipio_nombre
# 00040,40223,Vegas de Matute
# 00042,42173,Soria
# 00043,43110,"Pobla de Massaluca, La"
# 00045,45165,Talavera de la Reina
# 00115,08113,Manresa
# 00140,18193,"Zubia, La"

dictionary = {}

with open(filename, 'r') as content: 
    count = 0
    lines = csv.reader(content, doublequote=False)
    for line in lines:
        codigo_postal, id_region, description = line
        found = dictionary.get(codigo_postal, 'None')
        if found == "None":
            dictionary[codigo_postal] = description.strip()
        else:
            dictionary[codigo_postal] = found + ' / ' + description.strip()
        count += 1
json.dump(dictionary, open(jsonfile, "w" ), sort_keys=True, indent=4, ensure_ascii=True)