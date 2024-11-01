import os
import folium
from populate.populate import populate
from populate.query import query_last, plot_temp_data
from core.config import LON_UNICAMP, LAT_UNICAMP

if os.getenv("POPULATE", "false").lower() == "true":
    populate()

plot_temp_data()

df = query_last()

latitude = df["latitude"][0]
longitude = df["longitude"][0]
temp_value = df["temperature"][0]
temperature = f"Temperature: {temp_value}ºC"

map = folium.Map(location=[LAT_UNICAMP, LON_UNICAMP], zoom_start=17)

folium.Marker(
    [latitude, longitude],
    popup=temperature,
    tooltip=temperature,
).add_to(map)

map.save("temporary/mapa_interativo.html")