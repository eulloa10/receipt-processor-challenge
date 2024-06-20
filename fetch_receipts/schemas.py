import re
from marshmallow import Schema, fields, validate, validates_schema, ValidationError
from datetime import datetime


class ItemSchema(Schema):
    shortDescription = fields.Str(required=True)
    price = fields.Str(required=True)

    @validates_schema
    def validate_price(self, data, **kwargs):
        price_format = r'\d+(?:[.]\d{2})?$'
        price = data['price']
        if price == 0 or not re.match(price_format, price):
            raise ValidationError('Price must be greater than 0 and in the format XX.XX', field_name='price')

class ReceiptSchema(Schema):
    retailer = fields.Str(required=True)
    purchaseDate = fields.Str(required=True)
    purchaseTime = fields.Str(required=True, validate=validate.Regexp(r'^\d{2}:\d{2}$', error="Time format must be in 24-hour format (HH:MM)"))
    items = fields.List(fields.Nested(ItemSchema), required=True)
    total = fields.Str(required=True)

    @validates_schema
    def validate_date(self, data, **kwargs):
        format="%Y-%m-%d"
        purchase_date = data['purchaseDate']
        try:
            datetime.strptime(purchase_date, format)
        except ValueError:
            raise ValidationError('Date must be in YYYY-MM-DD format', field_name='purchaseDate')

    @validates_schema
    def validate_items(self, data, **kwargs):
        if len(data['items']) < 1:
            raise ValidationError('Items must be provided', field_name='items')

    @validates_schema
    def validate_total(self, data, **kwargs):
        total_format = r'\d+(?:[.]\d{2})?$'
        total = data['total']
        if total == 0 or not re.match(total_format, total):
            raise ValidationError('Total must be greater than 0 and in the format XX.XX', field_name='total')
