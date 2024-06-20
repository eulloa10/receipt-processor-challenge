import json

valid_receipt_a = {
    "retailer": "Walgreens",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "08:13",
    "total": "2.65",
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"},
        {"shortDescription": "Dasani", "price": "1.40"}
    ]
}
valid_receipt_b = {
    "retailer": "Target",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "13:13",
    "total": "1.25",
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"}
    ]
}

valid_receipt_c = {
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {
      "shortDescription": "Mountain Dew 12PK",
      "price": "6.49"
    },{
      "shortDescription": "Emils Cheese Pizza",
      "price": "12.25"
    },{
      "shortDescription": "Knorr Creamy Chicken",
      "price": "1.26"
    },{
      "shortDescription": "Doritos Nacho Cheese",
      "price": "3.35"
    },{
      "shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ",
      "price": "12.00"
    }
  ],
  "total": "35.35"
}

valid_receipt_d = {
  "retailer": "M&M Corner Market",
  "purchaseDate": "2022-03-20",
  "purchaseTime": "14:33",
  "items": [
    {
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    },{
      "shortDescription": "Gatorade",
      "price": "2.25"
    }
  ],
  "total": "9.00"
}

invalid_missing_fields = {
    "retailer": "CVS",
    "purchaseDate": "2022-01-02",
    "total": "2.65",
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"},
        {"shortDescription": "Dasani", "price": "1.40"}
    ]
}
invalid_date_format = {
    "retailer": "Ralph's",
    "purchaseDate": "01-02-2022",
    "purchaseTime": "08:13",
    "total": "2.65",
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"},
        {"shortDescription": "Dasani", "price": "1.40"}
    ]
}
invalid_time_format = {
    "retailer": "Whole Foods",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "24:13",
    "total": "1.25",
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"}
    ]
}
invalid_price_amount = {
    "retailer": "Target",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "13:13",
    "total": "1.25",
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "0.00"}
    ]
}

invalid_price_format = {
    "retailer": "Target",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "13:13",
    "total": "1.25",
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.234"}
    ]
}

invalid_empty_items = {
    "retailer": "Super King",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "08:13",
    "total": "2.65",
    "items": []
}
invalid_field_types = {
    "retailer": 12234532,
    "purchaseDate": "2022-01-02",
    "purchaseTime": "08:13",
    "total": "2.65",
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25"},
        {"shortDescription": "Dasani", "price": "1.40"}
    ]
}
invalid_extra_fields = {
    "retailer": "Walgreens",
    "purchaseDate": "2022-01-02",
    "purchaseTime": "08:13",
    "total": "2.65",
    "items": [
        {"shortDescription": "Pepsi - 12-oz", "price": "1.25", "SKU": "12345"},
        {"shortDescription": "Dasani", "price": "1.40"}
    ]
}

# Valid receipt
def test_receipt_a_valid(client):
    response = client.post('/receipts/process', json=valid_receipt_a)
    data = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert 'id' in data

# Valid receipt
def test_receipt_b_valid(client):
    response = client.post('/receipts/process', json=valid_receipt_b)
    data = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert 'id' in data

# Valid receipt
def test_receipt_c_valid(client):
    response = client.post('/receipts/process', json=valid_receipt_c)
    data = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert 'id' in data

# Valid receipt
def test_receipt_d_valid(client):
    response = client.post('/receipts/process', json=valid_receipt_d)
    data = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert 'id' in data

# Invalid receipt - missing fields
def test_receipt_missing_fields(client):
    response = client.post('/receipts/process', json=invalid_missing_fields)
    assert response.status_code == 400

# Invalid receipt - incorrect date format
def test_receipt_invalid_date(client):
    response = client.post('/receipts/process', json=invalid_date_format)
    assert response.status_code == 400

# Invalid receipt - incorrect time format
def test_receipt_invalid_time(client):
    response = client.post('/receipts/process', json=invalid_time_format)
    assert response.status_code == 400

# Invalid receipt - invalid price amount
def test_receipt_invalid_price(client):
    response = client.post('/receipts/process', json=invalid_price_amount)
    assert response.status_code == 400

# Invalid receipt - invalid price format
def test_receipt_invalid_price_format(client):
    response = client.post('/receipts/process', json=invalid_price_format)
    assert response.status_code == 400

# Invalid receipt - empty items
def test_receipt_empty_items(client):
    response = client.post('/receipts/process', json=invalid_empty_items)
    assert response.status_code == 400

# Invalid receipt - invalid field types
def test_receipt_invalid_field_types(client):
    response = client.post('/receipts/process', json=invalid_field_types)
    assert response.status_code == 400

# Invalid receipt - extra fields
def test_receipt_invalid_extra_fields(client):
    response = client.post('/receipts/process', json=invalid_extra_fields)
    assert response.status_code == 400

# Valid receipt - get points
def test_get_receipt_points_valid_id(client):
    receipt_id = '7b5aa609-da53-5dbb-923f-352fcd70a4d5'
    response = client.get(f'/receipts/{receipt_id}/points')
    data = json.loads(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert 'points' in data
    assert data['points'] == 20

# Nonexisting ID
def test_get_receipt_points_nonexistent_id(client):
    receipt_id = '7b5aa610-da54-5dbc-923g-352fcd70a4d9'
    response = client.get(f'/receipts/{receipt_id}/points')
    assert response.status_code == 404
