from flask import request
from flask_restful import Resource

from app.orders.schema import LineItemSchema
from app.orders.services.cart_item import CartItemService
from core.utils import Response


class CartItemController(Resource):
    cart_item_service = CartItemService()

    def get(self, cart_id):
        cart_items = self.cart_item_service.get_all(cart_id)
        cart_schema = LineItemSchema(many=True)
        cart_items = cart_schema.dump(cart_items)

        return Response(
            success=True,
            message="Cart items returned",
            data=cart_items,
            status_code=200,
        )

    def post(self, cart_id):
        cart_item_schema = LineItemSchema()
        cart_item = cart_item_schema.load(request.get_json())
        cart_item = self.cart_item_service.create(cart_id, cart_item)

        return Response(
            success=True, message="Cart item created", data=cart_item, status_code=201
        )


class CartItemDetailController(Resource):
    cart_item_service = CartItemService()

    def get(self, cart_id, cart_item_id):
        cart_item = self.cart_item_service.get(cart_item_id)
        cart_item_schema = LineItemSchema()
        cart_item = cart_item_schema.dump(cart_item)

        return Response(
            success=True, message="Cart item returned", data=cart_item, status_code=200
        )

    def patch(self, cart_id, cart_item_id):
        cart_item_schema = LineItemSchema(partial=True)
        data = cart_item_schema.load(request.get_json())
        self.cart_item_service.update(cart_item_id, data)

        return Response(success=True, message="Cart item updated", status_code=200)

    def delete(self, cart_id, cart_item_id):
        self.cart_item_service.delete(cart_item_id)

        return Response(success=True, message="Cart item deleted", status_code=200)
