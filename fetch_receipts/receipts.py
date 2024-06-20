from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from fetch_receipts.schemas import ReceiptSchema
from fetch_receipts.utils.scoring import ReceiptScorer

bp = Blueprint('receipts', __name__)

receipts = {}

@bp.route("/process", methods=['POST'])
def process_receipt():
    try:
        payload = ReceiptSchema().load(request.json)
    except ValidationError as error:
        return jsonify(error.messages), 400

    scorer = ReceiptScorer(payload)
    points = scorer.calculate_total_score()

    payload['points'] = points

    return jsonify({
        "payload": payload
    }), 200

@bp.route("/<receipt_id>/points", methods=['GET'])
def get_receipt_points(receipt_id):
    return {"points": "confirmed"}
