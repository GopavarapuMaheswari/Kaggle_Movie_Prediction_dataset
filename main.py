import streamlit as st
import pandas as pd

csv_file = '/home/mahi/Desktop/pythonbasic/Kaggle_Movie_Prediction_dataset/tmdb_5000_credits.csv'
df = pd.read_csv(csv_file)

st.title('Movie/Cast Search (Machine Learning Style)')
search_term = st.text_input('Enter a search term (e.g., avatar):')

if search_term:
    # Search in 'title' and 'character' columns if they exist
    results = pd.DataFrame()
    if 'title' in df.columns:
        results = pd.concat([results, df[df['title'].str.contains(search_term, case=False, na=False)]])
    if 'character' in df.columns:
        results = pd.concat([results, df[df['character'].str.contains(search_term, case=False, na=False)]])
    results = results.drop_duplicates()
    if not results.empty:
        st.write('Search Results:', results)
    else:
        st.write('No results found.')
else:
    st.write('Please enter a search term above.')
