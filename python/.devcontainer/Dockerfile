# Define the default Python version
ARG PYTHON_VERSION=3
FROM mcr.microsoft.com/devcontainers/python:${PYTHON_VERSION}

# Install additional OS packages
RUN apt-get -y update && \
    apt-get -y install --no-install-recommends gnupg software-properties-common \
        vim git

# Install Terraform only if needed
#RUN wget -O- https://apt.releases.hashicorp.com/gpg | \
#        gpg --dearmor > "/usr/share/keyrings/hashicorp-archive-keyring.gpg" ; \
#    echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" >> "/etc/apt/sources.list.d/hashicorp.list" && \
#    apt-get -y update && apt-get install terraform

# Install python package manager
RUN pip install poetry setuptools
