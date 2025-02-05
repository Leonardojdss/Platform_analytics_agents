# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && \
    apt-get install -y curl apt-transport-https build-essential unixodbc-dev

# Add Microsoft package signing key
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

# Add Microsoft SQL Server repository
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Update package lists and install msodbcsql18
RUN apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Copy the .env file into the container
COPY .env /app/.env

# Expose the port Streamlit will run on
EXPOSE 8501

# Run the application
CMD ["streamlit", "run", "src/app/main.py"]
