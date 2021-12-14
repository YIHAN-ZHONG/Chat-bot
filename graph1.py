

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import plotly.express as px 
import json
import chart_studio
import chart_studio.plotly as py


#py.plot(fig, filename = 'gdp_per_cap', auto_open=True)

def world_happiness_map():

#read the own data set 
    df=pd.read_csv('world-happiness-report-2021.csv')
    df['Rank']=df.index+1
    df=df[['Country name','Ladder score','Rank']]

# get the coordinates of the countries
    world_path = 'custom.geo.json'
    with open(world_path) as f:
        geo_world = json.load(f)

# Instanciating necessary lists
    found = []
    missing = []
    countries_geo = []

    tmp = df.set_index('Country name')

# corret the name of country in gep_json file 
    country_conversion_dict = {'Dominican Rep.':'Dominican Republic',
'N. Cyprus':'North Cyprus',
'Korea':'South Korea',
'Lao PDR':'Laos',
'Eq. Guinea':'Guinea',
'Bosnia and Herz.':'Bosnia and Herzegovina',
'Taiwan':'Taiwan Province of China',
'Dem. Rep. Congo': 'Congo (Brazzaville)',
"Côte d'Ivoire":'Ivory Coast',
'Macedonia':'North Macedonia',
'Palestine':'Palestinian Territories',
'Czech Rep.':'Czech Republic'}

    for country in geo_world['features']:
        country_name = country['properties']['name'] 

        country_name=country_conversion_dict[country_name] if country_name in country_conversion_dict.keys() else country_name
        go_on=country_name in tmp.index
     
        if go_on:
            found.append(country_name)
            geometry = country['geometry']
            countries_geo.append({
            'type': 'Feature',
            'geometry': geometry,
            'id':country_name
        })
        else:
            missing.append(country_name)

#sotcker les data geo 
    geo_world_ok = {'type': 'FeatureCollection', 'features': countries_geo}

    max_score=df['Ladder score'].max()
    max_val=int(max_score)+1

#prepare the range of the colorbar

    values = [i for i in range(max_val)]
    ticks = [i+1 for i in values]

# Create figure
    fig = px.choropleth(
    df,
    geojson=geo_world_ok,
    locations='Country name',
    hover_data=["Ladder score",'Rank'],
    color=df['Ladder score'],
    range_color=(0, df['Ladder score'].max()),
)

# Define layout specificities
    fig.update_layout(
    margin={'r':0,'t':0,'l':0,'b':0},
    coloraxis_colorbar={
        'title':'Ladder score of World Hapiness',
        'tickvals':values,
        'ticktext':ticks        
    })


    url=py.plot(fig, filename = 'world_happiness', auto_open=False)
  

    return url
    

