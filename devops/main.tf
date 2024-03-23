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


locals {
  project_root_dir = "${dirname(abspath(path.root))}"
  root_dir = "${abspath(path.root)}"
  templates_dir = "${local.root_dir}/templates"
  kafka_instances = [ for host in linode_instance.kafka-instance.* : {
      ip_address: host.ip_address
      label: host.label
      hostname: host.label
      private_ip: host.private_ip_address
  }]
  zookeeper_instances = [ for host in linode_instance.zookeeper-instance.* : {
      ip_address: host.ip_address
      label: host.label
      hostname: host.label
      private_ip: host.private_ip_address
  }]
}


resource "local_file" "zookeeper_kafka_hostsfile" {
  content = templatefile("${local.templates_dir}/hostsfile.tftpl", {
    kafka_instances=local.kafka_instances,
    zookeeper_instances=local.zookeeper_instances
  })
  filename = "${local.project_root_dir}/host-config.txt"
}