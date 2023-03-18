import folium
import json
import pandas as pd

tg_center = [47.5924, 9.0687]

bounding_box = [[47.375917,8.667973],[47.695418,9.502768]]

m = folium.Map(location=tg_center, zoom_start= 0, tiles='cartodbpositron')

m.fit_bounds(bounding_box)

geojson_data_thurgau = 'geo_data\switzerland-kanton.geojson'
geojson_data_gemeinden = 'geo_data\switzerland-gemeinde.geojson'
with open(geojson_data_gemeinden) as f:
    geojson_data_gemeinden = json.load(f)

with open(geojson_data_thurgau) as y:
    geojson_data_thurgau = json.load(y)



style_tg = lambda x: {'color': 'yellow', 'weight': 4, 'fillColor': 'none'}
style_gm = lambda x: {'color': 'green', 'weight': 2, 'fillColor': 'none'}


energy_data = 'energyData/co2EmissionenGebaeudeGemeinde.json'
energy_data = pd.read_json(energy_data, )
energy_data = energy_data[['bfs_nr_gemeinde', 'total']]

# drop nas
energy_data = energy_data.dropna()
print(energy_data)

import geopandas

geometries = geopandas.read_file('geo_data/towns_fixed.geojson')
#print(geometries.head())

print(geometries.dtypes)

joined = geometries.merge(energy_data, how="inner", on="bfs_nr_gemeinde")

map = joined.explore('total')
map.save('tg_mapCO2Emission.html')




map
print(energy_data)
print('Build successful')