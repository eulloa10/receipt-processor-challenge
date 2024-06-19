from flask import Blueprint


bp = Blueprint('receipts', __name__)

@bp.route("/process", methods=['POST'])
def process_receipt():
    return {"process": "confirmed"}

@bp.route("/<receipt_id>/points", methods=['GET'])
def get_receipt_points(receipt_id):
    return {"points": "confirmed"}
