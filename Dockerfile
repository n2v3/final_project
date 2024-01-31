# Use the official Python image as the base image
FROM python:3.12

# Set the working directory to /app
WORKDIR /app

# Copy the entire project into the container
COPY . /app

# Install Python dependencies
RUN pip install -r requirements.txt


# Expose port 8000
EXPOSE 8000

# Run the app
CMD python manage.py runserver 0.0.0.0:8000
