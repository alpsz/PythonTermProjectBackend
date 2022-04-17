from flask import Flask, jsonify

from app import app
from routes.user_bp import user_bp

app.register_blueprint(user_bp, url_prefix='/users')
@app.route('/')
def index():
    return jsonify({
        "msg": "Success"
    })

if __name__ == "__main__":
    app.run()