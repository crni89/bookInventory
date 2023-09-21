from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Testiranje validacije datuma ako je foramt pogresan
def test_invalid_date_format():
    response = client.post("/books", json={
        "id": 1,
        "naslov": "Test knjiga",
        "autor": "Test autor",
        "isnb": "1234567890123",
        "datum": "01-01-2022"
    })
    assert response.status_code == 400
    assert response.json() == {"detail" : "Datum mora biti u formatu dd.mm.yyyy."}


# Testiranje validacije datuma ako je foramt tacan
def test_valid_date_format():
    response = client.post("/books", json={
        "id": 2,
        "naslov": "Test knjiga",
        "autor": "Test autor",
        "isnb": "1234567890123",
        "datum": "01.01.2022."
    })
    assert response.status_code == 200


# Testiranje validacije ISBN-a ako nema tacno 13 cifara
def test_invalid_isbn_length():
    response = client.post("/books", json={
        "id": 3,
        "naslov": "Test knjiga",
        "autor": "Test autor",
        "isnb": "12345678901",
        "datum": "01.01.2022."
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "ISBN mora sadrzati tacno 13 cifara."}


# Testiranje validacije ISBN-a ako ima tacno 13 cifara
def test_valid_isbn_length():
    response = client.post("/books", json={
        "id": 4,
        "naslov": "Test knjiga",
        "autor": "Test autor",
        "isnb": "1234567890123",
        "datum": "01.01.2022."
    })
    assert response.status_code == 200
