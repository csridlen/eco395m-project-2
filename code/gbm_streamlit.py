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

# Data
# airbnb = get_dists()

# airbnb['host_since'] = (pd.to_datetime(airbnb['last_scraped']) - pd.to_datetime(airbnb['host_since'])) / np.timedelta64(1, 'D')
# # columns we don't need for ML model
# drop = ['id', 'month', 'last_scraped', 'host_id', 'host_name', 'neighbourhood',
#        'latitude', 'longitude',
#        'first_review', 'last_review',
#        'scrape_batch', 'batch_YRMO',
#        'instant_bookable',
#        'host_location',
#        'host_is_superhost',
#        'cum_sum',
#        'has_availability',
#        'amenities',
#        'neighbourhood_cleansed',
#        'neighbourhood_group_cleansed',
#        'avg_lat',
#        'avg_lon',
#        'last_app',
#        'List_month_byhost_month',
#     'List_month_host_overall',
#     'List_month_id_overall',
#        'List_month_byneigh',
#        'property_type']
# data = airbnb.drop(drop, axis = 1)
# data.astype(str)
# dict_ints = {"List_month": float,
#             'host_is_superhost_dum': float,
#              'room_type_dum':float,
#              'instant_bookable_dum':float,
#              'hotel_dum':float,
#             'bathrooms': float}
# data = data.astype(dict_ints)
# X = data.dropna(subset = ['price']).loc[:, data.columns != 'price']
# y = data['price'].dropna()

# # One hot encoding
# # which variables are categorical?
# dict_cats = {"host_response_time": "category",
#              "room_type": "category"}

# # drop amenities for now
# # Need to make host_response rate as int
# X['host_response_rate'] = X['host_response_rate'].str[:-1].astype(float)

# X = X.astype(dict_cats)
# encoder = OneHotEncoder(handle_unknown = "ignore")
# encoder_hrt = pd.DataFrame(encoder.fit_transform(X[["host_response_time"]]).toarray())
# encoder_hrt.columns = list(X["host_response_time"].unique())

# # Merge with original dataset
# X = X.join(encoder_hrt)

# # Do same for room type
# encoder_rt = pd.DataFrame(encoder.fit_transform(X[["room_type"]]).toarray())
# encoder_rt.columns = list(X["room_type"].unique())

# X = X.join(encoder_rt)

# ## Drop original variables
# original = list(dict_cats.keys())
# X = X.drop(original, axis = 1)

# X.columns = X.columns.astype(str)
# drop2 = ["nan",
#        "first_appearance",
#        "review_scores_accuracy",
#        "within a few hours",
#        "Hotel room",
#        "a few days or more",
#        "Private room",
#        "within an hour",
#        "Entire home/apt",
#        "within a day",
#        "hotel_dum",
#        "bathrooms",
#        "List_month"]
# X = X.drop(drop2, axis = 1) # drop variables that aren't important
# #print(X.dtypes)
# X = X.fillna(0)

# # Split into train and test
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
# params = {
#     "n_estimators": 50,
#     "max_depth": 5,
#     "min_samples_split": 5,
#     "learning_rate": 0.01,
#     "loss": "squared_error"}
# reg = ensemble.GradientBoostingRegressor(**params)
# gbm_model = reg.fit(X_train, y_train)


# host_since = st.number_input('Host Since', 0, 2022, 0)
# host_listings_count = st.number_input('Number of Host Listings', 0, 20, 0)
# accommodates = st.number_input('Number of People Accommodated', 0, 20, 0)
# bedrooms = st.number_input('Number of Bedrooms', 0, 10, 0)
# beds = st.number_input('Number of Beds', 0, 15, 0)
# minimum_nights = st.number_input('Minimum Nights Required', 0, 30, 0)
# maximum_nights = st.number_input('Maximum Nights Available', 0, 1, 0)
# availability_365 = st.number_input('Number of Days Available per Year', 0, 365, 0)
# review_scores_rating = st.number_input('Review Scores - Rating', 0, 10, 0)
# reviews_per_month = st.number_input('Reviews Per Month', 0, 30, 0)
# days_since_rev = st.number_input('Days Since Last Review', 0, 365, 0)
# host_is_superhost_dum = st.number_input('Host is Superhost (1 = "yes", 0 ="no")', 0, 1, 0,1)
# instant_bookable_dum = st.number_input('Instantly Bookable (1 = "yes", 0 ="no")', 0, 1, 0,1)
# station_dist = st.number_input('Distance to Nearest Subway Station', 0, 100, 0)
# park_dist = st.number_input('Distance to Nearest Park', 0, 100, 0)

