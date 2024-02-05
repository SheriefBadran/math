#Use the official Python runtime as a parant image
FROM python:3.8-slim

# Install Node.js, npm, git and clean up the 'apt' cache to reduce the size of the image by removing unnecessary files
# after installation is complete
RUN apt-get update && apt-get install -y nodejs npm git && rm -rf /var/lib/apt/lists/*

# Install nodemon globally
RUN npm install -g nodemon

# Create the vscode user with a specific user ID and group ID 
# -m flag to create /home/vscode if it doesn't exist to avoid permission being set on non-existing folder
# in the next step
RUN groupadd -r vscode && useradd --no-log-init -r -g vscode -m vscode

# Change ownership of the vscode user's home directory
RUN chown -R vscode:vscode /home/vscode

# Set the working directory in the container
WORKDIR /usr/src/app

# Set the ownership of the work directory to the vscode user
RUN chown vscode:vscode /usr/src/app

# Switch to the new user
USER vscode

# Install any needed packages
RUN pip install --no-cache-dir numpy scipy jupyter matplotlib invoke

#Make port 8888 available to the world outside this container
EXPOSE 8888

# Define environment variable
ENV NAME Math

# Start a shell
CMD ["/bin/bash"]