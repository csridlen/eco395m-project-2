import folium
from folium import plugins
import mapping as mp
import numpy as np
import model

# def make_map(X, NeighbourhoodGroupId):

#     NeighbourhoodGroup = mp.id_neighbourhood_group_dict[NeighbourhoodGroupId]

#     dfs = X[X['neighbourhood_group']==NeighbourhoodGroup].drop(['neighbourhood_group'], axis=1)
#     # if dfs.shape[0]>=1500:
#     #     dfs = dfs.sample(n=1500)
#     dfs = dfs.values.tolist()

#     map = folium.Map(mp.neighbourhood_group_latlong_dict[NeighbourhoodGroupId], zoom_start=12,
#                     width='100%',
#                     height='100%')
#     clusts = plugins.MarkerCluster().add_to(map)

#     for l, l1, l2, t, pr, mn, nr, rpm, clc, a365, nrl, nn in dfs:
#         pop_up = f'{l} || Type: {t} ||  Reviews: {nr} || Availability 365: {a365} || Price: ${pr}/night'
#         if t=='Entire Home':
#             folium.Marker([l1, l2], 
#                         icon=folium.Icon(color='black',icon='home', prefix='fa'),
#                         popup=pop_up).add_to(clusts)
#         if t=='Hotel Room':
#             folium.Marker([l1, l2], 
#                         icon=folium.Icon(color='black',icon='bed', prefix='fa'),
#                         popup=pop_up).add_to(clusts)
#         if t=='Private Room':
#             folium.Marker([l1, l2], 
#                         icon=folium.Icon(color='black',icon='user', prefix='fa'),
#                         popup=pop_up).add_to(clusts)
#         if t=='Shared Room':
#             folium.Marker([l1, l2], 
#                         icon=folium.Icon(color='black',icon='users', prefix='fa'),
#                         popup=pop_up).add_to(clusts)

#     return map


def regressor(form_data, NeighbourhoodGroupId, gbm_model):
    
    test = [int(form_data['room_type']), np.log1p(float(form_data['minimum_nights'])), float(form_data['number_of_reviews']),
            np.sqrt(float(form_data['number_of_reviews_ltm'])), float(form_data['calculated_host_listings_count']),
            float(form_data['availability_365']), int(form_data['neighbourhood']), float(form_data['neighbourhood_group'])]

    return float(round(np.expm1(list(gbm_model.predict([test]))[0]), 0))