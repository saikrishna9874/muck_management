import pandas as pd
import numpy as np
import plotly
import plotly.graph_objs as go
import matplotlib.pyplot as plt
from sklearn.svm import SVR



lagoon = pd.read_csv('final_data.csv')
fp = open('params.txt','r')
g = int(fp.readline())

latitudesList = lagoon['latitude'].tolist()
longitudeList = lagoon['longitude'].tolist()
depthList = lagoon['depth'].tolist()
mul_latitude = [x * 100 for x in latitudesList]
mul_longitude = [x * 100 for x in longitudeList]
lagoonList = lagoon.to_dict('records');
spring16,fall15,spring15,fall14,spring14,fall13,spring13,fall12,spring12,fall11,spring11,fall10,spring10,fall09,spring09,fall08,spring08,fall07,spring07,fall06,spring06,fall05=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
for tuple in lagoonList:
    spring16.append(tuple['spring\'16'])
    spring15.append(tuple['spring\'15'])
    spring14.append(tuple['spring\'14'])
    spring13.append(tuple['spring\'13'])
    spring12.append(tuple['spring\'12'])
    spring11.append(tuple['spring\'11'])
    spring10.append(tuple['spring\'10'])
    spring09.append(tuple['spring\'09'])
    spring08.append(tuple['spring\'08'])
    spring07.append(tuple['spring\'07'])
    spring06.append(tuple['spring\'06'])
    fall15.append(tuple['fall\'15'])
    fall14.append(tuple['fall\'14'])
    fall13.append(tuple['fall\'13'])
    fall12.append(tuple['fall\'12'])
    fall11.append(tuple['fall\'11'])
    fall10.append(tuple['fall\'10'])
    fall09.append(tuple['fall\'09'])
    fall08.append(tuple['fall\'08'])
    fall07.append(tuple['fall\'07'])
    fall06.append(tuple['fall\'06'])
    fall05.append(tuple['fall\'05'])

k = 0
for i in range(0,len(spring16)):
    if spring16[i] != 0:
        k=i
        break;
print(k)
depth_list = [x*0 for x in range(0,95)]
seasons=  [i for i in range(1,23)]
for i in range(k,len(spring16)):
    tpoints = [spring16[i],fall15[i],spring15[i],fall14[i],spring14[i],fall13[i],spring13[i],fall12[i],spring12[i],fall11[i],spring11[i],fall10[i],spring10[i],fall09[i],spring09[i],fall08[i],spring08[i],fall07[i],spring07[i],fall06[i],spring06[i],fall05[i]]
    points = list(reversed(tpoints))
    column_points = np.asarray(points).reshape(22, 1)
    column_seasons = np.asarray(seasons).reshape(22,1)
    svr_lin = SVR(kernel='linear', C=1e3)
    y_lin = svr_lin.fit(np.asarray(column_seasons), column_points).predict(g)
    depth_list.append(y_lin[0])
data = [go.Mesh3d(x=mul_latitude,y=mul_longitude,z=depth_list,
 colorscale = [[0, 'rgb(0, 255, 0)'],
                  [0.5, 'rgb(0, 0, 255)'],
                  [1, 'rgb(255, 0, 0)']],opacity=1.00),go.Mesh3d(x=mul_latitude,y=mul_longitude,z=depthList,
                   colorscale = [[0, 'rgb(0, 255, 0)'],
                                    [0.5, 'rgb(0, 0, 255)'],
                                    [1, 'rgb(255, 0, 0)']],opacity=0.5)
]

layout = go.Layout(
    xaxis=dict(
        title='latitude',
        autorange=True
    ),
    yaxis=dict(
        title='longitude',
        autorange=True
    )
)

plotly.offline.plot({
    "data": data,
    "layout":layout
}, auto_open=True)
