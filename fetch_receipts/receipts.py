from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from fetch_receipts.schemas import ReceiptSchema
from fetch_receipts.utils.scoring import ReceiptScorer
from fetch_receipts.utils.hash import create_id

bp = Blueprint('receipts', __name__)

receipts = {
    "7b5aa609-da53-5dbb-923f-352fcd70a4d5" : {
        "id": "7b5aa609-da53-5dbb-923f-352fcd70a4d5",
        "retailer": "Vons",
        "purchaseDate": "2024-06-20",
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
        "total": "35.35",
        "points": 20
    }
}

@bp.route("/process", methods=['POST'])
def process_receipt():
    try:
        payload = ReceiptSchema().load(request.json)
    except ValidationError as err:
        return jsonify({
            "error": "The receipt is invalid"
        }), 400

    id = create_id(payload)

    if id in receipts:
        return jsonify({
            "status": "Receipt has already been processed"
        }), 200

    scorer = ReceiptScorer(payload)
    points = scorer.calculate_total_score()

    payload['id'] = id
    payload['points'] = points
    receipts[id] = payload

    return jsonify({
        "id": id
    }), 200

@bp.route("/<id>/points", methods=['GET'])
def get_receipt_points(id):
    try:
        receipt = receipts[id]
    except KeyError as err:
        return jsonify({
            "error": "No receipt found for that id"
        }), 404

    points = receipt.get('points')

    return jsonify({
        "points": points
    }), 200
