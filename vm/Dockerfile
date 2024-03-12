# Use Debian Bullseye Slim as the base image
FROM debian:bullseye-slim

# Update package lists and install nano
RUN apt-get update && \
    apt-get install -y nano netcat-traditional nmap bash && \
    rm -rf /var/lib/apt/lists/*

# Set bash as the default shell
SHELL ["/bin/bash", "-c"]

# Set an entry point that runs indefinitely
ENTRYPOINT ["tail", "-f", "/dev/null"]