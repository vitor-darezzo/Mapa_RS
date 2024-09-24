import branca.utilities
import folium 
import branca.colormap as cm
import numpy as np
from folium.plugins import HeatMap

# Inicializa o mapa centrado no Rio Grande do Sul
mapa_rs = folium.Map(location=[-29.68, -53.80], zoom_start=6, tiles='cartodb positron')

# URL do GeoJSON para os municípios do RS
geojson_arquivo = "https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-43-mun.json"

# Estilo para o GeoJSON
estilo_municipios = {
    "color": "black",
    "weight": 1,
    "fillOpacity": 0
}

# Adiciona os municípios do RS ao mapa
folium.GeoJson(
    geojson_arquivo,
    name="Municípios",
    style_function=lambda x: estilo_municipios
).add_to(mapa_rs)


# Dados fornecidos (latitude, longitude, intensidade)
dados = np.array([
    [-291.714, -515.204, 9],
    [-293.541, -516.687, 2],
    [-294.863, -513.544, 1],
    [-299.510, -510.939, 1],
    [-293.560, -508.126, 2],
    [-299.173, -511.839, 19],
    [-296.967, -513.285, 1],
    [-292.675, -519.864, 2],
    [-291.629, -511.793, 10],
    [-295.142, -519.932, 9],
    [-300.844, -516.181, 6],
    [-292.354, -518.709, 1],
    [-298.511, -511.799, 1],
    [-292.255, -513.419, 1],
    [-293.836, -521.006, 2],
    [-299.032, -517.652, 1],
    [-293.734, -508.762, 7],
    [-296.045, -537.707, 1],
    [-294.593, -519.644, 1],
    [-296.826, -514.671, 1],
    [-301.915, -523.806, 1],
    [-295.476, -517.332, 2],
    [-293.442, -533.216, 2],
    [-300.346, -512.177, 5],
    [-290.039, -521.578, 1],
    [-292.845, -518.656, 10],
    [-294.388, -515.071, 2],
    [-297.179, -524.342, 2],
    [-296.842, -538.069, 6],
    [-299.716, -517.255, 1],
    [-296.193, -534.424, 1],
    [-297.547, -511.493, 8],
    [-293.712, -513.687, 2],
    [-293.425, -529.774, 1],
    [-287.127, -519.351, 2],
    [-296.468, -535.785, 1],
    [-295.355, -525.305, 3],
    [-294.191, -530.321, 1],
    [-296.507, -507.753, 2],
    [-295.141, -507.734, 3],
    [-295.968, -526.844, 1],
    [-296.065, -521.934, 4],
    [-289.322, -515.496, 6],
    [-301.135, -513.255, 1],
    [-292.890, -520.535, 1],
    [-293.747, -511.147, 1],
    [-297.942, -518.642, 1],
])

# Ajusta as coordenadas para a escala correta
dados[:, :2] /= 10

# Define o colormap
colormap = cm.LinearColormap(
    ['blue', 'lime', 'yellow', 'red'],
    vmin=dados[:, 2].min(),
    vmax=dados[:, 2].max(),
    caption="Intensidade"
)

# Adiciona a escala de cores ao mapa
colormap.add_to(mapa_rs)

# Cria o HeatMap e o adiciona ao mapa
HeatMap(
    data=dados,
    min_opacity=0.4,
    max_zoom=16,
    radius=25,
    blur=15,
    gradient={0.2: 'blue', 0.4: 'lime', 0.6: 'yellow', 1.0: 'red'}
).add_to(mapa_rs)


# Adiciona um controle de camadas ao mapa
folium.LayerControl(position="topleft").add_to(mapa_rs)

# Exibe o mapa
mapa_rs
