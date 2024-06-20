from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from fetch_receipts.schemas import ReceiptSchema

bp = Blueprint('receipts', __name__)

@bp.route("/process", methods=['POST'])
def process_receipt():
    try:
        payload = ReceiptSchema().load(request.json)
    except ValidationError as error:
        return jsonify(error.messages), 400

    return payload

@bp.route("/<receipt_id>/points", methods=['GET'])
def get_receipt_points(receipt_id):
    return {"points": "confirmed"}
