# Word2vec for amenities
from readtable import * 
import h2o
h2o.init()
from h2o.estimators.word2vec import H2OWord2vecEstimator
from h2o.estimators.gbm import H2OGradientBoostingEstimator
from datetime import datetime
import numpy as np
import pandas as pd

airbnb_path = "../data/cleaned_data_updated.csv"
airbnb_words = h2o.import_file(airbnb_path, destination_frame = "airbnbwords",
                             header = 1)
STOP_WORDS = ["w/","at","from","in","to","/","*","-","w","+","and","&", "near", "next"]

def tokenize(sentences, stop_word = STOP_WORDS):
    tokenized = sentences.tokenize("\\W+")
    tokenized_lower = tokenized.tolower()
    tokenized_filtered = tokenized_lower[(tokenized_lower.nchar() >= 2) | (tokenized_lower.isna()),:]
    tokenized_words = tokenized_filtered[tokenized_filtered.grep("[0-9]",invert=True,output_logical=True),:]
    tokenized_words = tokenized_words[(tokenized_words.isna()) | (~ tokenized_words.isin(STOP_WORDS)),:]
    return tokenized_words

def predict(airbnb_names,w2v, gbm):
    words = tokenize(h2o.H2OFrame(airbnb_names).ascharacter())
    airbnb_words_vec = w2v.transform(words, aggregate_method="AVERAGE")
    print(gbm.predict(test_data=airbnb_words_vec))
    
words = tokenize(airbnb_words["amenities"])
w2v_model = H2OWord2vecEstimator(sent_sample_rate = 0.0, epochs = 10)
w2v_model.train(training_frame=words)

airbnb_words_vecs = w2v_model.transform(words, aggregate_method = "AVERAGE")

valid_airbnb_names = ~ airbnb_words_vecs["C1"].isna()
data = airbnb_words[valid_airbnb_names,:].cbind(airbnb_words_vecs[valid_airbnb_names,:])
data_split = data.split_frame(ratios=[0.8])

# gbm model
gbm_model = H2OGradientBoostingEstimator()
gbm_model.train(x = airbnb_words_vecs.names,
                y= "price", 
                training_frame = data_split[0], 
                validation_frame = data_split[1])