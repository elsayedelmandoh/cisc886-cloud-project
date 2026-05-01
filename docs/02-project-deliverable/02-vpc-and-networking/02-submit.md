# what to submit

## Section 2 - VPC & Networking (4 marks)

Submit the following in your report:

1. **Terraform code** committed to GitHub (src/infrastructure/main.tf)
   - VPC configuration
   - Subnet definitions
   - Internet Gateway
   - Route tables
   - Security groups

2. **VPC configuration table** showing:
   - VPC name and CIDR block
   - Region
   - DNS settings

3. **Subnet design table** showing:
   - All subnets (public, private, EMR)
   - CIDR blocks for each
   - Availability zones
   - Purpose of each subnet

4. **Internet Gateway configuration** with name and attachment

5. **Route table** showing routes for internal traffic and internet access

6. **Security group rules** showing:
   - EC2 Security Group with inbound rules (SSH, HTTP, HTTPS, Ollama API port 11434, OpenWebUI port 3000)
   - EMR Security Group with rules for internal communication

> Terraform code is REQUIRED for this section. Run the notebook to generate main.tf
