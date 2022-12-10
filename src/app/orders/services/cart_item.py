from app.orders.models import LineItem as CartItem
from core.error_handlers import AppError


class CartItemService:
    model = CartItem

    def get_all(self, cart_id):
        carts = self.model.query.filter_by(cart_id=cart_id).all()
        return carts

    def create(self, cart_id, cart_item_data):
        cart_item_data.update({"cart_id": cart_id})
        cart_item = self.model(**cart_item_data)
        cart_item.save()

    def update(self, cart_item_id, cart_item_data):
        cart_item = self.get(cart_item_id)
        print("cart_item_data", cart_item_data)
        cart_item.update(cart_item_data)

        return cart_item

    def get(self, cart_item_id):
        cart_item = self.model.query.filter_by(id=cart_item_id).first()
        if not cart_item:
            raise AppError(404, "Cart item not found")

        return cart_item

    def delete(self, cart_item_id):
        cart_item = self.get(cart_item_id)
        cart_item.delete()
