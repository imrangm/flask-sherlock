import pytest

from run import app as application


@pytest.fixture()
def app():
    application.config.update({
        "TESTING": True,
    })
    yield application


@pytest.fixture
def client(app):   
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_api(client):
    response = client.get("/api/v1/movies/recommend")
    assert response.status_code == 200
    assert response.is_json
    assert response.get_json()[0]["title"] != ""

    response = client.get("/api/v1/movies/recommend?title=Kingpin")
    assert response.status_code == 200
    assert response.is_json
    assert len(response.get_json()) >= 2

    response = client.get("/api/v1/movies/recommend?title=Lost%20in%20Translation")
    assert response.status_code == 200
    assert response.is_json
    assert len(response.get_json()) >= 5