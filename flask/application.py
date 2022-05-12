from flask import (Flask, render_template, flash,
                    request, jsonify, Markup)
import logging, io, os, sys
import pandas as pd
import numpy as np
from modules.custom_transformers import *
from sklearn.ensemble import GradientBoostingRegressor
import scipy
import pickle



# EB looks for an 'application' callable by default.
application = Flask(__name__)

np.set_printoptions(precision=2)

#Model features
gbm_model = None
features = ['neighbourhood_group', 'new_neighbourhood', 'room_type', 'minimum_nights', 'number_of_reviews', 'number_of_reviews_ltm',
         'calculated_host_listing_count', 'availability_365'] 

# need to import gbm and mappings
@application.before_first_request
def startup():

    global gbm_model
    
    # gbm model
    with open('static/predict_wnames.ipynb', 'rb') as f:
        gbm_model = pickle.load(f)

        # min, max, default values to categories mapping dictionary
    with open('static/Dictionaries.pkl', 'rb') as f:
        default_dict,min_dict, max_dict, default_dict_mapped = pickle.load(f)

    # Encoded values to categories mapping dictionary
    with open('static/Encoded_dicts.pkl', 'rb') as f:
        le_neighbourhood_group_Encdict,le_new_neighbourhood_Encdict,le_room_type_Encdict = pickle.load(f)


@application.errorhandler(500)
def server_error(e):
    logging.exception('some eror')
    return """
    And internal error <pre>{}</pre>
    """.format(e), 500

@application.route("/", methods=['POST', 'GET'])
def index():
     # Encoded values to categories mapping dictionary
      # Encoded values to categories mapping dictionary
    with open('static/Encoded_dicts.pkl', 'rb') as f:
        le_neighbourhood_group_Encdict,le_new_neighbourhood_Encdict,le_room_type_Encdict= pickle.load(f)


    return render_template( 'index.html',le_neighbourhood_group_Encdict = le_neighbourhood_group_Encdict,le_new_neighbourhood_Encdict = le_new_neighbourhood_Encdict, le_room_type_Encdict = le_room_type_Encdict, price_prediction = 17.09)



# accepts either deafult values or user inputs and outputs prediction 
@application.route('/background_process', methods=['POST', 'GET'])
def background_process():
    Neighbourhood_Group = request.args.get('neighbourhood_group')                                        
    New_Neighbourhood = request.args.get('new_neighbourhood')                                        
    Room_Type = request.args.get('room_type')
    Minimum_nights = float(request.args.get('minimum_nights'))                                          
    Number_of_Reviews = float(request.args.get('number_of_reviews'))                
    Number_of_Reviews_ltm = float(request.args.get('number_of_reviews_ltm'))
    Calculated_Host_Listing_Count = float(request.args.get('calculated_host_listing_count'))
    Availability_365 = float(request.args.get('availability_365'))


	# values stroed in list later to be passed as df while prediction
    user_vals = [Neighbourhood_Group, New_Neighbourhood, Room_Type, Minimum_nights, Number_of_Reviews, 
        Number_of_Reviews_ltm, Calculated_Host_Listing_Count, Availability_365]


    x_test_tmp = pd.DataFrame([user_vals],columns = features)
    float_formatter = "{:.2f}".format

    pred = float_formatter(np.exp(gbm_model.predict(x_test_tmp[features])[0]))
    return jsonify({'price_prediction':pred})

# when running app locally
if __name__ == '__main__':
    application.debug = False
    application.run(host='0.0.0.0')