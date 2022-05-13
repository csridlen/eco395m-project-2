import pandas as pd
from sqlalchemy import create_engine

def getairbnbdata():
    conn_string = 'postgresql://postgres:eco395m@34.132.71.22:5432/airbnb'

    db = create_engine(conn_string)
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
    distances = pd.read_csv(clean_data_path).iloc[:, -4:]
    df = pd.concat([df, distances])
    return df
