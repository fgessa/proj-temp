from api.db import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(100), unique=True)
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(50))

    @classmethod
    def find_by_name(cls, name: str) -> "User":
        return User.query.filter_by(name=name).first()
    
    @classmethod
    def find_by_public_id(cls, public_id:str) -> "User":
        return User.query.filter_by(public_id=public_id).first()