# Use the official Python base image with Python 3.11
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install the Flask dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code to the container
COPY . .

# Specify the command to run the Flask app
CMD ["python", "app.py"]
