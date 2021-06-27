#!/usr/bin/python
import json

def value(json):
  return json["DELETE_ME"]["value"]

def strref(json):
  if "STRREF" in json:
    return "TLK: " + str(json["STRREF"]["value"] - 16777217)
  else:
    return "TLK: null"

f = open('src/itp/placeablepal.itp.json')

data = json.load(f)

for i in data["MAIN"]["value"]:
  print(value(i) + " [" + strref(i) + "]")
  if "LIST" in i:
    for j in i["LIST"]["value"]:
      print("- " + value(j) + " [" + strref(j) + "]")
      if "LIST" in j:
        for k in j["LIST"]["value"]:
          print("-- " + value(j) + " [" + strref(j) + "]")
f.close()
