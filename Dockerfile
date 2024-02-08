# Use the official Python image as the base image
FROM python:3.12

# Set the working directory to /app
WORKDIR /app

# Copy the entire project into the container
#COPY . /app

COPY requirements.txt /app

# Install Python dependencies
RUN pip install -r requirements.txt

VOLUME ["/app"]

# Install psql
RUN apt-get update && apt-get install -y postgresql-client

# Expose port 8000
EXPOSE 8000

# Run the app
CMD python manage.py runserver 0.0.0.0:8001
