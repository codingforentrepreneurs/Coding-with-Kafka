terraform {
  required_providers {
    linode = {
      source  = "linode/linode"
    }
  }
}

provider "linode" {
  token = var.linode_api_token
}

resource "linode_instance" "zookeeper-instance" {
    label = "zookeeper${count.index + 1}" # unique in linode
    count = var.zookeeper_server_count
    image = "linode/ubuntu22.04"
    region = "us-sea"
    type = var.server_type
    authorized_keys = [trimspace(file(var.ssh_public_key_path))]
    private_ip = true

    provisioner "remote-exec" {
        connection {
            host = "${self.ip_address}"
            type = "ssh"
            user = "root"
            private_key = "${file(var.ssh_private_key_path)}"
        }
        inline = [
            "hostnamectl set-hostname zookeeper${count.index + 1}",
        ]
    }

}

resource "linode_instance" "kafka-instance" {
    label = "kafka${count.index + 1}"
    count = var.kafka_server_count
    image = "linode/ubuntu22.04"
    region = "us-sea"
    type = var.server_type
    authorized_keys = [trimspace(file(var.ssh_public_key_path))]
    private_ip = true

    provisioner "remote-exec" {
        connection {
            host = "${self.ip_address}"
            type = "ssh"
            user = "root"
            private_key = "${file(var.ssh_private_key_path)}"
        }
        inline = [
            "hostnamectl set-hostname kafka${count.index + 1}",
        ]
    }
}