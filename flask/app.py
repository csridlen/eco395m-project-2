import pandas as pd
import numpy as np
import random
import os
import folium
import shutil
import time
from folium import plugins
import flask
from flask import Flask, render_template, request, redirect, session, url_for, make_response
import mapping as mp
import preprocess as pre
import model 


class MyFlask(flask.Flask):
    def get_send_file_max_age(self, name):
        if name.lower().endswith('map.html'):
            return 0
        return flask.Flask.get_send_file_max_age(self, name)

app = MyFlask(__name__)

app.secret_key = 'NYC Airbnb'


df = pd.read_csv("../data/newnh_airbnb_2021.csv")
not_used = ["id", "host_id", "host_name", "neighbourhood", "last_review", "license"]
X = df.drop(not_used, axis = 1)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/about')
def about():
    title = 'violet2 - '
    return render_template('about.html', title=title)



@app.route('/host')
def host():
    session['title'] = 'host - '
    session['customer'] = 'host'
    return render_template('host.html', title=session['title'], customer=session['customer'])


@app.route('/host/price', methods=['GET', 'POST'])
def hostprice():
    session['title'] = 'price estimation - '
    session['customer'] = 'host'
    return render_template('price.html', title=session['title'], customer=session['customer'],neighbourhood_dict=mp.id_neighborhood_dict, neighbourhood_group_dict=mp.id_neighbourhood_group_dict, room_type_dict=mp.id_room_type_dict)



# @app.route('/host/map', methods=['GET', 'POST'])
# def hostmap():

#     session['title'] = 'map - '
#     session['customer'] = 'host'
    
#     return render_template('mapnearby.html', title=session['title'], customer=session['customer'], neighbourhood_group_dict=mp.id_neighbourhood_group_dict)


# @app.route('/host/map/view', methods=['GET', 'POST'])
# def hostmapview():

#     session['title'] = 'map - '
#     session['customer'] = 'host'

#     if request.method == 'POST':
#         map_data = request.form.to_dict(flat=True)
#         session['map_data'] = map_data

#     if (session['map_data']['neighbourhood_group'][0]!='Select'):
#         NeighbourhoodGroupId = int(session['map_data']['neighbourhood_group'])

#         map = pre.make_map(X, NeighbourhoodGroupId)
#         map.save('static/maps/map.html')
#     else:
#         NeighbourhoodGroupId = 2
    
#     return render_template('mapnearbyview.html', title=session['title'], customer=session['customer'],
#                             neighbourhood_group_dict=mp.id_neighbourhood_group_dict, neighbourhood_group=mp.id_neighbourhood_group_dict[NeighbourhoodGroupId])


@app.route('/host/price/result', methods=['GET', 'POST'])
def pricepredict():

    if session['customer'] == 'host':
        session['title'] = 'smart price estimation - '
    else:
        session['title'] = 'price prediction - '

    if request.method == 'POST':
        form_data = request.form.to_dict(flat=True)
        session['form_data'] = form_data

        NeighbourhoodGroupId = int(form_data['neighbourhood_group'])
        pred = pre.regressor(form_data, NeighbourhoodGroupId, gbm_model)
        pred_total = pred*(int(form_data['minimum_nights']))
        
        # map = pre.make_map(X, NeighbourhoodGroupId)
        # map.save('static/maps/map.html')

    return render_template('priceresult.html', customer=session['customer'], title=session['title'], neighbourhood_group_dict=mp.id_neighbourhood_group_dict,
                           form_data=form_data, neighbourhood_group=mp.id_neighbourhood_group_dict[int(form_data['neighbourhood_group'])],
                           room_type_dict=mp.id_room_type_dict,
                           roomt=mp.id_room_type_dict[int(form_data['room_type'][0])], pred=pred, pred_total=pred_total)


if __name__ == '__main__':
    app.run()

