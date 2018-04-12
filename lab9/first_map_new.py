#Import the folium package for making maps
import folium

#-74, latitude: 41
#Create a map, centered (0,0), and zoomed out a bit:
mapWorld = folium.Map(location=[40.7685406,-73.96681],zoom_start=16)
folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapWorld)
#Save the map:
mapWorld.save(outfile='hunter_college_16_with_marker.html')
