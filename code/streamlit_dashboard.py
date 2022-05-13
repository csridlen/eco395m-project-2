import streamlit as st
import pandas as pd 
import plotly.express as px
from word2vec_functions import *
import h2o
h2o.init()
import numpy as np
import pandas as pd
from math import sqrt
from readtable import *
import numpy as np
from sklearn import ensemble
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.metrics import mean_squared_error
from math import sqrt
import matplotlib.pyplot as plt

# Initializing word2vec model
# airbnb_path = "../data/newnh_airbnb_2021.csv"
# airbnb_names = h2o.import_file(airbnb_path, destination_frame = "airbnbnames",
#                              header = 1)
# Create word vectors
# words = tokenize(airbnb_names["name"])
# w2v_model = H2OWord2vecEstimator(sent_sample_rate = 0.0, epochs = 10)
# w2v_model.train(training_frame = words)
# airbnb_names_vecs = w2v_model.transform(words, aggregate_method = "AVERAGE")
# valid_airbnb_names = ~ airbnb_names_vecs["C1"].isna()
# data = airbnb_names[valid_airbnb_names,:]
# data_split = data.split_frame(ratios=[0.8])

# gbm_model = H2OGradientBoostingEstimator()
# gbm_model.train(x = airbnb_names_vecs.names,
#                 y= "price", 
#                 training_frame = data_split[0], 
#                 validation_frame = data_split[1])

# # We can't just rely on the names because RMSE is pretty high

# varimp = gbm_model.varimp(use_pandas=True)
# top_20 = list(varimp.head(20)["variable"])

# ## In word2vec.ipynb, we see the top 20 most important categorizations
# # Let's filter just for those 20
# top_20_list = list(set(airbnb_names_vecs.names)  & set(top_20))
# airbnb_names_vecs = airbnb_names_vecs[valid_airbnb_names, :]
# airbnb_names_vecs = airbnb_names_vecs[top_20_list]
# airbnb_names_vecs
#data = airbnb_names[valid_airbnb_names,:].cbind(airbnb_names_vecs[valid_airbnb_names,:])
#data

# data = pd.read_csv("../data/newnh_airbnb_2021.csv")

# not_used = ["id", "host_id", "name", "host_name", "neighbourhood", "latitude", "longitude", "price", "last_review", "license", "new_neighbourhood"]
# X = data.drop(not_used, axis = 1)
# # We want numbers to be of same type
# dict_ints = {'minimum_nights': float,
#              'number_of_reviews': float,
#              'calculated_host_listings_count': float,
#              'availability_365': float,
#              'number_of_reviews_ltm': float
# }
# X = X.astype(dict_ints)
# dict_cats = { 
#     "neighbourhood_group": "category",
#     "room_type": "category"
# }
# list_cats = list(dict_cats.keys())

# X = X.astype(dict_cats)
#X.dtypes


# Convert y to float as well
# y = data["price"].astype(float)

# # One hot encode room type
# encoder = OneHotEncoder(handle_unknown = "ignore")
# encoder_df = pd.DataFrame(encoder.fit_transform(X[["room_type"]]).toarray())
# # Merge with original dataset
# X_df = X.join(encoder_df)

# Filter for top neighborhoods

# One hot encode neighborhoods
# encoder_n = pd.DataFrame(encoder.fit_transform(X[["neighbourhood_group"]]).toarray())
# encoder_n.columns = [4, 5, 6, 7, 8]
# # Merge with original dataset
# X = X_df.join(encoder_n)
# # Drop original categorical vartiables
# #X.dtypes
# X = X.drop(list_cats, axis = 1)
# #X.dtypes # all variables are floats
# X = X.fillna(0)

# ## Create gradient-boosted model
# # All feature names must be strings
# X.columns = X.columns.astype(str)
# # Split into train and test
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
# params = {
#     "n_estimators": 500,
#     "max_depth": 10,
#     "min_samples_split": 5,
#     "learning_rate": 0.01,
#     "loss": "squared_error"}
# reg = ensemble.GradientBoostingRegressor(**params)
# gbm_model = reg.fit(X_train, y_train)
#writing the function. 
#Turning csv file into dataframe

