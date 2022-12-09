from app.products.models import Category, Label, Product
from core.error_handlers import AppError
from core.utils import replace_space_with_dash


class ProductService:
    model = Product

    def create(self, data):
        prod_labels = data.pop("labels", None)
        prod_category = data.pop("category", None)
        if prod_category:
            category = Category.query.filter_by(name=prod_category.upper()).first()
            if not category:
                category = Category(name=prod_category)
                category.save()
            data.update({"category_id": category.id})

        product = Product(**data)
        product.save()

        if prod_labels:
            labels_list = []
            for prod_label in prod_labels:
                formatted_label = replace_space_with_dash(prod_label)
                label = Label.query.filter_by(name=formatted_label).first()
                if not label:
                    label = Label(name=formatted_label).save()
                labels_list.append(label)
            product.labels = labels_list
            product.save()

    def get_all(self):
        return Product.query.all()

    def get(self, product_id):
        product = Product.query.filter_by(id=product_id).first()
        if not product:
            raise AppError(404, "Product not found")

        return product

    def update(self, product_id, data):
        product = self.get(product_id)

        prod_category = data.pop("category", None)
        if prod_category:
            category = Category.query.filter_by(name=prod_category.upper()).first()
            if not category:
                category = Category(name=prod_category)
                category.save()
            data.update({"category_id": category.id})
        product.update(data)

        prod_labels = data.pop("labels", None)
        if prod_labels:
            labels_list = []
            for prod_label in prod_labels:
                formatted_label = replace_space_with_dash(prod_label)
                label = Label.query.filter_by(name=formatted_label).first()
                if not label:
                    label = Label(name=formatted_label).save()
                labels_list.append(label)
            product.labels.extend(labels_list)

    def delete(self, product_id):
        product = self.get(product_id)
        product.delete()
