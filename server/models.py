from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

# Metadata object to customize naming conventions if needed
metadata = MetaData()

# Create the SQLAlchemy database object
db = SQLAlchemy(metadata=metadata)

# Define the Pet model
class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    species = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Pet {self.id}, {self.name}, {self.species}>'
