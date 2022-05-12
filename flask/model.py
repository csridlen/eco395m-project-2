from word2vec_functions import *
import h2o
h2o.init()
import numpy as np
import pandas as pd
from math import sqrt
from h2o.estimators.word2vec import H2OWord2vecEstimator
from h2o.estimators.gbm import H2OGradientBoostingEstimator
import sklearn
from sklearn import ensemble
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer

# Initializing word2vec model
airbnb_path = "../data/newnh_airbnb_2021.csv"
airbnb_names = h2o.import_file(airbnb_path, destination_frame = "airbnbnames",
                             header = 1)
# Create word vectors
words = tokenize(airbnb_names["name"])
w2v_model = H2OWord2vecEstimator(sent_sample_rate = 0.0, epochs = 10)
w2v_model.train(training_frame = words)
airbnb_names_vecs = w2v_model.transform(words, aggregate_method = "AVERAGE")
valid_airbnb_names = ~ airbnb_names_vecs["C1"].isna()
data = airbnb_names[valid_airbnb_names,:].cbind(airbnb_names_vecs[valid_airbnb_names,:])
data_split = data.split_frame(ratios=[0.8])

gbm_model = H2OGradientBoostingEstimator()
gbm_model.train(x = airbnb_names_vecs.names,
                y= "price", 
                training_frame = data_split[0], 
                validation_frame = data_split[1])

# We can't just rely on the names because RMSE is pretty high

varimp = gbm_model.varimp(use_pandas=True)
top_20 = list(varimp.head(20)["variable"])

## In word2vec.ipynb, we see the top 20 most important categorizations
# Let's filter just for those 20
top_20_list = list(set(airbnb_names_vecs.names)  & set(top_20))
airbnb_names_vecs = airbnb_names_vecs[valid_airbnb_names, :]
airbnb_names_vecs = airbnb_names_vecs[top_20_list]
airbnb_names_vecs
#data = airbnb_names[valid_airbnb_names,:].cbind(airbnb_names_vecs[valid_airbnb_names,:])
#data

data = airbnb_names[valid_airbnb_names,:].cbind(airbnb_names_vecs).as_data_frame()

not_used = ["id", "host_id", "name", "host_name", "neighbourhood", "latitude", "longitude", "price", "last_review"]
X = data.drop(not_used, axis = 1)
# We want numbers to be of same type
dict_ints = {'minimum_nights': float,
             'number_of_reviews': float,
             'calculated_host_listings_count': float,
             'availability_365': float,
             'number_of_reviews_ltm': float
}
X = X.astype(dict_ints)
dict_cats = { 
    "neighbourhood_group": "category",
    "room_type": "category",
    "new_neighbourhood": "category"
}
list_cats = list(dict_cats.keys())

X = X.astype(dict_cats)
X.dtypes


# Convert y to float as well
y = data["price"].astype(float)

# One hot encode room type
encoder = OneHotEncoder(handle_unknown = "ignore")
encoder_df = pd.DataFrame(encoder.fit_transform(X[["room_type"]]).toarray())
# Merge with original dataset
X_df = X.join(encoder_df)

# Filter for top neighborhoods

# One hot encode neighborhoods
encoder_n = pd.DataFrame(encoder.fit_transform(X[["neighbourhood_group"]]).toarray())
encoder_n.columns = [4, 5, 6, 7, 8]
# Merge with original dataset
X = X_df.join(encoder_n)
# Drop original categorical vartiables
X.dtypes
X = X.drop(list_cats, axis = 1)
X.dtypes # all variables are floats
X = X.fillna(0)

## Create gradient-boosted model
# All feature names must be strings
X.columns = X.columns.astype(str)
# Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
params = {
    "n_estimators": 500,
    "max_depth": 10,
    "min_samples_split": 5,
    "learning_rate": 0.01,
    "loss": "squared_error"}
reg = ensemble.GradientBoostingRegressor(**params)
gbm_model = reg.fit(X_train, y_train)