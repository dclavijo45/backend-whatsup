from config import SECRET_KEY, MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from routes.verify_number import verify_number_v1
from routes.register import register_v1
from routes.login import login_v1
from flask import Flask, jsonify
from flask_cors import CORS

# Settings for App
app = Flask(__name__, static_url_path='')
app.secret_key = SECRET_KEY

# Settings for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Settings for CORS
CORS(
    app,
    resources={
        r"/*": {
            "origins": "*",
            "methods": ["OPTIONS", "GET", "POST", "PUT", "DELETE"],
            "allow_headers": ["Authorization", "Content-Type"],
        }
    },
)

# Catch http errors
@app.errorhandler(404)
def notFound(e):
    return jsonify({"message": "Not found"}), 404

# Routes
app.add_url_rule(login_v1["login"], view_func=login_v1["login_controller"])
app.add_url_rule(register_v1["register"], view_func=register_v1["register_controller"])
app.add_url_rule(verify_number_v1["verify_number"], view_func=verify_number_v1["verify_number_controller"])