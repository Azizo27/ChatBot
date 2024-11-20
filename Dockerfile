# Use an official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download necessary NLTK data
RUN python -m nltk.downloader wordnet

# Copy the Python script
COPY main.py .

# Command to run the script
CMD ["python", "main.py"]
