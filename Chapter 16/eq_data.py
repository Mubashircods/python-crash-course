from pathlib import Path
import json
import plotly.express as px




path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf8')
data = json.loads(contents)

all_eq_dics = data['features']
mgds, lons, lats, eq_title = [], [], [], []
for eq_data in all_eq_dics:
    mgs = eq_data['properties']['mag']
    lon = eq_data['geometry']['coordinates'][0]
    lat = eq_data['geometry']['coordinates'][1]
    titles = eq_data['properties']['title']
    mgds.append(mgs)
    lons.append(lon)
    lats.append(lat)
    eq_title.append(titles)

title = 'Globle Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mgds,
                     title=title, color=mgds,
                     color_continuous_scale='viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_title
                    )
fig.show()
