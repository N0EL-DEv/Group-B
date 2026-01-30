import pandas as pd
import math

#Load dataset
dataset = pd.read_csv("C:\\Users\\THIS PC\\OneDrive\\Documents\\GroupB_road_csv.csv")

#Dictionary to store graph data
graph = {}

#Reference point
REF_LAT = 4.161608
REF_LON = 9.297882

#Distance function
def distance(lat, lon):
    return math.sqrt((lat - REF_LAT)**2 + (lon - REF_LON)**2)

#Build dictionary
for row in dataset.itertuples(index=False):
    graph[row.Point, row.Description] = {
        "Latitude": row.Latitude,
        "Longitude": row.Longitude,
        "Description": row.Description,
        "Distance": distance(row.Latitude, row.Longitude)
    }

#Show all points
for key, value in graph.items():
    print(f"{key}: {value}")



from haversine import haversine
 
final_graph = set()
 
# Loop through consecutive points in the dataset

for i in range(len(dataset) - 1):

    # Extract coordinates

    lat1, long1 = dataset.iloc[i]["Latitude"], dataset.iloc[i]["Longitude"]

    lat2, long2 = dataset.iloc[i+1]["Latitude"], dataset.iloc[i+1]["Longitude"]
 
    # Compute distance

    dist = haversine((lat1, long1), (lat2, long2))
 
    # Handle cost safely (default to None if missing)

    cost1 = dataset.iloc[i]["Cost"] if "Cost" in dataset.columns else None

    cost2 = dataset.iloc[i+1]["Cost"] if "Cost" in dataset.columns else None
 
    # Build node tuples (longitude, latitude, distance, cost)

    node1 = (long1, lat1, round(dist, 3), cost1)

    node2 = (long2, lat2, round(dist, 3), cost2)
 
    # Add edge to final graph

    final_graph.add((node1, node2))
 
    # Print results in the requested format

    print(f"Pair {i}: {dataset.iloc[i]['Point']} → {dataset.iloc[i+1]['Point']}")

    print(f"  From: {dataset.iloc[i]['Description']}")

    print(f"  To  : {dataset.iloc[i+1]['Description']}")

    print(f"  Distance: {round(dist, 3)} km\n")

 