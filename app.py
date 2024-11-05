import folium
from flask import Flask, send_from_directory
from populate.query import query_last
from core.config import LON_UNICAMP, LAT_UNICAMP

app = Flask(__name__)

@app.route('/')
def generate_and_serve_map():
    df = query_last()
    map = folium.Map(location=[LAT_UNICAMP, LON_UNICAMP], zoom_start=16)
    for _, row in df.iterrows():
        latitude = row.latitude
        longitude = row.longitude
        temp_value = row.temperature
        temperature = f"Temperature: {temp_value}ºC"

        folium.Marker(
            [latitude, longitude],
            popup=temperature,
            tooltip=temperature,
            icon=folium.Icon(color="red"),
        ).add_to(map)
    map.save("temporary/mapa_interativo.html")
    return send_from_directory('temporary', 'mapa_interativo.html')

if __name__ == '__main__':
    app.run(debug=True)
