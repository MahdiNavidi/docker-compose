# Use a lightweight Python base image
FROM docker.arvancloud.ir/python:3.9-alpine

# Set working directory
WORKDIR /app

# Copy the Python script
COPY check_ip.py .

# Install required packages
# RUN pip install requests

# Run the script
CMD ["python", "check_ip.py"]