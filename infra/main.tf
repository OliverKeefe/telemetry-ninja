terraform {
    required_providers {
        docker = {
            source = "kreuzwerker/docker"
            version = "2.23.1"
        }
    }
}

provider "docker" {
    # host = "unix:///var/run/docker.sock"
    host = "tcp://localhost:2375"
}

# Create docker MySql container

resource "docker_image" "mysql" {
    name = "mysql:latest"
}

resource "docker_container" "dbserver" {
    image = docker_image.mysql.latest
    name = "dbserver"
    must_run = true
    publish_all_ports = true
    #command = ["--default-authentication-plugin=mysql_native_password"]
}