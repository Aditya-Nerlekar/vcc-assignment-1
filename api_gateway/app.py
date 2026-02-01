from flask import Flask, jsonify
import requests

app = Flask(__name__)

# Replace with actual VM IPs
USER_SERVICE_URL = "http://192.168.100.10:4002"
PRODUCT_SERVICE_URL = "http://192.168.100.11:4001"

@app.route("/health", methods=["GET"])
def health():
    """
    Health check endpoint for API Gateway
    """
    return jsonify({
        "status": "UP",
        "service": "API Gateway",
        "port": 3000
    }), 200

@app.route("/users", methods=["GET"])
def forward_users():
    response = requests.get(f"{USER_SERVICE_URL}/users")
    return jsonify(response.json())

@app.route("/products", methods=["GET"])
def forward_products():
    response = requests.get(f"{PRODUCT_SERVICE_URL}/products")
    return jsonify(response.json())

@app.route("/all", methods=["GET"])
def forward_all():
    users = requests.get(f"{USER_SERVICE_URL}/users").json()
    products = requests.get(f"{PRODUCT_SERVICE_URL}/products").json()
    return jsonify({
        "users": users,
        "products": products
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
