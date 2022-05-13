import streamlit as st
import pandas as pd 
import plotly.express as px
import h2o
h2o.init()
import numpy as np
import pandas as pd
from math import sqrt
#from readtable import *
import numpy as np
from sklearn import ensemble
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt
from readtable import *
import pickle

pickle_in = open('gbmmodel.pkl', 'rb') 
model = pickle.load(pickle_in)
        
        
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(host_since, host_response_rate, accomodates, bedrooms, beds, minimum_nights, availability_365, review_scores_rating, days_since_rev, host_is_superhost_dum, instant_bookable_dum, station_dist, park_dist, host_total_listings_count):   
 
 
    # Making predictions 
    prediction = model.predict( 
        [[host_since, host_response_rate, accomodates, bedrooms, beds, minimum_nights, availability_365, review_scores_rating, days_since_rev, host_is_superhost_dum, instant_bookable_dum, station_dist, park_dist, host_total_listings_count]])
     
    if prediction == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Airbnb Smart Pricing </h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    host_since = st.number_input('Host Since', 1910, 2022, 2020, 1)
    host_response_rate = st.number_input('Host Response Rate', 0, 1, 0)
    #host_listings_count = st.number_input('Number of Host Listings', 0, 20, 0, 1)
    accomodates = st.number_input('Number of People Accommodated', 0, 20, 0, 1)
    bedrooms = st.number_input('Number of Bedrooms', 0, 10, 0, 1)
    beds = st.number_input('Number of Beds', 0, 15, 0, 1)
    minimum_nights = st.number_input('Minimum Nights Required', 0, 30, 0, 1)
    #maximum_nights = st.number_input('Maximum Nights Available', 0, 1, 0, 1)
    availability_365 = st.number_input('Number of Days Available in the Last Year', 0, 365, 0, 1)
    review_scores_rating = st.number_input('Review Scores - Rating', 0, 10, 0)
    #reviews_per_month = st.number_input('Reviews Per Month', 0, 30, 0)
    days_since_rev = st.number_input('Days Since Last Review', 0, 365, 0, 1)
    host_is_superhost_dum = st.number_input('Host is Superhost (1 = "yes", 0 ="no")', 0, 1, 0,1)
    instant_bookable_dum = st.number_input('Instantly Bookable (1 = "yes", 0 ="no")', 0, 1, 0,1)
    station_dist = st.number_input('Distance to Nearest Subway Station (in miles)', 0, 100, 0)
    park_dist = st.number_input('Distance to Nearest Park (in miles)', 0, 100, 0)
    host_total_listings_count = st.number_input('Total Number of Host Listing', 0, 30, 0, 1)
    #availability_30 = st.number_input('Number of Days Available in the Last Month', 0, 30, 0,1)
    #availability_60 = st.number_input('Number of Days Available in the last 2 Months', 0, 60, 0,1)
    #availability_90 = st.number_input('Number of Days Available in the last 3 Months', 0, 90, 0,1)
    #days_since_first_rev = st.number_input('Days Since First Review', 0, 500, 0, 1)
    #host_length = st.number_input('Host Length', 0, 300, 0, 1)
    #room_type_dum = st.number_input('Room Type (1 = "yes", 0 ="no")', 0, 1, 0,1)
    #station_dist2 = st.number_input('Distance 2 to Nearest Subway Station (in miles)', 0, 100, 0)
    #park_dist2 = st.number_input('Distance 2 to Nearest Park (in miles)', 0, 100, 0)
    #Shared room = st.number_input('Shared Room (1 = "yes", 0 ="no")', 0, 1, 0,1)
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(host_since, host_response_rate, accomodates, bedrooms, beds, minimum_nights, availability_365, review_scores_rating, days_since_rev, host_is_superhost_dum, instant_bookable_dum, station_dist, park_dist, host_total_listings_count) 
        st.success('Your Predicted Price per Night is {}'.format(result))
        print(result)

#inputs = [minimum_nights, number_of_reviews, reviews_per_month, calculated_host_listings_count, availability_365, number_of_reviews_ltm, rt0(room_type), rt1(room_type), rt2(room_type), rt3(room_type), ng4(neighborhood_group), ng5(neighborhood_group), ng6(neighborhood_group), ng7(neighborhood_group), ng8(neighborhood_group)]

#X = pd.DataFrame(inputs, columns = ['minimum_nights','number_of_reviews', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365', 'number_of_reviews_ltm', '0', '1', '2', '3', '4', '5', '6', '7', '8'])

#pred = gbm_model.predict(X)

#idx = random.randint(100,250)

#st.metric(label="Predicted Price", value=idx)

if __name__=='__main__': 
    main()