from app.orders.services.cart import CartService
from core.error_handlers import AppError


class PaymentService:
    cart_service = CartService()

    def process_payment(self, cart_id):
        data = {"state": "COMPLETED", "is_paid": True}
        try:
            self.cart_service.update(cart_id, data)
        except Exception as e:
            raise AppError(500, "Payment failed")
