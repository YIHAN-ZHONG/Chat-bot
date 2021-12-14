
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def Average_score_regional ():

    df=pd.read_csv('world-happiness-report-2021.csv')
    df_regional=df.groupby('Regional indicator').mean().reset_index().sort_values('Ladder score', ascending = True)

    ladderscore=[float("{:.2f}".format(y_value)) for y_value in df_regional['Ladder score'].values]
    
    df_indicator=df_regional.iloc[:,[0,-7,-6,-5,-4,-3,-2,-1]]
    

    sns.set_style("white")
    sns.set_color_codes('pastel')
    
    #fig, ax = plt.subplots()
    df_indicator.set_index('Regional indicator').plot(kind='barh', stacked=True,figsize = (20,6))
    #ax.set(title='Average Happiness Ladder score for different regions',xlabel='Ladder score',ylabel='Regional indicator')
    plt.title('Average Happiness Ladder score for different regions', fontsize=16)
    plt.xlabel('Ladder score')
    plt.ylabel('Regional indicator')
    plt.yticks(fontsize=8)   
    plt.legend(loc='best',fontsize=8,title='Hapiness categories')
    for i, v in enumerate(ladderscore):
        plt.text(v, i, str(v)) 
    
    filename =  "graph3.png"
    plt.savefig(filename)
    #image = discord.File(filename)

    return filename
    
    

#Average_score_regional ()




