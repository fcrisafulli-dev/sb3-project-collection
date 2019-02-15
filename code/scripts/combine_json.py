import json
import sys

user=sys.argv[1]

json_data=[]
for x in range (25):
	with open("../files/%s_projects_part_%s.json" % (user,x)) as tmpjson:
		for i in json.load(tmpjson):
			json_data.append(i)

with open("../files/%s_projects_full.json" % (user),"w") as tmpjson:
	json.dump(json_data,tmpjson)
