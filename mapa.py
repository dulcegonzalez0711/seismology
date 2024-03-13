import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.basemap import Basemap 
import pandas as pd 

# Cargar datos de eventos sísmicos
data = pd.read_csv('qsqn.csv') 

# Crear el mapa de Guatemala 
plt.figure(figsize=(10, 10)) 
m = Basemap(llcrnrlon=-93, llcrnrlat=12, urcrnrlon=-88, urcrnrlat=18.5, projection='merc', resolution='h') 

m.drawcoastlines() 
m.drawcountries(linewidth=1, color='black') 
m.drawstates() 
m.drawmapboundary(fill_color='#E6E6FA', linewidth=0)
m.fillcontinents(color='white', lake_color='#069AF3')

# Convertir coordenadas de longitud y latitud a coordenadas de mapa 

x, y = m(np.array(data['longitude']), np.array(data['latitude'])) # Trazar eventos sísmicos 
m.scatter(x, y, marker='o', color='#90EE90', zorder=4) 
plt.title('Localización geográfica de eventos sísmicos', fontsize=18) 
plt.savefig('mapaaa') 