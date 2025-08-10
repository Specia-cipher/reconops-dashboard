# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies needed for some Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Ensure the database is initialized before starting the app (if needed)
# This is a placeholder command, you might need to adjust it
# CMD ["python", "manage.py", "db", "upgrade"]

# Expose the port on which the Flask app will run
EXPOSE 5000

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Run the Flask application
# Use a production-ready WSGI server like Gunicorn instead of the Flask dev server
# You'll need to add gunicorn to your requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
