try:
    import streamlit as st
    import pandas as pd
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import LabelEncoder
    from sklearn.model_selection import train_test_split
    import joblib
    import os
except ImportError as e:
    import sys
    sys.exit(f"Required module missing: {e}. Please install all dependencies using 'pip install streamlit pandas scikit-learn joblib'.")

csv_path = os.path.join(os.path.dirname(__file__), 'tmdb_5000_credits.csv')

if not os.path.exists(csv_path):
    st.error(f"CSV file not found: {csv_path}. Please make sure 'tmdb_5000_credits.csv' is in the same directory as this script.")
    st.stop()

# Load your dataset

df = pd.read_csv(csv_path)

# Debugging: Show CSV column names
st.write('CSV Columns:', df.columns.tolist())

# Check for required columns
required_columns = ['genres', 'director', 'budget', 'title']
missing_columns = [col for col in required_columns if col not in df.columns]
if missing_columns:
    st.error(f"Missing columns in CSV: {missing_columns}. Please use a CSV file with these columns or update the code to match your CSV structure.")
    st.stop()

# Example: Use 'genres', 'director', 'budget' as features, 'title' as target
# Preprocess features
df['genres'] = df['genres'].astype(str)
df['director'] = df['director'].astype(str)

le_genres = LabelEncoder()
le_director = LabelEncoder()
le_title = LabelEncoder()

df['genres_enc'] = le_genres.fit_transform(df['genres'])
df['director_enc'] = le_director.fit_transform(df['director'])
df['title_enc'] = le_title.fit_transform(df['title'])

X = df[['genres_enc', 'director_enc', 'budget']]
y = df['title_enc']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save encoders and model for reuse
joblib.dump(model, 'movie_model.pkl')
joblib.dump(le_genres, 'le_genres.pkl')
joblib.dump(le_director, 'le_director.pkl')
joblib.dump(le_title, 'le_title.pkl')

# Streamlit UI
st.title("Movie Name Predictor")

genres_input = st.text_input("Genres (as string, e.g., Action)")
director_input = st.text_input("Director")
budget_input = st.number_input("Budget", min_value=0)

if st.button("Predict Movie Name"):
    # Load model and encoders
    model = joblib.load('movie_model.pkl')
    le_genres = joblib.load('le_genres.pkl')
    le_director = joblib.load('le_director.pkl')
    le_title = joblib.load('le_title.pkl')
    
    # Encode inputs
    genres_enc = le_genres.transform([genres_input])[0] if genres_input in le_genres.classes_ else 0
    director_enc = le_director.transform([director_input])[0] if director_input in le_director.classes_ else 0
    
    X_pred = [[genres_enc, director_enc, budget_input]]
    pred_enc = model.predict(X_pred)[0]
    movie_name = le_title.inverse_transform([pred_enc])[0]
    
    st.success(f"Predicted Movie Name: {movie_name}")