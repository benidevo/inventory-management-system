from core.resources.database import db


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    line_items = db.relationship("LineItem", backref="cart", lazy=True)
    quantity = db.Column(db.Integer, nullable=False, default=0)
    total_amount = db.Column(db.Integer, nullable=False, default=0)
    state = db.Column(db.Enum("DRAFT", "COMPLETED", name="cart_state"), default="DRAFT")
    is_paid = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return f"Cart {self.id}"

    def get_total_amount(self):
        self.total_amount = sum(
            [line_item.get_total_amount() for line_item in self.line_items]
        )
        self.quantity = self.get_quantity()
        return self

    def get_quantity(self):
        return sum([line_item.quantity for line_item in self.line_items])

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


class LineItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey("cart.id"))
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"))
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(
        db.DateTime, server_default=db.func.now(), onupdate=db.func.now()
    )

    def __init__(self, cart_id, product_id, quantity):
        self.cart_id = cart_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return f"LineItem {self.id}"

    def get_total_amount(self):
        return self.products.price * self.quantity

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
