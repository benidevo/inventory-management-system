from flask import request
from flask_restful import Resource

from app.products.schema import CreateProductSchema, ProductSchema
from app.products.services.product import ProductService
from core.utils import Response


class ProductController(Resource):
    product_service = ProductService()

    def get(self):
        products = self.product_service.get_all()
        product_schema = ProductSchema(many=True)
        products = product_schema.dump(products)
        return Response(
            success=True,
            message="Product created successfully",
            status_code=201,
            data=products,
        )

    def post(self):
        request_schema = CreateProductSchema()
        data = request_schema.load(request.json)
        self.product_service.create(data)

        return Response(
            success=True, message="Product created successfully", status_code=201
        )


class ProductDetailController(Resource):
    product_service = ProductService()

    def get(self, product_id):
        product = self.product_service.get(product_id)
        product = ProductSchema().dump(product)

        return Response(
            success=True,
            message="Product retrieved successfully",
            data=product,
            status_code=200,
        )

    def patch(self, product_id):
        request_schema = CreateProductSchema(partial=True)
        data = request_schema.load(request.json)
        self.product_service.update(product_id, data)

        return Response(
            success=True, message="Product updated successfully", status_code=200
        )

    def delete(self, product_id):
        self.product_service.delete(product_id)

        return Response(
            success=True, message="Product deleted successfully", status_code=200
        )
