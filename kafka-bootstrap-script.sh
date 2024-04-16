#!/bin/bash

# Public gist available at:
# https://gist.github.com/codingforentrepreneurs/aef0968829883110e24b107f7278255f

# Check if an argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 new_hostname"
    exit 1
fi

# Set the hostname
sudo hostnamectl set-hostname "$1"

# Confirmation message
echo "Hostname has been changed to $1"

# Set the the Zookeeper Instance ID from 
# Check if 'zookeeper' is in the hostname
if [[ "${1,,}" == *"zookeeper"* ]]; then
    # Extract the numerical ID from the hostname, remove leading zeros
    host_id=$(echo "$1" | grep -o '[0-9]*' | sed 's/^0*//')

    # ensure /data/zookeeper/ exists
    sudo mkdir -p /data/zookeeper

    # Write the ID to the Zookeeper myid file
    echo "$host_id" | sudo tee /data/zookeeper/myid

    # Display the contents of the myid file
    cat /data/zookeeper/myid
else
    echo "The new hostname does not contain 'zookeeper', no Zookeeper ID changes made."
fi


# Create user "tars"
sudo useradd -r -s /sbin/nologin tars
sudo usermod -aG sudo tars
echo "tars ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/tars

# Define all required directories
directories=(
    /data/my-config
    /var/log/zookeeper
    /var/log/kafka
    /opt/kafka
    /tmp/zookeeper
    /data/zookeeper
    /data/kafka
)

# Loop through each directory
for dir in "${directories[@]}"; do
    # Create the directory with sudo, avoiding errors if it already exists
    sudo mkdir -p "$dir"
    
    # Change the ownership to 'tars' user and group, recursively
    sudo chown -R tars:tars "$dir"
done

# Install Java and Required packages
sudo apt-get update && sudo apt-get -y install wget ca-certificates zip net-tools vim nano tar netcat openjdk-8-jdk

# Add file limits configs - allow to open 100,000 file descriptors
echo "* hard nofile 100000" | sudo tee --append /etc/security/limits.conf
echo "* soft nofile 100000" | sudo tee --append /etc/security/limits.conf

# update memory swap
sudo sysctl vm.swappiness=1
echo 'vm.swappiness=1' | sudo tee --append /etc/sysctl.conf

# Download Kafka (including Zookeeper) from
# https://kafka.apache.org/downloads
curl https://dlcdn.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz -o kafka.tgz
tar -xvzf kafka.tgz
mv kafka_*/* /opt/kafka/
rm kafka.tgz