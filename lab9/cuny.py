import folium
import pandas as pd


cuny = pd.read_csv('cunyLocations.csv')
print (cuny["Campus"])

mapCUNY = folium.Map(location=[40.768731, -73.964915])

for index,row in cuny.iterrows():
    print ("index, row",index,row)
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Campus"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapCUNY)
#For each row in the file, we find the latitude, longitude, and name of the campus, and use those to create a new marker which we add to our map. We repeat for each row, until we have made markers for all 23 campuses in the file.


mapCUNY.save(outfile='cunyLocations_new.html')
