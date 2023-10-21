# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV APP_HOME /app

# Create and set the working directory
WORKDIR $APP_HOME

# Update the package list and install necessary system packages
RUN apt-get update && apt-get install -y \
    cmake \
    g++ \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /app
COPY requirements.txt $APP_HOME/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY main.py $APP_HOME

# Expose the port the application runs on
EXPOSE 5000

# Define the command to run your application
CMD ["flask", "--app", "main", "run", "--host=0.0.0.0"]
