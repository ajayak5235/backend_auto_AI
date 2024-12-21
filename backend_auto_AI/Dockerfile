# # Use a stable Python image
# FROM python:3.7-slim-buster

# # Set the working directory
# WORKDIR /app

# # Ensure the pip version is updated
# RUN pip install --upgrade pip

# # Copy the requirements file and install dependencies
# COPY requirements.txt ./
# RUN pip install -r requirements.txt

# # Copy the application code
# COPY . .

# # Expose the desired port
# EXPOSE 4000

# # Set environment variables for Flask
# ENV FLASK_APP=app.py
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV FLASK_RUN_PORT=4000

# # Run the Flask application
# CMD ["flask", "run"]




# Autonomous Code Review Agent System

## Project Structure

### Root Directory (code-review-agent/)

#### Dockerfile
# dockerfile
# Base image

FROM python:3.8-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy application files
COPY . /app/

# Expose ports
EXPOSE 8000

# Command to run FastAPI
CMD ["uvicorn", "app.main:app", "--reload","--host", "0.0.0.0", "--port", "8000"]
