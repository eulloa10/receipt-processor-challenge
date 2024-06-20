import uuid

def create_id(payload):
    retailer = payload.get('retailer')
    purchase_date = payload.get('purchaseDate')
    purchase_time = payload.get('purchaseTime')
    items_count = len(payload.get('items'))
    total = payload.get('total')

    all_receipt_info = f"{retailer}-{purchase_date}-{purchase_time}-{items_count}-{total}"
    namespace = uuid.NAMESPACE_DNS
    id = uuid.uuid5(namespace, all_receipt_info)
    id_str = str(id)
    return id_str
