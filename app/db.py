from app import db

class Menu(db.Model):
    __tablename__ = "Menus"
    ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"('{self.ID}','{self.Name}')"

class Dishes(db.Model):
    __tablename__ = "Menus_items"

    ID = db.Column(db.Integer, primary_key=True)
    DishName = db.Column(db.String, nullable=False)
    Menu = db.Column(db.Integer, nullable=False)
    Date = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"('{self.ID}','{self.DishName}','{self.DishName}','{self.Date}')"


