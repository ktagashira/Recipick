from fastapi.testclient import TestClient
from app.main import get_application

client = TestClient(get_application())


def test_greeting_root():
    response = client.get("/greeting/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_items_root():
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == [{"item_id": "Foo"}, {"item_id": "Bar"}]
