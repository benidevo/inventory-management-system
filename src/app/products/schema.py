from marshmallow import Schema, fields

from core.utils import CamelCaseSchema


class CreateProductSchema(Schema):
    name = fields.String(required=True)
    price = fields.Integer(required=True)
    quantity = fields.Integer(required=True)
    labels = fields.List(fields.String())
    category = fields.String()


# class CreateProductSchema(Schema):
#     name = fields.String(required=True)
#     price = fields.Integer(required=True)
#     quantity = fields.Integer(required=True)
#     labels = fields.List(fields.String())
#     category = fields.String()


class ListSchema(CamelCaseSchema):
    id = fields.Integer()
    name = fields.String()


class CategorySchema(ListSchema):
    pass


class LabelSchema(ListSchema):
    pass


class ProductSchema(CamelCaseSchema):
    id = fields.Integer()
    name = fields.String()
    price = fields.Integer()
    quantity = fields.Integer()
    category = fields.Nested(CategorySchema)
    labels = fields.List(fields.Nested(LabelSchema))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

    class Meta:
        ordered = True
