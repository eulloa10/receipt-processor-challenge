from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from fetch_receipts.schemas import ReceiptSchema
from fetch_receipts.utils.scoring import ReceiptScorer
from fetch_receipts.utils.hash import create_id

bp = Blueprint('receipts', __name__)

receipts = {}

@bp.route("/process", methods=['POST'])
def process_receipt():
    try:
        payload = ReceiptSchema().load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    scorer = ReceiptScorer(payload)
    points = scorer.calculate_total_score()

    id = create_id(payload)
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
            "error": f"Receipt with id '{id}' not found"
        }), 404

    points = receipt.get('points')

    return jsonify({
        "points": points
    }), 200
