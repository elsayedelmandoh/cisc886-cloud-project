# section 2: vpc & networking (4 marks)

## vpc configuration

| Setting | Value |
|---------|-------|
| VPC Name | 25xrvl-vpc |
| CIDR Block | 10.0.0.0/16 |
| Region | us-east-1 |
| DNS Hostnames | Enabled |

## subnet design

| Subnet | CIDR | Type | Purpose |
|--------|------|------|---------|
| 25xrvl-public-1a | 10.0.1.0/24 | Public | EC2 instance |
| 25xrvl-private-1a | 10.0.2.0/24 | Private | EMR cluster |
| 25xrvl-emr-1a | 10.0.3.0/24 | Private | Data processing |

## security groups

### EC2 Security Group (25xrvl-ec2-sg)

| Port | Protocol | Source | Purpose |
|------|----------|--------|---------|
| 22 | TCP | 0.0.0.0/0 | SSH |
| 80 | TCP | 0.0.0.0/0 | HTTP |
| 443 | TCP | 0.0.0.0/0 | HTTPS |
| 11434 | TCP | 0.0.0.0/0 | Ollama API |
| 3000 | TCP | 0.0.0.0/0 | OpenWebUI |

### EMR Security Group

| Port | Protocol | Source | Purpose |
|------|----------|--------|---------|
| 22 | TCP | 25xrvl-ec2-sg | SSH |
| 8443 | TCP | 25xrvl-ec2-sg | EMR master |