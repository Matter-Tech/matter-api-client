from matter_api_client.http_client import get, post, put, delete


def test_get(httpserver):
    body = '{"Hello": "Goodbye"}'
    endpoint = "/hello"
    httpserver.expect_request(endpoint).respond_with_data(body)
    result = get(httpserver.url_for(endpoint))
    assert result.text == body
    assert result.json == {"Hello": "Goodbye"}
    assert result.status_code == 200


def test_post_plain(httpserver):
    body = '{"Hello": "Goodbye"}'
    endpoint = "/hello"
    httpserver.expect_request(endpoint).respond_with_data(body)
    result = post(url=httpserver.url_for(endpoint))
    assert result.text == body
    assert result.json == {"Hello": "Goodbye"}
    assert result.status_code == 200


def test_post(httpserver):
    body = '{"Hello": "Goodbye"}'
    payload = {"Payload": "Data"}
    headers = {"Content-Type": "application/json"}
    endpoint = "/hello"
    httpserver.expect_request(endpoint).respond_with_data(body)
    result = post(url=httpserver.url_for(endpoint), payload=payload, headers=headers)
    assert result.text == body
    assert result.json == {"Hello": "Goodbye"}
    assert result.status_code == 200


def test_put_plain(httpserver):
    body = '{"Hello": "Goodbye"}'
    endpoint = "/hello"
    httpserver.expect_request(endpoint).respond_with_data(body)
    result = put(url=httpserver.url_for(endpoint))
    assert result.text == body
    assert result.json == {"Hello": "Goodbye"}
    assert result.status_code == 200


def test_put(httpserver):
    body = '{"Hello": "Goodbye"}'
    payload = {"Payload": "Data"}
    headers = {"Content-Type": "application/json"}
    endpoint = "/hello"
    httpserver.expect_request(endpoint).respond_with_data(body)
    result = put(url=httpserver.url_for(endpoint), payload=payload, headers=headers)
    assert result.text == body
    assert result.json == {"Hello": "Goodbye"}
    assert result.status_code == 200


def test_delete_plain(httpserver):
    body = '{"Hello": "Goodbye"}'
    endpoint = "/hello"
    httpserver.expect_request(endpoint).respond_with_data(body)
    result = delete(url=httpserver.url_for(endpoint))
    assert result.text == body
    assert result.json == {"Hello": "Goodbye"}
    assert result.status_code == 200


def test_delete(httpserver):
    body = '{"Hello": "Goodbye"}'
    payload = {"Payload": "Data"}
    headers = {"Content-Type": "application/json"}
    endpoint = "/hello"
    httpserver.expect_request(endpoint).respond_with_data(body)
    result = delete(url=httpserver.url_for(endpoint), payload=payload, headers=headers)
    assert result.text == body
    assert result.json == {"Hello": "Goodbye"}
    assert result.status_code == 200
