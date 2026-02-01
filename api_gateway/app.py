from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Service URLs
USER_SERVICE_URL = "http://localhost:4002"
PRODUCT_SERVICE_URL = "http://localhost:4001"

@app.route("/users", methods=["GET"])
def forward_users():
    """Forward to User Service"""
    try:
        response = requests.get(f"{USER_SERVICE_URL}/users")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/products", methods=["GET"])
def forward_products():
    """Forward to Product Service"""
    try:
        response = requests.get(f"{PRODUCT_SERVICE_URL}/products")
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/all", methods=["GET"])
def forward_all():
    """Forward and aggregate from both services"""
    try:
        users = requests.get(f"{USER_SERVICE_URL}/users").json()
        products = requests.get(f"{PRODUCT_SERVICE_URL}/products").json()
        return jsonify({
            "users": users,
            "products": products
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
