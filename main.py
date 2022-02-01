from config import PORT, HOST, DEBUG
from __init__ import app
from utils.ma import ma
from utils.db import db

if __name__ == "__main__":
    db.init_app(app)
    ma.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host=HOST, port=PORT, debug=bool(DEBUG))
