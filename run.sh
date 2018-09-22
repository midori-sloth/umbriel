#!/usr/bin/env bash

# Build the container
clear
echo "Building umbriel microservice"
(docker-compose build && \
clear && \
# Run the container
echo "Running umbriel microservice" && \
docker-compose up -d --force-recreate --remove-orphans && \
clear && \
# Display results
docker-compose ps) || \
"Unable to run umbriel service"
