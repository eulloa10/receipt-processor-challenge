import re
from marshmallow import Schema, fields, validate, validates_schema, ValidationError
from datetime import datetime


class ItemSchema(Schema):
    shortDescription = fields.Str(required=True)
    price = fields.Str(required=True)

    @validates_schema
    def validate_short_description(self, data, **kwargs):
        short_description_format = '^[\\w\\s\\-]+$'
        short_description = data.get('shortDescription')
        if not re.match(short_description_format, short_description):
            raise ValidationError('Invalid short description format', field_name='shortDescription')

    @validates_schema
    def validate_price(self, data, **kwargs):
        price_format = '^\\d+\\.\\d{2}$'
        price = data.get('price')
        if float(price) == 0.00 or not re.match(price_format, price):
            raise ValidationError('Price must be greater than 0.00 and in the format XX.XX', field_name='price')

class ReceiptSchema(Schema):
    retailer = fields.Str(required=True)
    purchaseDate = fields.Str(required=True)
    purchaseTime = fields.Str(required=True, validate=validate.Regexp(r'^([01]\d|2[0-3]):?([0-5]\d)$', error="Time format must be in 24-hour format (HH:MM)"))
    items = fields.List(fields.Nested(ItemSchema), required=True)
    total = fields.Str(required=True)

    @validates_schema
    def validate_retailer_name(self, data, **kwargs):
        retailer_name_format="^[\\w\\s\\-&]+$"
        retailer_name = data.get('retailer')
        if not re.match(retailer_name_format, retailer_name):
            raise ValidationError('Invalid retailer name', field_name='retailer')

    @validates_schema
    def validate_date(self, data, **kwargs):
        format="%Y-%m-%d"
        purchase_date = data.get('purchaseDate')
        try:
            datetime.strptime(purchase_date, format)
        except ValueError:
            raise ValidationError('Date must be in YYYY-MM-DD format', field_name='purchaseDate')

    @validates_schema
    def validate_items(self, data, **kwargs):
        if len(data.get('items')) < 1:
            raise ValidationError('Items must be provided', field_name='items')

    @validates_schema
    def validate_total(self, data, **kwargs):
        total_format = '^\\d+\\.\\d{2}$'
        total = data.get('total')
        if float(total) == 0.00 or not re.match(total_format, total):
            raise ValidationError('Total must be greater than 0.00 and in the format XX.XX', field_name='total')
