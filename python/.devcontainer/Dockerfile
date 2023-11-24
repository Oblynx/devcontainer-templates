# Define the default Python version
ARG PYTHON_VERSION=3
FROM mcr.microsoft.com/devcontainers/python:${PYTHON_VERSION}

# Install additional OS packages
RUN apt-get -y update && \
    apt-get -y install --no-install-recommends gnupg software-properties-common \
        vim git

# Install python package manager
RUN pip install poetry setuptools

# How to add a new user if necessary: https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user#_creating-a-nonroot-user
# Ensure that vscode is the UID 1000
RUN groupmod --gid 1000 vscode \
    && usermod --uid 1000 --gid 1000 vscode \
    && chown -R 1000:1000 /home/vscode
