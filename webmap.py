import folium
map = folium.Map(location=[6.6998, -1.6246],
                 zoom_start=20, titles="Stamen Terrain")

fg = folium.FeatureGroup(name="Kumasi")

for coordinates in [[6.6719, -1.6068], [6.6939, -1.6363]]:
    map.add_child(folium.Marker(location=coordinates,
                                popup="This is my Fav places in Kuamsi", icon=folium.Icon(color='blue')))


map.add_child(fg)

map.save("GhanaMap.html")
