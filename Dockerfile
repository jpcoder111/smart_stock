# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Create the log directory and files
RUN mkdir -p /app/logs/http_requests && \
    touch /app/logs/http_requests/requests.log && \
    touch /app/logs/http_requests/responses.log

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["gunicorn", "-c", "gunicorn_config.py", "main.wsgi:application"]
