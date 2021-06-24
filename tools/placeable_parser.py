#!/usr/bin/python
import json

f = open('src/itp/placeablepal.itp.json')

data = json.load(f)

for i in data["MAIN"]["value"]:
  print(i["DELETE_ME"]["value"])

f.close()
