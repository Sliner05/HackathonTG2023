import folium

tg_center = [47.5924, 9.0687]

bounding_box = [[47.375917,8.667973],[47.695418,9.502768]]

m = folium.Map(location=tg_center, zoom_start= 0, tiles='cartodbpositron')

m.fit_bounds(bounding_box)

geojson_data_thurgau = 'geo_data\switzerland-kanton.geojson'
geojson_data_gemeinden = 'geo_data\switzerland-gemeinde.geojson'

style_tg = lambda x: {'color': 'yellow', 'weight': 4, 'fillColor': 'none'}
style_gm = lambda x: {'color': 'green', 'weight': 2, 'fillColor': 'none'}

folium.GeoJson(geojson_data_gemeinden, style_function=style_gm).add_to(m)
folium.GeoJson(geojson_data_thurgau, style_function=style_tg).add_to(m)



m.save('tg_map.html')
m
print('Build successful')