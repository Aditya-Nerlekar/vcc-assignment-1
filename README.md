# Microservices using Python & VirtualBox

## Architecture
- User Service (VM1)
- Product Service (VM2)
- API Gateway (VM3)
- All VMs connected via Internal Network

## Technologies
- Python
- Flask
- REST APIs
- VirtualBox

## How to Run

### On ALL VMs (once)

```bash
git clone https://github.com/<your-username>/microservices-python-vm.git
cd microservices-python-vm
pip3 install -r requirements.txt
```

### VM-1 (User Service)

```bash
cd user_service
python3 app.py
```

Runs on: `http://<USER_VM_IP>:5001/users`

### VM-2 (Product Service)

```bash
cd product_service
python3 app.py
```

Runs on: `http://<PRODUCT_VM_IP>:5002/products`

### VM-3 (API Gateway)

```bash
cd api_gateway
python3 app.py
```

Runs on: `http://<API_GATEWAY_IP>:5000`

## API Endpoints

- `/users` - Get users from User Service
- `/products` - Get products from Product Service
- `/all` - Get both users and products aggregated

## Testing

From API Gateway VM or Client VM:

```bash
curl http://<API_GATEWAY_IP>:5000/users
curl http://<API_GATEWAY_IP>:5000/products
curl http://<API_GATEWAY_IP>:5000/all
```

## Important Notes

- Replace `<USER_VM_IP>`, `<PRODUCT_VM_IP>`, and `<API_GATEWAY_IP>` with actual VM IPs
- Edit `api_gateway/app.py` to set correct service URLs
- Ensure all VMs are on the same network
# vcc-assignment-1
