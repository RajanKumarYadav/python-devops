from app import app


# def test1():
#     response = app.test_client().get("/insert")
#     assert response.status_code == 200


# def test2():
#     response = app.test_client().get("/base")
#     assert response.status_code == 200


def test3():
    response = app.test_client().get("/base")
    assert b"My daily checklist" in response.data
