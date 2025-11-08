# server/app.py

from flask import Flask
from flask_migrate import Migrate
from models import db

# Create a Flask application instance
app = Flask(__name__)

# Configure the database connection to the local file app.db
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Configure flag to disable modification tracking (saves memory)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Create a Migrate object to manage schema modifications
migrate = Migrate(app, db)

if __name__ == '__main__':
    # Run the app on port 5555 in debug mode
    app.run(port=5555, debug=True)
