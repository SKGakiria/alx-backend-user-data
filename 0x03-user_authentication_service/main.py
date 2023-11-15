#!/usr/bin/env python3
"""The Main file"""
import requests


def register_user(email: str, password: str) -> None:
    """Tests the registration of a user"""
    url = "{}/users".format(BASE_URL)
    info = {
        'email': email,
        'password': password,
    }
    res = requests.post(url, data=info)
    if res.status_code == 200:
        assert (res.json() == {"email": email, "message": "user created"})
    else:
        assert (res.status_code == 400)
        assert (res.json() == {"message": "email already registered"})


def log_in_wrong_password(email: str, password: str) -> None:
    """Tests log in with wrong password credentials"""
    url = "{}/sessions".format(BASE_URL)
    info = {
        'email': email,
        'password': password,
    }
    res = requests.post(url, data=info)
    assert (res.status_code == 401)


def log_in(email: str, password: str) -> str:
    """Tests for log in"""
    url = "{}/sessions".format(BASE_URL)
    info = {
        'email': email,
        'password': password,
    }
    res = requests.post(url, data=info)
    assert res.status_code == 200
    assert (res.json() == {"email": email, "message": "logged in"})
    return res.cookies('session_id')


def profile_unlogged() -> None:
    """Tests for profile existence without being logged in"""
    url = "{}/profile".format(BASE_URL)
    res = requests.get(url)
    assert (res.status_code == 403)


def profile_logged(session_id: str) -> None:
    """Tests for profile existence while logged in"""
    url = "{}/profile".format(BASE_URL)
    cookies = {'session_id': session_id}
    res = requests.get(url, cookies=cookies)
    assert (res.status_code == 200)


def log_out(session_id: str) -> None:
    """Tests for log out"""
    BASE_URL = "http://127.0.0.1:5000/"
    url = "{}/sessions".format(BASE_URL)
    cookies = {'session_id': session_id}
    res = requests.delete(url, cookies=cookies)
    if res.status_code == 302:
        assert (res.url == BASE_URL)
    else:
        assert (res.status_code == 200)


def reset_password_token(email: str) -> str:
    """Tests for the resetting of a password"""
    url = "{}/reset_password".format(BASE_URL)
    info = {'email': email}
    res = requests.post(url, data=info)
    if res.status_code == 200:
        return res.json()['reset_token']
    assert (res.status_code == 401)


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Tests for updating of a password"""
    url = "{}/reset_password".format(BASE_URL)
    info = {'email': email, 'reset_token': reset_token,
            'new_password': new_password}
    res = requests.put(url, data=info)
    if res.status_code == 200:
        assert (res.json() == {"email": email, "message": "Password updated"})
    else:
        assert (res.status_code == 403)


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
