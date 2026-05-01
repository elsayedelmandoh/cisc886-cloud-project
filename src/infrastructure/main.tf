# VPC Configuration
resource "aws_vpc" "25xrvl_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support  = true
  tags = {
    Name = "25xrvl-vpc"
  }
}
# Internet Gateway
resource "aws_internet_gateway" "25xrvl_igw" {
  vpc_id = aws_vpc.25xrvl_vpc.id

  tags = {
    Name = "25xrvl-igw"
  }
}
# Public Subnet
resource "aws_subnet" "25xrvl_public" {
  vpc_id                  = aws_vpc.25xrvl_vpc.id
  cidr_block             = "10.0.1.0/24"
  availability_zone      = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "25xrvl-public-1a"
  }
}
# Private Subnet for EMR
resource "aws_subnet" "25xrvl_private" {
  vpc_id                  = aws_vpc.25xrvl_vpc.id
  cidr_block             = "10.0.2.0/24"
  availability_zone      = "us-east-1a"
  map_public_ip_on_launch = false

  tags = {
    Name = "25xrvl-private-1a"
  }
}
# EMR Subnet
resource "aws_subnet" "25xrvl_emr" {
  vpc_id                  = aws_vpc.25xrvl_vpc.id
  cidr_block             = "10.0.3.0/24"
  availability_zone      = "us-east-1a"
  map_public_ip_on_launch = false

  tags = {
    Name = "25xrvl-emr-1a"
  }
}
# Public Route Table
resource "aws_route_table" "25xrvl_public_rt" {
  vpc_id = aws_vpc.25xrvl_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.25xrvl_igw.id
  }

  tags = {
    Name = "25xrvl-public-rt"
  }
}
# Associate Public Subnet with Route Table
resource "aws_route_table_association" "public_assoc" {
  subnet_id       = aws_subnet.25xrvl_public.id
  route_table_id = aws_route_table.25xrvl_public_rt.id
}
# EC2 Security Group
resource "aws_security_group" "25xrvl_ec2_sg" {
  name        = "25xrvl-ec2-sg"
  description = "Security group for EC2 instance"
  vpc_id      = aws_vpc.25xrvl_vpc.id
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 11434
    to_port     = 11434
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  ingress {
    from_port   = 3000
    to_port     = 3000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "25xrvl-ec2-sg"
  }
}
# EMR Security Group
resource "aws_security_group" "25xrvl_emr_sg" {
  name        = "25xrvl-emr-sg"
  description = "Security group for EMR cluster"
  vpc_id      = aws_vpc.25xrvl_vpc.id
  ingress {
    from_port       = 22
    to_port         = 22
    protocol        = "tcp"
    security_groups = [aws_security_group.25xrvl_ec2_sg.id]
  }
  ingress {
    from_port       = 8443
    to_port         = 8443
    protocol        = "tcp"
    security_groups = [aws_security_group.25xrvl_ec2_sg.id]
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "25xrvl-emr-sg"
  }
}
