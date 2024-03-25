#!/bin/bash

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


# Set the Zookeeper Instance ID
# uncomment during manual use
# sudo nano /data/zookeeper/myid

# Extract the Zookeeper Instance ID from 
# the hostname
hostname=$(hostname)
host_id=$(echo $hostname | grep -o '[0-9]*' | sed 's/^0*//')
echo "$host_id" | sudo tee /data/zookeeper/myid
cat /data/zookeeper/myid


# Install Java and Required packages
sudo apt-get update && sudo apt-get -y install wget ca-certificates zip net-tools vim nano tar netcat openjdk-8-jdk
# Verifying versions
java -version

# update memory swap
# to leverage as little SSD as possible
sudo sysctl vm.swappiness=1
echo 'vm.swappiness=1' | sudo tee --append /etc/sysctl.conf

# Copy contents of the terraform hostsfile and append to /etc/hosts
# nano /etc/hosts
cat /etc/hosts


# Download Kafka (including Zookeeper) from
# https://kafka.apache.org/downloads
curl https://dlcdn.apache.org/kafka/3.7.0/kafka_2.13-3.7.0.tgz -o kafka.tgz
tar -xvzf kafka.tgz
mv kafka_*/* /opt/kafka/
rm kafka.tgz

ls /opt/kafka/bin | grep "zookeeper"



# verify:
cat /opt/kafka/config/zookeeper.properties

# Run
# /opt/kafka/bin/zookeeper-server-start.sh /opt/kafka/config/zookeeper.properties
# /opt/kafka/bin/zookeeper-server-start.sh /data/my-config/zookeeper.properties

# In new terminal, enter the shell
# /opt/kafka/bin/zookeeper-shell.sh localhost:2181