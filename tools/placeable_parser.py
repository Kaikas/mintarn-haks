#!/usr/bin/python
import json

def value(json):
  return json["DELETE_ME"]["value"]

def strref(json):
  if "STRREF" in json:
    return json["STRREF"]["value"] - 16777217
  else:
    return 0

def find_itp_string(json, p_id):
  for i in json["entries"]:
    if i["id"] == p_id:
      return i["text"]
  return "null"

placeable_file = open('src/itp/placeablepal.itp.json')
tlk_file = open('src/tlk/mintarn.tlk.json')

p_data = json.load(placeable_file)
t_data = json.load(tlk_file)

for i in p_data["MAIN"]["value"]:
  print(value(i) + " [TLK: " + str(strref(i)) + "]: " + find_itp_string(t_data, strref(i)))
  if "LIST" in i:
    for j in i["LIST"]["value"]:
      print("- " + value(j) + " [" + str(strref(j)) + "]")
      if "LIST" in j:
        for k in j["LIST"]["value"]:
          print("-- " + value(j) + " [" + str(strref(j)) + "]")
placeable_file.close()
tlk_file.close()

#16777441

