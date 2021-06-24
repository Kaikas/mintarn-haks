#!/usr/bin/python
import json

f = open('src/itp/placeablepal.itp.json')

data = json.load(f)

for i in data["MAIN"]["value"]:
  print(i["DELETE_ME"]["value"])
  if "LIST" in i:
    for j in i["LIST"]["value"]:
      print(" - " + j["DELETE_ME"]["value"])
      if "LIST" in j:
        for k in j["LIST"]["value"]:
          print(" -- " + k["DELETE_ME"]["value"])
f.close()
