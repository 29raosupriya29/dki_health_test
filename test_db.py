from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import unittest

# Define the database connection
DATABASE_URL = "sqlite:///example.db"
engine = create_engine(DATABASE_URL, echo=True)

# Define the data model
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50))
    email = Column(String(50))

# Create tables in the database
Base.metadata.create_all(engine)

# Sample data for testing
sample_user_data = {'username': 'testuser', 'email': 'testuser@example.com'}

# Define database test cases
class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        # Create a session to interact with the database
        Session = sessionmaker(bind=engine)
        self.session = Session()


    def test_add_user(self):
        # Positive scenario: Add a user to the database
        new_user = User(**sample_user_data)
        self.session.add(new_user)
        self.session.commit()

        # Verify that the user has been added successfully
        retrieved_user = self.session.query(User).filter_by(username='testuser').first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, 'testuser@example.com')


    def test_retrieve_user(self):
        # Positive scenario: Retrieve a user from the database
        new_user = User(**sample_user_data)
        self.session.add(new_user)
        self.session.commit()

        # Retrieve the user and verify the data
        retrieved_user = self.session.query(User).filter_by(username='testuser').first()
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.email, 'testuser@example.com')

    def test_modify_user(self):
        # Positive scenario: Modify the email of an existing user
        new_user = User(**sample_user_data)
        self.session.add(new_user)
        self.session.commit()

        # Modify the user's email
        modified_user = self.session.query(User).filter_by(username='testuser').first()
        modified_user.email = 'modified@example.com'
        self.session.commit()

        # Retrieve the modified user and verify the updated email
        retrieved_user = self.session.query(User).filter_by(username='testuser').first()
        self.assertEqual(retrieved_user.email, 'modified@example.com')

# Run the tests
if __name__ == '__main__':
    unittest.main()
