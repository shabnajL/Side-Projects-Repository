#importing folium package
import folium

# the Map method of FOLIUM return MAP

# setting the coordinates of daegu to busan
start_x, start_y = 35.8714, 128.6014
end_x, end_y = 35.1796, 129.0756

# initial view of the map starting Zoom level = 10
map = folium.Map(location=[start_x, start_y], zoom_start=10)

# setting place name to show in popup
start_place = 'Daegu'
end_place = 'Busan'

# marking the targeted places into the map
folium.Marker([start_x, start_y], popup=start_place).add_to(map)
folium.Marker([end_x, end_y], popup=end_place).add_to(map)

# creating a line from daegu to busan and setting line optacity
folium.PolyLine(locations=[(start_x, start_y), (end_x, end_y)], line_opacity=0.95).add_to(map)
# saving in html to see the map
map.save("random_Map.html")
