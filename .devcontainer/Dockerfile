#Use the official Python runtime as a parant image
FROM python:3.8-slim

# Define environment variable
ENV NAME Math

# Install Node.js, npm, git and clean up the 'apt' cache to reduce the size of the image by removing unnecessary files
# after installation is complete
RUN apt-get update && apt-get install -y nodejs npm git && rm -rf /var/lib/apt/lists/*

# Install any needed packages
RUN pip install --no-cache-dir numpy scipy sympy jupyter matplotlib invoke

# Install nodemon globally
RUN npm install -g nodemon

# Create the vscode user with a specific user ID and group ID 
# -m flag to create /home/vscode if it doesn't exist to avoid permission being set on non-existing folder
# in the next step
RUN groupadd -r vscode && useradd --no-log-init -r -g vscode -m vscode

# Change ownership of the vscode user's home directory
# RUN chown -R vscode:vscode /home/vscode

# Set the working directory in the container
WORKDIR /usr/src/app

# Set the ownership of the work directory to the vscode user
RUN chown vscode:vscode /usr/src/app

# Change owner from root to vscode on vscode directory and all it's content
# This should be done as late as possible for devcontainer run all mounts
# vscode must be able to write to the .gitconfig
# |---------- Move responsibility for mounts to this file later ---------------|
RUN chown -R vscode:vscode /home/vscode

# If .ssh doesn't already exist from devcontainer mounts, create the directory and change owner
# to vscode for everything in it.
# vscode must be able to read from .ssh directory files for git operations
RUN mkdir /home/vscode/.ssh && chown -R vscode:vscode /home/vscode/.ssh

# Switch to the new user
USER vscode

#Make port 8888 available to the world outside this container in case running jupyter on a local host
EXPOSE 8888

# Start a shell
CMD ["/bin/bash"]