#neighborhood = st.selectbox(
     # 'Neighborhood',
     # ('Allerton', "Annadale-Huguenot-Prince's Bay-Woodrow", 'Arden Heights-Rossville', 'Astoria (Central)', 'Astoria (East)-Woodside (North)', 'Astoria (North)-Ditmars-Steinway', 'Astoria Park', 'Auburndale', 'Baisley Park', 'Bath Beach', 'Bay Ridge', 'Bay Terrace-Clearview', 'Bayside', 'Bedford Park', 'Bedford-Stuyvesant (East)', 'Bedford-Stuyvesant (West)', 'Bellerose', 'Belmont', 'Bensonhurst', 'Borough Park', 'Breezy Point-Belle Harbor-Rockaway Park-Broad Channel', 'Brighton Beach', 'Brooklyn Heights', 'Brooklyn Navy Yard', 'Brownsville', 'Bushwick (East)', 'Bushwick (West)', 'Calvary & Mount Zion Cemeteries', 'Calvert Vaux Park', 'Cambria Heights', 'Canarsie', 'Canarsie Park & Pier', 'Carroll Gardens-Cobble Hill-Gowanus-Red Hook', 'Castle Hill-Unionport', 'Central Park', 'Chelsea-Hudson Yards', 'Chinatown-Two Bridges', 'Claremont Park', 'Claremont Village-Claremont (East)', 'Clinton Hill', 'Co-op City', 'College Point', 'Concourse-Concourse Village', 'Coney Island-Sea Gate', 'Corona', 'Crotona Park', 'Crotona Park East', 'Crown Heights (North)', 'Crown Heights (South)', 'Cypress Hills', 'Douglaston-Little Neck', 'Downtown Brooklyn-DUMBO-Boerum Hill', 'Dyker Heights', 'East Elmhurst', 'East Flatbush-Erasmus', 'East Flatbush-Farragut', 'East Flatbush-Remsen Village', 'East Flatbush-Rugby', 'East Flushing', 'East Harlem (North)', 'East Harlem (South)', 'East Midtown-Turtle Bay', 'East New York (North)', 'East New York-City Line', 'East New York-New Lots', 'East Village', 'East Williamsburg', 'Eastchester-Edenwald-Baychester', 'Elmhurst', 'Far Rockaway-Bayswater', 'Financial District-Battery Park City', 'Flatbush', 'Flatbush (West)-Ditmas Park-Parkville', 'Flatlands', 'Flushing Meadows-Corona Park', 'Flushing-Willets Point', 'Fordham Heights', 'Forest Hills', 'Fort Greene', 'Fort Hamilton', 'Fresh Meadows-Utopia', 'Glen Oaks-Floral Park-New Hyde Park', 'Glendale', 'Gramercy', 'Grasmere-Arrochar-South Beach-Dongan Hills', 'Gravesend (East)-Homecrest', 'Gravesend (South)', 'Gravesend (West)', 'Great Kills-Eltingville', 'Greenpoint', 'Greenwich Village', 'Hamilton Heights-Sugar Hill', 'Harlem (North)', 'Harlem (South)', "Hell's Kitchen", 'Highbridge', 'Highbridge Park', 'Highland Park-Cypress Hills Cemeteries (North)', 'Hollis', 'Holy Cross Cemetery', 'Howard Beach-Lindenwood', 'Hunts Point', 'Hutchinson Metro Center', 'Inwood', 'Inwood Hill Park', 'Jackson Heights', 'Jacob Riis Park-Fort Tilden-Breezy Point Tip', 'Jamaica', 'Jamaica Estates-Holliswood', 'Jamaica Hills-Briarwood', 'Kensington', 'Kew Gardens', 'Kew Gardens Hills', 'Kingsbridge Heights-Van Cortlandt Village', 'Kingsbridge-Marble Hill', 'Kissena Park', 'Laurelton', 'Lincoln Terrace Park', 'Long Island City-Hunters Point', 'Longwood', 'Lower East Side', 'Madison', 'Manhattanville-West Harlem', 'Mapleton-Midwood (West)', 'Marine Park-Mill Basin-Bergen Beach', "Mariner's Harbor-Arlington-Graniteville", 'Maspeth', 'Melrose', 'Middle Village', 'Middle Village Cemetery', 'Midtown South-Flatiron-Union Square', 'Midtown-Times Square', 'Midwood', 'Montefiore Cemetery', 'Morningside Heights', 'Morris Park', 'Morrisania', 'Mott Haven-Port Morris', 'Mount Eden-Claremont (West)', 'Mount Hebron & Cedar Grove Cemeteries', 'Mount Hope', 'Mount Olivet & All Faiths Cemeteries', 'Murray Hill-Broadway Flushing', 'Murray Hill-Kips Bay', 'New Dorp-Midland Beach', 'New Springville-Willowbrook-Bulls Head-Travis', 'North Corona', 'Norwood', 'Oakland Gardens-Hollis Hills', 'Oakwood-Richmondtown', 'Ocean Hill', 'Old Astoria-Hallets Point', 'Ozone Park', 'Ozone Park (North)', 'Park Slope', 'Parkchester', 'Pelham Bay Park', 'Pelham Bay-Country Club-City Island', 'Pelham Gardens', 'Pelham Parkway-Van Nest', 'Pomonok-Electchester-Hillcrest', 'Port Richmond', 'Prospect Heights', 'Prospect Lefferts Gardens-Wingate', 'Prospect Park', 'Queens Village', 'Queensboro Hill', 'Queensbridge-Ravenswood-Dutch Kills', 'Rego Park', 'Richmond Hill', 'Ridgewood', 'Riverdale-Spuyten Duyvil', 'Rockaway Beach-Arverne-Edgemere', 'Rockaway Community Park', 'Rosebank-Shore Acres-Park Hill', 'Rosedale', 'Sheepshead Bay-Manhattan Beach-Gerritsen Beach', 'SoHo-Little Italy-Hudson Square', 'Soundview Park', 'Soundview-Bruckner-Bronx River', 'Soundview-Clason Point', 'South Jamaica', 'South Ozone Park', 'South Richmond Hill', 'South Williamsburg', 'Spring Creek-Starrett City', 'Springfield Gardens (North)-Rochdale Village', 'Springfield Gardens (South)-Brookville', 'St. Albans', 'St. George-New Brighton', 'St. John Cemetery', 'Stuyvesant Town-Peter Cooper Village', 'Sunnyside', 'Sunnyside Yards (North)', 'Sunnyside Yards (South)', 'Sunset Park (Central)', 'Sunset Park (East)-Borough Park (West)', 'Sunset Park (West)', 'The Battery-Governors Island-Ellis Island-Liberty Island', 'The Evergreens Cemetery', 'Throgs Neck-Schuylerville', 'Todt Hill-Emerson Hill-Lighthouse Hill-Manor Heights', 'Tompkinsville-Stapleton-Clifton-Fox Hills', 'Tottenville-Charleston', 'Tremont', 'Tribeca-Civic Center', 'United Nations', 'University Heights (North)-Fordham', 'University Heights (South)-Morris Heights', 'Upper East Side-Carnegie Hill', 'Upper East Side-Lenox Hill-Roosevelt Island', 'Upper East Side-Yorkville', 'Upper West Side (Central)', 'Upper West Side-Lincoln Square', 'Upper West Side-Manhattan Valley', 'Van Cortlandt Park', 'Wakefield-Woodlawn', 'Washington Heights (North)', 'Washington Heights (South)', 'West Farms', 'West New Brighton-Silver Lake-Grymes Hill', 'West Village', 'Westchester Square', 'Westerleigh-Castleton Corners', 'Whitestone-Beechhurst', 'Williamsbridge-Olinville', 'Williamsburg', 'Windsor Terrace-South Slope', 'Woodhaven', 'Woodside', 'Yankee Stadium-Macombs Dam Park'))
        
        
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(host_since, host_response_rate, accomodates, bedrooms, beds, minimum_nights, availability_365, review_scores_rating, days_since_rev, host_is_superhost_dum, instant_bookable_dum, station_dist, park_dist, host_total_listings_count):   
 
 
    # Making predictions 
    prediction = gbm_model.predict( 
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