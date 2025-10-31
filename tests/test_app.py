from app import create_app
from app.models import db, User


def test_user_creation():
    app = create_app()
    with app.app_context():
        user = User(name="TestUser")
        db.session.add(user)
        db.session.commit()
        fetched = User.query.first()
        assert fetched.name == "TestUser"
