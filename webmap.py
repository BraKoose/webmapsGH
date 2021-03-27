import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[37.0902, 95.7129],
                 zoom_start=10, titles="Stamen Terrain")

fg = folium.FeatureGroup(name="Kumasi")


for k, l in zip(lat, lon):
    map.add_child(folium.Marker(location=[k, l],
                                popup="This is my Fav places in Kuamsi", icon=folium.Icon(color='blue')))


map.add_child(fg)

map.save("GhanaMap.html")
