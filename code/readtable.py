import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

load_dotenv()

DATABASE_USERNAME = os.environ["DATABASE_USERNAME"]
DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
DATABASE_HOST = os.environ["DATABASE_HOST"]
DATABASE_PORT = os.environ["DATABASE_PORT"]
DATABASE_DATABASE = os.environ["DATABASE_DATABASE"]

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DATABASE}"

def getairbnbdata():
    db = create_engine(SQLALCHEMY_DATABASE_URL)
    conn = db.connect()
    sql = """
    SELECT id, month, "List_month", last_scraped, host_id, host_name, host_since, host_location, 
    host_response_time, host_response_rate, host_is_superhost, host_listings_count, host_total_listings_count, 
    neighbourhood, neighbourhood_cleansed, neighbourhood_group_cleansed, latitude, longitude, property_type,
    room_type, accommodates, bathrooms, bedrooms, beds, price, minimum_nights, maximum_nights, has_availability, 
    availability_30, availability_60, availability_90, availability_365, number_of_reviews, first_review,
    last_review, review_scores_rating, review_scores_accuracy, review_scores_cleanliness, review_scores_checkin,
    review_scores_communication, review_scores_location, review_scores_value, instant_bookable, 
    calculated_host_listings_count, reviews_per_month, amenities, scrape_batch, "batch_YRMO", days_since_rev,
    days_since_first_rev, host_length, host_is_superhost_dum, room_type_dum, instant_bookable_dum, 
    avg_lat, avg_lon, first_appearance, last_app, cum_sum, "List_month_byhost_month", "List_month_host_overall",
    "List_month_id_overall", hotel_dum, "List_month_byneigh"
    FROM public."listings2021" p
    WHERE drop_indicator = 0;
    """
    df = pd.read_sql_query(sql, con=conn, parse_dates=['last_scraped', 'host_since', 'first_review', 'last_review', 'scrape_batch'])

    #close connection
    conn.close()
    return df

def get_dists():
    # get airbnb data
    df = getairbnbdata()
    # merge with distance data
    clean_data_path = '../data/cleaned_data_updated.csv'
    select = ['id', 'station_dist', 'station_dist2', 'park_dist', 'park_dist2']
    distances = pd.read_csv(clean_data_path)[select]
    df = df.merge(distances, on = 'id', how = 'inner')
    return df