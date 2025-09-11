# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and source code
COPY main.py ./
COPY tmdb_5000_credits.csv ./

# Install dependencies
RUN pip install --no-cache-dir streamlit pandas

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0"]