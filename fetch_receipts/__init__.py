from flask import Flask
from fetch_receipts import receipts

def create_app():
    app = Flask(__name__)
    app.register_blueprint(receipts.bp, url_prefix='/receipts')

    return app
