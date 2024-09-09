# Start coding here! Use as many cells as you like
import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv(r"C:\Users\Hardy\OneDrive\Desktop\Datasets\netflix_data.csv")
#print(netflix_df)

start_year = 1990
end_year = 1999
filtered_df = netflix_df[(netflix_df['release_year'] >= start_year) & (netflix_df['release_year'] <= end_year)]
duration_counter = filtered_df[['duration']].mode()
#duration = 94
#print(duration_counter)

genre = 'action'
short_movie_count_counter = filtered_df[(filtered_df['duration'] < 90) & 
                                        (filtered_df['type'] == 'Movie') & 
                                        (filtered_df['genre'].str.contains(genre, case=False, na=False))] #.count()
#print(short_movie_count_counter)
#short_movie_count = 7

# EVANGELION?!
eva = filtered_df[filtered_df['show_id'] == 's2039']
#print(eva)
