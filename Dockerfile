# Pull the base image.
FROM python

# Set the working directory.
WORKDIR /src

# Update Linux packages.
RUN apt-get --yes update

# Update pip.
RUN pip install --upgrade pip

# Clone stakeholders from GitHub into the working directory.
# (Use the HTTPS URL to avoid the need for SSH keys.)
RUN git clone https://github.com/critical-path/stakeholders.git .

# Install stakeholders.
RUN pip install .
RUN chmod +x ./start-api-and-app.sh

# Run stakeholders.  
EXPOSE 8080
ENTRYPOINT ["./start-api-and-app.sh"]
