# Kaggle_Movie_Prediction_dataset

## Quickstart: Movie Filter App

### 1. Install dependencies (in a virtual environment recommended)
```sh
pip install streamlit pandas
```

### 2. Run the Streamlit app
```sh
streamlit run main.py
```

### 3. Build and run with Docker
```sh
docker build -t streamlit-movie-app .
docker run -p 8501:8501 streamlit-movie-app
```

### 4. Usage
- Open your browser at http://localhost:8501
- Enter a search term (e.g., `avatar`) in the input box to filter movies or cast by name.

---