#@st.cache
# def load_data():
#     """ Function for loading data"""
#     df =pd.read_csv("../data/data_2021_distance.csv")

    
#     numeric_df = df.select_dtypes(['float', 'int'])
#     numeric_cols = numeric_df.columns
    
#     text_df = df.select_dtypes(['object'])
#     text_cols = text_df.columns
    
   
#    return df, numeric_cols, text_cols, numeric_df, text_df


# # df, numeric_cols, text_cols = load_data()

# # find data mean or mode to set as default value
# mnn = df["minimum_nights"].mean()
# nrv = df["number_of_reviews"].mean()
# hlc = df["calculated_host_listings_count"].mean()
# avallyear = df["availability_365"].mean()
# nrevltm = df["number_of_reviews_ltm"].mean()

# nbg = df["neighbourhood_group"].mode()
# nb = df["new_neighbourhood"].mode()
# rt = df["room_type"].mode()


#Title for the dashboard

st.title("NYC Airbnb Smart Pricing")


# showing dataset 
#st.write(df)

#Adding checkbox to sidebar

#check_box = st.sidebar.checkbox(label = "Display dataset")

#if check_box:
    #show the dataset
    #st.write(df)
    
#giving sidebar a title

# st.sidebar.title("Settings")
# feature_selection =st.sidebar.multiselect(label = "Variables" , options =numeric_cols)

# print(feature_selection)
# df_features = df[feature_selection]
# plotly_figure = px.line(data_frame=df_features, x=df_features.index, y=feature_selection)

neighborhood_group = st.selectbox(
     'Neighborhood Group',
     ('Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island'))

minimum_nights = st.number_input('Minimum Number of Nights', 0, 30, 0, 1)

number_of_reviews = st.number_input('Number of Reviews', 0, 150, 0, 1)

number_of_reviews = st.number_input('Reviews per Month', 0, 30, 0)

calculated_host_listings_count = st.number_input('Number of Host Listings', 0, 50, 0, 1)

availability_365 = st.number_input('Number of Days Per Year Availables', 0, 365, 0, 1)

number_of_reviews_ltm = st.number_input('Number of Reviews in the Last 12 Months', 0, 150, 0, 1)

room_type = st.selectbox(
     'Room Type',
     ('Shared Room', 'Private Room', 'Entire Home/Apt', 'Hotel Room'))

# @st.cache
# def rt0(room_type):
#     if room_type=='Entire Home/Apt':
#         return 1 
#     else:
#         return 0
    
# @st.cache    
# def rt1(room_type):
#     if room_type=='Hotel Room':
#         return 1
#     else:
#         return 0
    
# @st.cache    
# def rt2(room_type):
#     if room_type=='Private Room':
#         return 1
#     else:
#         return 0
    
# @st.cache
# def rt3(room_type):
#     if room_type =='Shared Room':
#         return 1
#     else:
#         return 0

# @st.cache
# def ng4(neighborhood_group):
#     if neighborhood_group=='Bronx':
#         return 1 
#     else:
#         return 0

# @st.cache
# def ng5(neighborhood_group):
#     if neighborhood_group=='Brooklyn':
#         return 1 
#     else:
#         return 0

# @st.cache
# def ng6(neighborhood_group):
#     if neighborhood_group=='Manhattan':
#         return 1 
#     else:
#         return 0

# @st.cache    
# def ng7(neighborhood_group):
#     if neighborhood_group=='Queens':
#         return 1 
#     else:
#         return 0

# @st.cache
# def ng8(neighborhood_group):
#     if neighborhood_group=='Staten Island':
#         return 1 
#     else:
#         return 0
    
