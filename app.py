from flask import Flask, request, render_template
import folium
import geopandas as gpd
from folium import Element
from folium import plugins

import argparse

app = Flask(__name__)
app.secret_key = 'somethingsecret'

@app.route('/', methods=['GET', 'POST'])
def home():
    towns = gpd.GeoDataFrame.from_file('citiestownpopulation2013.geojson')
    burma_map = folium.Map(location=[25, 100],
                               tiles='Mapbox Bright', zoom_start=5)
    folium.GeoJson(towns.to_crs(epsg='4326').to_json(),
                   name='geojson').add_to(burma_map)
    burma_map.save('templates/landing.html')
    return render_template('landing.html')

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Test')
    parser.add_argument('--debug', dest='debug', action='store_true')
    parser.set_defaults(debug=False)
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=5000, debug=args.debug)
