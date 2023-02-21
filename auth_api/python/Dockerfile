FROM python:3-alpine

# Add your instructions to dockerize the application
# App must run on port 8000

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port for Flask app
EXPOSE 8000

# Start Flask app
CMD ["python", "api.py"]
