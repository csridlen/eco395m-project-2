import pandas as pd

df = pd.read_csv("../data/newnh_airbnb_2021.csv")
df2 = df.groupby('new_neighbourhood')
df2 = pd.DataFrame(df2.first())
df2.reset_index(inplace=True)
df2['index'] = df2.index

neighbourhood_id_dict = dict(zip(df2.new_neighbourhood, df2.index))
id_neighbourhood_dict = dict(zip(df2.index, df2.new_neighbourhood))

neighbourhood_group_id_dict = {'Bronx': 0, 'Brooklyn': 1, 'Manhattan': 2, 'Queens': 3, 'Staten Island': 4}
id_neighbourhood_group_dict = {0: 'Bronx', 1: 'Brooklyn', 2: 'Manhattan', 3: 'Queens', 4: 'Staten Island'}

room_type_id_dict = {'Shared Room': 0, 'Private Room': 1, 'Entire Home/Apt': 2, 'Hotel Room': 3}
id_room_type_dict = {0: 'Shared Room', 1: 'Private Room', 2: 'Entire Home/Apt', 3: 'Hotel Room'}

neighbourhood_group_latlong_dict = {0.0: [40.837048,  -73.865433],
                                    1.0: [40.650002, -73.949997],
                                    2.0: [40.776676, -73.971321],
                                    3.0: [40.742054, -73.769417],
                                    4.0: [40.579021, -74.151535]}