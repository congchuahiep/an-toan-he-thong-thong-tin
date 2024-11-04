from app import db, app

# Định nghĩa mô hình người dùng
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()