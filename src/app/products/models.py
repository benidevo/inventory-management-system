from core.resources.database import db

labels = db.Table(
    "labels",
    db.Column("label_id", db.Integer, db.ForeignKey("label.id"), primary_key=True),
    db.Column("product_id", db.Integer, db.ForeignKey("product.id"), primary_key=True),
)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    labels = db.relationship(
        "Label",
        secondary=labels,
        lazy="subquery",
        backref=db.backref("products", lazy=True),
    )
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    def __init__(self, name, price, quantity, category_id=None):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category_id = category_id

    def __repr__(self):
        return f"Product {self.name}"

    def in_stock(self):
        return self.quantity > 0

    def update(self, update_dictionary: dict):
        for col_name in self.__table__.columns.keys():
            if col_name in update_dictionary:
                setattr(self, col_name, update_dictionary[col_name])

        self.save()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Label(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Label {self.name}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    products = db.relationship("Product", backref="category", lazy=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    def __init__(self, name):
        self.name = name.upper()

    def __repr__(self):
        return f"{self.name}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
