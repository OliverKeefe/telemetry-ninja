terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.23.1"
    }
  }
}

provider "docker" {
  host = "npipe:////.//pipe//docker_engine"
}

resource "docker_image" "mysql" {
  name         = "mysql:5.7"
  keep_locally = false
}

resource "docker_container" "mysql" {
  image = docker_image.mysql.latest
  name  = "mysql"
  ports {
    internal = 3306
    external = 3306
  }

  env = [
    "MYSQL_ROOT_PASSWORD=secret",
    "MYSQL_DATABASE=telemetry_ninja",
    "MYSQL_USER=testuser",
    "MYSQL_PASSWORD=testpassword", #TODO: Actually use proper secret management etc... This is just for testing.
  ]
  restart = "always"
}

