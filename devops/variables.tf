variable "linode_api_token" {
  sensitive = true
}

variable "server_type" {
    default = "g6-standard-2"
    type = string
}

variable "zookeeper_server_count" {
    default = 1
    type = number
}

variable "kafka_server_count" {
    default = 1
    type = number
}

variable "ssh_public_key_path" {
    description = "SSH public key path to use for Linode instances"
    default     = "~/.ssh/id_rsa.pub"
    type        = string
    sensitive   = false
}

variable "ssh_private_key_path" {
    description = "Path to the SSH public key"
    default = "~/.ssh/id_rsa"
    sensitive   = true
}