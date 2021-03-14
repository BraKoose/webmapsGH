import folium
map = folium.Map(location=[7, 1.0232],
                 zoom_start=7, titles="Stamen Terrain")
map.save("GhanaMap.html")
