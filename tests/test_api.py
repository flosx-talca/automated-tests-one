from app.api import app
def test_make_reservation_available():
    client = app.test_client()
    response = client.post('/reservations', json={"room": "A", "time": "12:00"})
    assert response.status_code == 201
    assert response.get_json() == {"message": "Reservation made successfully"}
    pass
def test_make_reservation_not_available():
    client = app.test_client()
    # First reservation
    client.post('/reservations', json={"room": "A", "time": "12:00"})
    # Second reservation at the same time
    response = client.post('/reservations', json={"room": "A", "time": "12:00"})
    assert response.status_code == 409
    assert response.get_json() == {"message": "Room is not available at this time"}
