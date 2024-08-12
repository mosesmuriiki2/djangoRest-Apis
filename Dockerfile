# Use the official Python 3.10 Alpine image as the base
FROM --platform=$BUILDPLATFORM python:3.10-alpine AS builder

# Set the working directory in the container
WORKDIR /app

# Expose port 8000 for the Django application
EXPOSE 8000

# Install system dependencies
RUN apk update && apk add --no-cache \
    pkgconfig \
    gcc \
    musl-dev \
    bash \
    mariadb-dev 

# Copy the requirements file to the container
COPY requirements.txt /app/

# Install Python packages from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Set the entry point and default command to run the Django server
ENTRYPOINT ["python3"]

CMD ["manage.py", "runserver", "0.0.0.0:8000"]
