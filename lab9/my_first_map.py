#import the folium package for making maps
import folium
#https://www.google.com/maps/place/Hunter+College/@40.7685406,-73.9668138,17z/data=!3m1!4b1!4m5!3m4!1s0x89c258eb899f0889:0xb5e90aa7d877ee1f!8m2!3d40.7685406!4d-73.9646251?hl=en

#Create a map, centered (0,0), and zoomed out a bit:
mapWorld = folium.Map(location=[0,0],zoom_start=3)

#Save the map:
mapWorld.save(outfile='tempMap.html')
