provider "aws" {
  region = "us-east-1"
}

resource "local_file" "ansible_inventory" {
  content = templatefile("${path.module}/inventory.tpl",
    {
      ip = aws_instance.app_server.public_ip
    }
  )

  filename = "../ansible/inventory.ini"
}


# resource "aws_security_group" "devops_sg" {
#   name        = "devops-sg"
#   description = "Allow SSH and app access"

#   ingress {
#     description = "SSH"
#     from_port   = 22
#     to_port     = 22
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   ingress {
#     description = "App"
#     from_port   = 5000
#     to_port     = 5000
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   ingress {
#     description = "Kubernetes NodePort"
#     from_port   = 30000
#     to_port     = 32767
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
# }
# # 