# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY . /app 
RUN pip install -r requirements.txt

# Expose the port your Flask app will run on
EXPOSE 8080

# Set environment variables for Flask
ENV FLASK_APP=system_deck.py  
ENV FLASK_ENV=production  
# Run the Flask application
CMD ["python3", "system_deck.py"]