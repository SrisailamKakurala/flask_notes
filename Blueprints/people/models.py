from Blueprints.app import db

class Person(db.Model):
    __tablename__ = 'people'
    
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.String(100))
    
    def __repr__(self):
        return f"<PERSON: {self.name}, AGE: {self.age}>"
    
    def get_id(self):
        return self.pid