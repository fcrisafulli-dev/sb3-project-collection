import json
import csv
import sys

user=sys.argv[1]

with open("../files/%s_projects_full.json" % (user)) as tmpjson:
	complete_json=json.load(tmpjson)

with open("../files/%s_projects.csv" %(user),"wb+") as tmpcsv:
	cw = csv.writer(tmpcsv)
	cw.writerow([
		"title",
		"instructions",
		"description",
		"author_id",
		"id",
		"stats_views",
		"stats_loves",
		"stats_favorites",
		"stats_comments",
		"author_scratchteam",
		"comments_allowed",
		"is_published",
		"public",
		"visibility",
		"author_history_joined",
		"history_created",
		"history_shared",
		"history_modified",
		"stats_remixes",
		"remix_root",
		"remix_parent"])
	for project in complete_json:
		cw.writerow([
			project["title"].encode("utf-8").strip(),
			project["instructions"].encode("utf-8").strip(),
			project["description"].encode("utf-8").strip(),
			project["author"]["id"],
			project["id"],
			project["stats"]["views"],
			project["stats"]["loves"],
			project["stats"]["favorites"],
			project["stats"]["comments"],
			project["author"]["scratchteam"],
			project["comments_allowed"],
			project["is_published"],
			project["public"],
			project["visibility"],
			project["author"]["history"]["joined"],
			project["history"]["created"],
			project["history"]["shared"],
			project["history"]["modified"],
			project["stats"]["remixes"],
			project["remix"]["root"],
			project["remix"]["parent"]
			])
