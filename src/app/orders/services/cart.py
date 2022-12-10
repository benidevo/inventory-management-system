from app.orders.models import Cart


class CartService:
    model = Cart

    def get_all(self):
        carts = self.model.query.all()

        return carts

    def create(self, user_id):
        cart = self.model(user_id)
        cart.save()

        return cart

    def get(self, cart_id):
        return self.model.query.get(cart_id)

    def update(self, cart_id, cart_data):
        cart = self.get(cart_id)
        cart.update(cart_data)

        return cart
