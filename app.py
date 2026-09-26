from flask import Flask
from models.database import create_tables

app = Flask(__name__)


# Create database tables
create_tables()


@app.route("/")
def home():
    return "Virtual Interview Assistant Backend is Running!"


if __name__ == "__main__":
    app.run(debug=True)