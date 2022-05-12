import pandas as pd
import numpy as np
import mapping as mp
import model 
import random
import os
import folium
import shutil
import time
from folium import plugins
import flask
from flask import Flask, render_template, request, redirect, session, url_for, make_response



class MyFlask(flask.Flask):
    def get_send_file_max_age(self, name):
        if name.lower().endswith('map.html'):
            return 0
        return flask.Flask.get_send_file_max_age(self, name)

app = MyFlask(__name__)

app.secret_key = 'NYC Airbnb'


df = pd.read_csv("../data/newnh_airbnb_2021.csv")

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
    return render_template('price.html', title=session['title'], customer=session['customer'], neighbourhood_dict=mp.id_neighborhood_dict,
                           neighbourhood_group_dict=mp.id_neighbourhood_group_dict, room_type_dict=mp.id_room_type_dict)



@app.route('/host/map', methods=['GET', 'POST'])
def hostmap():

    session['title'] = 'map - '
    session['customer'] = 'host'
    
    return render_template('mapnearby.html', title=session['title'], customer=session['customer'], neighbourhood_group_dict=mp.id_neighbourhood_group_dict)


@app.route('/host/map/view', methods=['GET', 'POST'])
def hostmapview():

    session['title'] = 'map - '
    session['customer'] = 'host'

    if request.method == 'POST':
        map_data = request.form.to_dict(flat=True)
        session['map_data'] = map_data

    if (session['map_data']['city'][0]!='Select'):
        CityId = int(session['map_data']['city'])

        map = pre.make_map(df, CityId)
        map.save('static/maps/map.html')
    else:
        CityId = 100
    
    return render_template('mapnearbyview.html', title=session['title'], customer=session['customer'],
                            city_dict=mp.id_city_dict, city_name=mp.id_city_dict[CityId], link=mp.nearby_id_link_dict[CityId],
                            label=mp.nearby_id_name_dict[CityId])


@app.route('/host/price/result', methods=['GET', 'POST'])
@app.route('/tourist/price/result', methods=['GET', 'POST'])
def pricepredict():

    if session['customer'] == 'host':
        session['title'] = 'smart price estimation - '
    else:
        session['title'] = 'price prediction - '

    if request.method == 'POST':
        form_data = request.form.to_dict(flat=True)
        session['form_data'] = form_data

        CityId = int(form_data['city'])
        pred = pre.regressor(form_data, CityId, reg)
        pred_total = pred*(int(form_data['minimum_nights']))
        
        map = pre.make_map(df, CityId)
        map.save('static/maps/map.html')

    return render_template('priceresult.html', customer=session['customer'], title=session['title'], city_dict=mp.id_city_dict,
                           popularity_dict=mp.id_pop_dict, form_data=form_data, city=mp.id_city_dict[int(form_data['city'])],
                           popu=mp.id_pop_dict[int(form_data['popularity'][0])], room_type_dict=mp.id_room_type_dict,
                           roomt=mp.id_room_type_dict[int(form_data['room_type'][0])], current_time=int(time.time()),
                           link=mp.nearby_id_link_dict[CityId], label=mp.nearby_id_name_dict[CityId], pred=pred, pred_total=pred_total)


@app.route('/data')
def data():
    session['title'] = 'data - '
    session['customer'] = 'data'
    return render_template('data.html', title=session['title'], customer=session['customer'])


if __name__ == '__main__':
    app.run()
© 2022 GitHub, Inc.
Terms
Privacy
