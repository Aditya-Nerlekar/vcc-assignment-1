from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({
        "service": "User Service",
        "users": ["Alice", "Bob", "Charlie"]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4002)
