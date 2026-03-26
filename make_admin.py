from app import create_app
from app.models import User
from app.extensions import db

app = create_app()

with app.app_context():
    email = input("Enter user email to make admin: ").strip()
    user = User.query.filter_by(email=email).first()

    if user:
        user.role = "admin"
        db.session.commit()
        print(f"{user.email} is now an admin.")
    else:
        print("User not found.")