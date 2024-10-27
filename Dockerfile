# Use the official Ubuntu 18.04 as the base image
FROM ubuntu:18.04

# Set environment variables to prevent prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive

# Update the package list and install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file from your host to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application files to the container
COPY . .

# Expose the port that the application will run on
EXPOSE 5000

# Command to run the application
CMD ["python3", "app.py"]
