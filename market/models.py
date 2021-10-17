from market import db

class Item(db.Model):
    name= db.Column(db.String(length=30),unique=True,nullable=False)
    barcode= db.Column(db.String(length=12),unique=True,nullable=False)
    price= db.Column(db.Integer,nullable=False)
    id= db.Column(db.Integer,primary_key=True)
    description= db.Column(db.String(length=1024), nullable=False,unique=True)

    def __repr__(self):
        return f'Item {self.name}'