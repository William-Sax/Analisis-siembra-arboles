import pandas as pd
from data.datos import arbolesRio,nuquiEstadistica
from helper.crearTabalasHTML import crearTabla

#Tabla de analisis de veredas de riosucio choco con siembra de mas de 250 arboles
tabla1 = pd.DataFrame(arbolesRio,columns=['Veredas','arboles'])
tabla2 = pd.DataFrame(nuquiEstadistica,columns=['Veredas','arboles'])

municipiosConMasSiembraArboles=tabla1.query('arboles>250')
municipiosConMasSiembraArboles2=tabla2.query('arboles>100')

print(municipiosConMasSiembraArboles)
print(municipiosConMasSiembraArboles2)

#crando tabalas 
crearTabla(municipiosConMasSiembraArboles,"riosucioSiembraArboles")
crearTabla(municipiosConMasSiembraArboles2,"nuquiSiembraArboles")
