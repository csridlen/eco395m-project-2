import pandas as pd
import json
import math
import numpy as np
from shapely.geometry import shape, Point
from readtable import getairbnbdata
from sklearn import neighbors

lauri_data = getairbnbdata()
nycmap2020 = json.load(open("../data/2020_Neighborhood_Tabulation_Areas.geojson"))
station_map = json.load(open("../data/Subway_Stations.geojson"))
parks_map = json.load(open("../data/Parks_Zones.geojson"))


# this remaps all the airbnb locations to the polygons formed from the updated neighborhoods 
lauri_data["new_neighbourhood"] = ""

for i, row in lauri_data.iterrows():
    for feature in nycmap2020["features"]:
        polygon = shape(feature["geometry"])
        if polygon.contains(Point(row["avg_lon"], row["avg_lat"])):
            lauri_data["new_neighbourhood"][i] = feature["properties"]["ntaname"]


# retrieve latitude and longitude of each subway station
station_lat = []
station_lon = []
for n in station_map["features"]:
    station_lat.append(n["geometry"]["coordinates"][1])
    station_lon.append(n["geometry"]["coordinates"][0])

stations = pd.DataFrame({"latitude": station_lat, "longitude": station_lon})


# convert latitude and longitude to radians and zip them into coordinates
stations["coordinate"] = list(
    zip(stations["latitude"] * math.pi / 180, stations["longitude"] * math.pi / 180)
)
lauri_data["coordinate"] = list(
    zip(lauri_data["avg_lat"] * math.pi / 180, lauri_data["avg_lon"] * math.pi / 180)
)

# this calculates the distance between the airbnb and each station and finds the nearest station using the haversine distance formula
station_location = np.asarray(list(stations["coordinate"]))
tree = neighbors.BallTree(station_location, metric="haversine")
airbnb_location = np.asarray(list(lauri_data["coordinate"]))
station_dist, _ = tree.query(X=airbnb_location, k=1)
lauri_data["station_dist"] = station_dist
lauri_data["station_dist"] = lauri_data["station_dist"].apply(lambda x: x * 3960)

# we'll repeat the process but using the manhattan distance formula
tree2 = neighbors.BallTree(station_location, metric="manhattan")
station_dist2, _ = tree2.query(X=airbnb_location, k=1)
lauri_data["station_dist2"] = station_dist2
lauri_data["station_dist2"] = lauri_data["station_dist2"].apply(lambda x: x * 3960)

# we'll retrieve the distances now for park zones
park_lat = []
park_lon = []

# the geojson for parks actually form zones rather than points so we have to get each latitude longitude from the polygons within each park
for p in parks_map["features"]:
    for c in p["geometry"]["coordinates"][0][0]:
        park_lat.append(c[1])
        park_lon.append(c[0])

parks = pd.DataFrame({"latitude": park_lat, "longitude": park_lon})


# convert latitude and longitude to radians and zip them into coordinates
parks["coordinate"] = list(
    zip(parks["latitude"] * math.pi / 180, parks["longitude"] * math.pi / 180)
)

#calculate the distances
parks_location = np.asarray(list(parks["coordinate"]))
tree3 = neighbors.BallTree(parks_location, metric="haversine")
park_dist, _ = tree3.query(X=airbnb_location, k=1)
lauri_data["park_dist"] = park_dist
lauri_data["park_dist"] = lauri_data["park_dist"].apply(lambda x: x * 3960)

# in new york of all places (but for walksable streets in general), manhattan distance would be more applicable
tree4 = neighbors.BallTree(parks_location, metric="manhattan")
park_dist2, _ = tree4.query(X=airbnb_location, k=1)
lauri_data["park_dist2"] = park_dist2
lauri_data["park_dist2"] = lauri_data["park_dist2"].apply(lambda x: x * 3960)

#writes to csv
lauri_data.to_csv("cleaned_data_updated.csv")