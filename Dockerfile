# Use the official Python image
FROM python:3.8 

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the app will run
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]

