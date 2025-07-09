from flask import Flask, jsonify, request
from app.reservations import check_availability

app = Flask(__name__)

reservartions = []

@app.route('/reservations', methods=['POST'])
def make_reservation():
    data = request.get_json()
    is_available = check_availability(reservartions, data)

    if is_available:
        reservartions.append(data)
        return jsonify({"message": "Reservation made successfully"}), 201
    else:
        return jsonify({"message": "Room is not available at this time"}), 409  
    