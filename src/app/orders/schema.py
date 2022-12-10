from marshmallow import fields

from core.utils import CamelCaseSchema


class CartSchema(CamelCaseSchema):
    id = fields.Integer()
    user_id = fields.Integer()
    line_items = fields.Nested("LineItemSchema", many=True)
    is_paid = fields.Boolean()
    quantity = fields.Integer()
    total_amount = fields.Integer()
    state = fields.String()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

    class Meta:
        ordered = True


class LineItemSchema(CamelCaseSchema):
    id = fields.Integer(dump_only=True)
    cart_id = fields.Integer(dump_only=True)
    product_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        ordered = True
