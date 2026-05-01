# section 7: web interface (2 marks)

## openwebui installation

```bash
# Install Docker
sudo apt-get update
sudo apt-get install -y docker.io docker-compose

# Run OpenWebUI
sudo docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart unless-stopped \
  ghcr.io/open-webui/open-webui:main
```

## configure openwebui

1. Access OpenWebUI at: http://<EC2-PUBLIC-IP>:3000
2. Go to Settings > Admin Settings > Connections
3. Set Ollama Base URL: http://host.docker.internal:11434
4. Save settings
5. Select model: 25xrvl-codegpt

## auto-start on reboot

```bash
sudo cat > /etc/systemd/system/openwebui.service << EOF
[Unit]
Description=OpenWebUI
After=network.target

[Service]
Type=simple
User=ubuntu
ExecStart=/usr/bin/docker run -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart unless-stopped ghcr.io/open-webui/open-webui:main

[Install]
WantedBy=multi-user.target
EOF

sudo systemctl enable openwebui
sudo systemctl start openwebui
```

## required screenshots

- [ ] Browser screenshot of OpenWebUI with model name visible
- [ ] Browser screenshot of sample conversation