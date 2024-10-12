# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any required packages (in case you add dependencies later)
RUN pip install --no-cache-dir -r requirements.txt || true

# Run the cpu_stress.py script
CMD ["python", "cpu_stress.py"]
