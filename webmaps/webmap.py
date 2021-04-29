import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'pink'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(location=[37.0902, 95.7129],
                 zoom_start=6, titles="Koose")

fg = folium.FeatureGroup(name="Kumasi")


for k, l, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[
                 k, l], popup=str(el) + " This is my Fav places in Kuamsi", icon=folium.Icon(color=color_producer(el))))


map.add_child(fg)

map.save("GhanaMap.html")
