
#!/usr/bin/env python3
from random import choice as rc
from faker import Faker
from app import app
from models import db, Pet

with app.app_context():

    # Initialize Faker for random names
    fake = Faker()

    # Delete all rows in the "pets" table to prevent duplicates
    Pet.query.delete()

    # Create an empty list for pets
    pets = []

    # Define possible species
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Add sample Pet instances
    pets.append(Pet(name="Fido", species="Dog"))
    pets.append(Pet(name="Whiskers", species="Cat"))
    pets.append(Pet(name="Hermie", species="Hamster"))
    pets.append(Pet(name="Slither", species="Snake"))

    # Optionally, generate 6 more random pets to make a total of 10
    for _ in range(6):
        pets.append(Pet(name=fake.first_name(), species=rc(species)))

    # Insert all pets into the database
    db.session.add_all(pets)
    db.session.commit()

    print(f"Inserted {len(pets)} pets into the database.")
