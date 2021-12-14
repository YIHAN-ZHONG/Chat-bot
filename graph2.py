
import plotly.express as px
import pandas as pd
import numpy as np 
import chart_studio
import chart_studio.plotly as py

def life_expetency_regional(region):
    
    df=pd.read_csv('world-happiness-report-2021.csv')
#we calculated the exponential values of ladder score to better appreciate and present the relation between it(ladder  score) and the life health expectancy
    df['exp_values']=np.exp(df['Ladder score'])

    df['Regional indicator']= df['Regional indicator'].str.replace(' ','_',regex=True)


    df_region=df[df['Regional indicator']==region]
    
    hover_dic={'exp_values':False,'Country name':True}

    fig = px.sunburst(df_region, path=['Regional indicator', 'Country name'], values='exp_values',
                  color='Healthy life expectancy', hover_data=hover_dic, title="Life expentency of each country related to there happiness level")


    url=py.plot(fig, filename = 'world_happiness_regional_barh', auto_open=False)
  

    return url

life_expetency_regional('Western_Europe')