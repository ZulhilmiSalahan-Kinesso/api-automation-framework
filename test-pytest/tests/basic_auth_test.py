import requests

def test_basic_authentication():
    authUrl = 'http://httpbin.org/basic-auth/foo/bar'
    username = 'foo'
    password = 'bar'
    req = requests.get(url=authUrl, auth=(username, password))
    assert req.status_code == 200
