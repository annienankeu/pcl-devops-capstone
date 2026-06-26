resource "aws_instance" "app_server" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t2.medium"
  subnet_id     = aws_subnet.public_subnet.id

  vpc_security_group_ids = [aws_security_group.app_sg.id]

  key_name = var.key_name

  root_block_device {
    volume_size = 30
    volume_type = "gp3"
  }

  tags = {
    Name = "capstone-app-server"
  }
}