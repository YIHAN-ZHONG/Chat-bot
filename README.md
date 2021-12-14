# Chat-bot
The objective of the project is to create a chat bot in discord with predefined commands to produce data visualization of the world happiness report as output.                             

In order to do this, the following packages are needed: chart-studio , plotly , -U discord , -U python-dotenv, matplotlib, numpy and pandas. 

**NB: To execute our program you need to have all this installed in your computer   **                         

 The data used was that of the world happiness level. it is data set of 150 different countries with different indicators to represent their happiness level per country.                                          
Furthermore three different graphs are plotted: 

 A map: present the different countries and their ladder score (happiness level). 

A pie chart: present the average value of the life expectancy rate per regions. it takes as parameter the region.  

 A stacked bar chart:  present the average ladder score value per region in descending order.        

In addition to this, for the map and pie chart we return an URL link, and the user can click on the link, which will lead him to an interactive graph html to better visualize. 

                     

Finally, the different names and help of the graphs are: 

Graph1   

Name: map_country_happiness      

Help:  This command responds to the happiness level of each country on the map. 

Graph2 

Name: life_expectancy  

Help:  This command shows the different happiness level in a bar chat with its different indicator component grouped by region. 

Graph3 

Name: pie_mean_happiness     

Help: This command takes regional indicator as parameter and returns the mean life expectancy rate per region. 

**NB. In order to call these commands you need to write the “$” followed by the name of the graph. Also, we will have to choose as parameter a region from this sets { Western_Europe , Latin_America_and_Caribbean, Central_and_Eastern_Europe, North_America_and_ANZ, East_Asia, Middle_East_and_North_Africa} **