neighborhood = st.selectbox(
     'Neighborhood',
     ('Allerton', "Annadale-Huguenot-Prince's Bay-Woodrow", 'Arden Heights-Rossville', 'Astoria (Central)', 'Astoria (East)-Woodside (North)', 'Astoria (North)-Ditmars-Steinway', 'Astoria Park', 'Auburndale', 'Baisley Park', 'Bath Beach', 'Bay Ridge', 'Bay Terrace-Clearview', 'Bayside', 'Bedford Park', 'Bedford-Stuyvesant (East)', 'Bedford-Stuyvesant (West)', 'Bellerose', 'Belmont', 'Bensonhurst', 'Borough Park', 'Breezy Point-Belle Harbor-Rockaway Park-Broad Channel', 'Brighton Beach', 'Brooklyn Heights', 'Brooklyn Navy Yard', 'Brownsville', 'Bushwick (East)', 'Bushwick (West)', 'Calvary & Mount Zion Cemeteries', 'Calvert Vaux Park', 'Cambria Heights', 'Canarsie', 'Canarsie Park & Pier', 'Carroll Gardens-Cobble Hill-Gowanus-Red Hook', 'Castle Hill-Unionport', 'Central Park', 'Chelsea-Hudson Yards', 'Chinatown-Two Bridges', 'Claremont Park', 'Claremont Village-Claremont (East)', 'Clinton Hill', 'Co-op City', 'College Point', 'Concourse-Concourse Village', 'Coney Island-Sea Gate', 'Corona', 'Crotona Park', 'Crotona Park East', 'Crown Heights (North)', 'Crown Heights (South)', 'Cypress Hills', 'Douglaston-Little Neck', 'Downtown Brooklyn-DUMBO-Boerum Hill', 'Dyker Heights', 'East Elmhurst', 'East Flatbush-Erasmus', 'East Flatbush-Farragut', 'East Flatbush-Remsen Village', 'East Flatbush-Rugby', 'East Flushing', 'East Harlem (North)', 'East Harlem (South)', 'East Midtown-Turtle Bay', 'East New York (North)', 'East New York-City Line', 'East New York-New Lots', 'East Village', 'East Williamsburg', 'Eastchester-Edenwald-Baychester', 'Elmhurst', 'Far Rockaway-Bayswater', 'Financial District-Battery Park City', 'Flatbush', 'Flatbush (West)-Ditmas Park-Parkville', 'Flatlands', 'Flushing Meadows-Corona Park', 'Flushing-Willets Point', 'Fordham Heights', 'Forest Hills', 'Fort Greene', 'Fort Hamilton', 'Fresh Meadows-Utopia', 'Glen Oaks-Floral Park-New Hyde Park', 'Glendale', 'Gramercy', 'Grasmere-Arrochar-South Beach-Dongan Hills', 'Gravesend (East)-Homecrest', 'Gravesend (South)', 'Gravesend (West)', 'Great Kills-Eltingville', 'Greenpoint', 'Greenwich Village', 'Hamilton Heights-Sugar Hill', 'Harlem (North)', 'Harlem (South)', "Hell's Kitchen", 'Highbridge', 'Highbridge Park', 'Highland Park-Cypress Hills Cemeteries (North)', 'Hollis', 'Holy Cross Cemetery', 'Howard Beach-Lindenwood', 'Hunts Point', 'Hutchinson Metro Center', 'Inwood', 'Inwood Hill Park', 'Jackson Heights', 'Jacob Riis Park-Fort Tilden-Breezy Point Tip', 'Jamaica', 'Jamaica Estates-Holliswood', 'Jamaica Hills-Briarwood', 'Kensington', 'Kew Gardens', 'Kew Gardens Hills', 'Kingsbridge Heights-Van Cortlandt Village', 'Kingsbridge-Marble Hill', 'Kissena Park', 'Laurelton', 'Lincoln Terrace Park', 'Long Island City-Hunters Point', 'Longwood', 'Lower East Side', 'Madison', 'Manhattanville-West Harlem', 'Mapleton-Midwood (West)', 'Marine Park-Mill Basin-Bergen Beach', "Mariner's Harbor-Arlington-Graniteville", 'Maspeth', 'Melrose', 'Middle Village', 'Middle Village Cemetery', 'Midtown South-Flatiron-Union Square', 'Midtown-Times Square', 'Midwood', 'Montefiore Cemetery', 'Morningside Heights', 'Morris Park', 'Morrisania', 'Mott Haven-Port Morris', 'Mount Eden-Claremont (West)', 'Mount Hebron & Cedar Grove Cemeteries', 'Mount Hope', 'Mount Olivet & All Faiths Cemeteries', 'Murray Hill-Broadway Flushing', 'Murray Hill-Kips Bay', 'New Dorp-Midland Beach', 'New Springville-Willowbrook-Bulls Head-Travis', 'North Corona', 'Norwood', 'Oakland Gardens-Hollis Hills', 'Oakwood-Richmondtown', 'Ocean Hill', 'Old Astoria-Hallets Point', 'Ozone Park', 'Ozone Park (North)', 'Park Slope', 'Parkchester', 'Pelham Bay Park', 'Pelham Bay-Country Club-City Island', 'Pelham Gardens', 'Pelham Parkway-Van Nest', 'Pomonok-Electchester-Hillcrest', 'Port Richmond', 'Prospect Heights', 'Prospect Lefferts Gardens-Wingate', 'Prospect Park', 'Queens Village', 'Queensboro Hill', 'Queensbridge-Ravenswood-Dutch Kills', 'Rego Park', 'Richmond Hill', 'Ridgewood', 'Riverdale-Spuyten Duyvil', 'Rockaway Beach-Arverne-Edgemere', 'Rockaway Community Park', 'Rosebank-Shore Acres-Park Hill', 'Rosedale', 'Sheepshead Bay-Manhattan Beach-Gerritsen Beach', 'SoHo-Little Italy-Hudson Square', 'Soundview Park', 'Soundview-Bruckner-Bronx River', 'Soundview-Clason Point', 'South Jamaica', 'South Ozone Park', 'South Richmond Hill', 'South Williamsburg', 'Spring Creek-Starrett City', 'Springfield Gardens (North)-Rochdale Village', 'Springfield Gardens (South)-Brookville', 'St. Albans', 'St. George-New Brighton', 'St. John Cemetery', 'Stuyvesant Town-Peter Cooper Village', 'Sunnyside', 'Sunnyside Yards (North)', 'Sunnyside Yards (South)', 'Sunset Park (Central)', 'Sunset Park (East)-Borough Park (West)', 'Sunset Park (West)', 'The Battery-Governors Island-Ellis Island-Liberty Island', 'The Evergreens Cemetery', 'Throgs Neck-Schuylerville', 'Todt Hill-Emerson Hill-Lighthouse Hill-Manor Heights', 'Tompkinsville-Stapleton-Clifton-Fox Hills', 'Tottenville-Charleston', 'Tremont', 'Tribeca-Civic Center', 'United Nations', 'University Heights (North)-Fordham', 'University Heights (South)-Morris Heights', 'Upper East Side-Carnegie Hill', 'Upper East Side-Lenox Hill-Roosevelt Island', 'Upper East Side-Yorkville', 'Upper West Side (Central)', 'Upper West Side-Lincoln Square', 'Upper West Side-Manhattan Valley', 'Van Cortlandt Park', 'Wakefield-Woodlawn', 'Washington Heights (North)', 'Washington Heights (South)', 'West Farms', 'West New Brighton-Silver Lake-Grymes Hill', 'West Village', 'Westchester Square', 'Westerleigh-Castleton Corners', 'Whitestone-Beechhurst', 'Williamsbridge-Olinville', 'Williamsburg', 'Windsor Terrace-South Slope', 'Woodhaven', 'Woodside', 'Yankee Stadium-Macombs Dam Park'))

#inputs = [minimum_nights, number_of_reviews, reviews_per_month, calculated_host_listings_count, availability_365, number_of_reviews_ltm, rt0(room_type), rt1(room_type), rt2(room_type), rt3(room_type), ng4(neighborhood_group), ng5(neighborhood_group), ng6(neighborhood_group), ng7(neighborhood_group), ng8(neighborhood_group)]

#X = pd.DataFrame(inputs, columns = ['minimum_nights','number_of_reviews', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365', 'number_of_reviews_ltm', '0', '1', '2', '3', '4', '5', '6', '7', '8'])

#pred = gbm_model.predict(X)

st.metric(label="Predicted Price", value=200, delta= 5.00, delta_color="inverse")

